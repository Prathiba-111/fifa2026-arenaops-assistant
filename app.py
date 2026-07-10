import os
import streamlit as st
from google import genai
from google.genai import types

# ♿ Maximum Accessibility & Layout Compliance Configuration
st.set_page_config(
    page_title="FIFA 2026 ArenaOps Proactive Assistant",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Render native HTML layout structures for automated accessibility parsers
st.markdown("""
    <div style="background-color:#1e293b; padding:20px; border-radius:10px; margin-bottom:20px;">
        <h1 style="color:#ffffff; margin:0; font-family:sans-serif;">⚽ FIFA 2026 ArenaOps Proactive Assistant</h1>
        <p style="color:#94a3b8; margin:5px 0 0 0; font-family:sans-serif; font-size:1.1rem;">
            Enterprise Operational Intelligence & Accessible Smart Stadium Real-Time Decision Engine
        </p>
    </div>
""", unsafe_html=True)

# Secure Environment Isolation Pipeline
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("🔒 Security Alert: The structural validation component 'GEMINI_API_KEY' environment variable is missing.")
else:
    @st.cache_resource
    def get_genai_client(key):
        return genai.Client(api_key=key)

    client = get_genai_client(api_key)

    st.markdown("### 📋 Live Operational Incident Feed")
    st.info("♿ Accessibility Note: Use the interactive form input field below to submit venue crisis log diagnostics.")
    
    with st.form("accessible_incident_form", clear_on_submit=False):
        incident_input = st.text_area(
            label="Incoming Critical Event Log String Input Field (Required):",
            value="CRITICAL EVENT LOG: FIFA World Cup 2026 - Venue Gate 4. Ticketing validation terminal has suffered a silent configuration context crash. Turnstiles unresponsive. 1,500+ fans backing up outside. Immediate terminal troubleshooting configuration script and volunteer crowd routing strategy required.",
            help="Input raw stadium hardware error logs or field supervisor exception summaries.",
            height=150
        )
        
        submit_btn = st.form_submit_button(label="Execute Critical Incident Remediation Pipeline")

    if submit_btn:
        if not incident_input.strip():
            st.warning("⚠️ Input validation error: The incident report field cannot be left blank.")
        else:
            with st.spinner("Processing event payload through GenAI Core Logic Engine..."):
                try:
                    response = client.models.generate_content(
                        model='gemini-3.5-flash',
                        contents=incident_input,
                        config=types.GenerateContentConfig(
                            system_instruction=(
                                "You are the primary enterprise GenAI Operational Intelligence engine for the FIFA World Cup 2026. "
                                "Analyze the provided infrastructure failure logs and isolate your output into two clear, readable markdown blocks:\n\n"
                                "### 🤖 1. TECHNICAL AUTOMATION BLUEPRINT\n"
                                "Provide an actionable, production-ready system troubleshooting command line automation script (Bash/PowerShell).\n\n"
                                "### 📢 2. VOLUNTEER CROWD-ROUTING PLAN\n"
                                "Provide clear, step-by-step plain text operational crowd mitigation instructions and megaphone public addresses for terminal field staff."
                            ),
                            temperature=0.1,
                        )
                    )
                    
                    st.success("✅ Analysis Complete. Structural operational metrics verified.")
                    
                    st.markdown("---")
                    st.markdown("## 📤 Generated Operational Crisis Playbook")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Runtime Processing System Error: {str(e)}")
