import streamlit as st
from backend import app



# PAGE CONFIG

st.set_page_config(
    page_title="Sentinels of Truth",
    layout="wide"
)


# =========================
# SIDEBAR
# =========================

st.sidebar.title("Sentinels of Truth")

st.sidebar.markdown("""
### Multi-Agent Verification System

#### Technologies Used
- LangGraph
- Ollama
- Streamlit
- SQLite
- DuckDuckGo Search
- Pydantic

---

#### Agent Workflow

1. Agent Alpha investigates claims
2. External search verification
3. Agent Beta checks database
4. Claim is INSERTED / DISCARDED / FLAGGED

---

#### Features
- Contradiction Detection  
- Persistent Knowledge Base  
- Structured Outputs  
- Uncertainty Handling  
- Multi-Agent Architecture
""")


# =========================
# MAIN TITLE
# =========================

st.title("Sentinels of Truth")

st.markdown("""
AI-powered Multi-Agent Claim Verification & Knowledge Management System
""")


# INPUT SECTION

claim = st.text_area(
    label="Enter a claim to verify",
    placeholder="Example: Drinking coffee increases lifespan.",
    height=150
)



# VERIFY BUTTON

if st.button("Verify Claim"):

    # Empty Input Check
    if not claim.strip():

        st.warning("Please enter a claim before verification.")

    else:

        # Loading Spinner
        with st.spinner("Investigating claim..."):

            result = app.invoke({
                "claim": claim
            })

    
        # REPORT EXTRACTION

        report = result["verification_report"]

        verdict = report["verdict"]
        confidence = report["confidence"]
        reasoning = report["reasoning"]

        status = result["database_status"]


        
        # DIVIDER

        st.divider()


        
        # VERIFICATION REPORT

        st.subheader("Verification Report")


        # Metrics Row
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                label="Verdict",
                value=verdict
            )

        with col2:
            st.metric(
                label="Confidence",
                value=f"{confidence:.2f}"
            )


        
        # REASONING

        st.markdown("### Reasoning")

        st.write(reasoning)


        
        # DATABASE STATUS

        st.markdown("### Database Status")


        if status == "INSERTED":

            st.success(
                "Claim inserted into database."
            )

        elif status == "DISCARDED":

            st.warning(
                "Duplicate claim detected."
            )

        elif status == "FLAGGED":

            st.error(
                "Contradictory claim detected. Human review required."
            )


        
        # FINAL DECISION

        st.markdown("### Final Decision")

        st.info(
            result["final_decision"]
        )


        
        # SEARCH RESULTS
        
        with st.expander("View Search Results"):

            st.write(
                result["search_results"]
            )



# FOOTER

st.divider()

st.caption(
    "Built using LangGraph, Ollama, Streamlit, and SQLite"
)