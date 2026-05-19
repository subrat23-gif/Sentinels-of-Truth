from typing import TypedDict
from langgraph.graph import StateGraph
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_ollama import ChatOllama
from pydantic import BaseModel
from typing import Literal
import sqlite3


# Defining the State 
class VerificationState(TypedDict):
    claim: str
    search_results: str
    verification_report: dict
    database_status: str
    final_decision: str

# This would do web search for our claim
search_tool = DuckDuckGoSearchRun()

# We would produce report from our llm and it would be in unstructured way so we use Pydantic to get our results in the way we want(structured)
class VerificationReport(BaseModel):
    verdict: Literal["True", "False", "Uncertain"]
    reasoning: str
    confidence: float 

# Initializing our model
llm = ChatOllama(
    model ="agent_alpha",
    temperature= 0.2
)

# Binding our tools
llm_with_tools = llm.bind_tools([search_tool])

# Structuring our output we got from llm
structured_output = llm_with_tools.with_structured_output(VerificationReport)


def agent_alpha(state:VerificationState):

    claim = state["claim"]

    # Search for the result
    search_results = search_tool.invoke(claim)
    
    # Prompt

    prompt = f"""

    Claim:{claim}
    Search Results:{search_results}

    Analyze the claim carefully.

    Important Rules:
    - If the claim is nonsensical, meaningless, ambiguous, or unverifiable,
      return verdict as "Uncertain".
    - Do not force True/False decisions when evidence is weak.
    - Use lower confidence scores for unverifiable or ambiguous claims.
    - Do not use placeholder-style wording like "[Claim]".
      Use natural explanatory language.

    Return:
    - verdict
    - reasoning
    - confidence

    Verdict must ONLY be one of:
    - True
    - False
    - Uncertain

    Return confidence as a decimal number between 0 and 1.
    """
    # Output
    report = structured_output.invoke(prompt)
 
    return{
        "search_results" : search_results ,
        "verification_report" : report.model_dump()
    }



def agent_beta(state:VerificationState):

    claim = state["claim"]
    report = state["verification_report"]
    
    # We establish connection to our claims database
    conn = sqlite3.connect("claims.db")
    cursor = conn.cursor()
    
    # If there would be duplicate available then we would discard our claim.
    cursor.execute(
        """
        Select * from claims
        where claim = ?
        """,(claim,)
    )
    
    existing = cursor.fetchone()
     
    
    if existing:
        existing_verdict = existing[2].strip().lower() # 2nd column is verdict 
        new_verdict = report["verdict"].strip().lower()

        if existing_verdict != new_verdict:
            conn.close()

            return{

                "database_status" : "FLAGGED" ,
                "final_decision" : "Contradictory verdict has been detected. Requires Human review."
            }
        else:
            conn.close()

            return {
                "database_status": "DISCARDED",
                "final_decision" : "This claim alreadyy exists with the same verdict."
            }
    
    cursor.execute(
        """
        Insert into claims(
            claim,
            verdict,
            reasoning,
            confidence,
            status
        )

        Values(?,?,?,?,?)

        """, 
        (
            claim,
            report["verdict"],
            report["reasoning"],
            report["confidence"],
            "INSERTED"
        )
        
    )

    conn.commit()

    conn.close()

    return {
        "database_status" : "INSERTED",
        "final_decision" : "Claim added to database."
    }


#----------------- GRAPH -------------

graph = StateGraph(VerificationState)

graph.add_node("alpha_node" , agent_alpha)
graph.add_node("beta_node",agent_beta)

graph.set_entry_point("alpha_node")

graph.add_edge("alpha_node","beta_node")

graph.set_finish_point("beta_node")

#-------------------COMPILE--------------

app = graph.compile()

