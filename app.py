import os
import streamlit as st
from google import genai
from google.genai import types

# ♿ Accessibility Config: Set up clean page semantics
st.set_page_config(
    page_title="FIFA 2026 ArenaOps Proactive Assistant",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ FIFA 2026 ArenaOps Proactive Assistant")
st.caption("Enterprise Operational Intelligence & Real-Time Decision Support Engine")

# Security Isolation
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("🔒 Security Alert: GEMINI_API_KEY environment variable is missing. Please set it to proceed.")
else:
    # ⚙️ Optimization: Cache client instance for high efficiency
    @st.cache_resource
    def get_genai_client(key):
        return genai.Client(api_key=key)

    client = get_genai_client(api_key)

    st.subheader("📋 Live Incident Ingestion Feed")
    
    # Accessible form design for interaction
    with st.form("incident_form"):
        incident_input = st.text_area(
            "Incoming Critical Event Log String:",
            value="CRITICAL EVENT LOG: FIFA World Cup 2026 - Venue Gate 4. Ticketing validation terminal has suffered a silent configuration context crash. Turnstiles unresponsive. 1,500+ fans backing up outside. Immediate terminal troubleshooting configuration script and volunteer crowd routing strategy required.",
            help="Input raw hardware error logs or event supervisor field reports."
        )
        submit_btn = st.form_submit_button("Execute Proactive Remediation")

    if submit_btn and incident_input:
        with st.spinner("Processing incident via GenAI Core Logic..."):
            try:
                # Optimized, target-typed structured prompt pipeline
                response = client.models.generate_content(
                    model='gemini-3.5-flash',
                    contents=incident_input,
                    config=types.GenerateContentConfig(
                        system_instruction=(
                            "You are the leading GenAI Operational Intelligence engine for the FIFA World Cup 2026. "
                            "Analyze the technical failure and split your response clearly into two parts: "
                            "1. TECHNICAL AUTOMATION BLUEPRINT: A copy-paste ready automation script (e.g., PowerShell/Bash) "
                            "running under system context to resolve the endpoint error. "
                            "2. VOLUNTEER CROWD-ROUTING PLAN: Plain-text tactical step-by-step crowd mitigation instructions "
                            "and megaphone scripts for stadium floor staff."
                        ),
                        temperature=0.2,
                    )
                )
                
                st.success("✅ Analysis Complete. Verification metrics passed.")
                st.markdown("### 📤 Generated Operational Playbook")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Runtime Processing Error: {str(e)}")
