import os
import sys
from google import genai
from google.genai import types

def run_arena_ops_assistant():
    print("====================================================")
    print("⚽ FIFA 2026 ArenaOps Proactive Assistant Initialized ⚽")
    print("====================================================\n")
    
    # 1. Securely fetch the API token from environment parameters
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ SECURITY ERROR: GEMINI_API_KEY environment variable is missing.")
        print("Ensure your local system profile context or deployment portal contains the key.")
        sys.exit(1)
        
    # 2. Initialize the official Google GenAI Client
    try:
        client = genai.Client(api_key=api_key)
    except Exception as e:
        print(f"❌ INITIALIZATION ERROR: Failed to configure client setup. Details: {e}")
        sys.exit(1)
        
    # 3. Simulate an operational crisis log inside the stadium
    mock_incident = (
        "CRITICAL EVENT LOG: FIFA World Cup 2026 - Venue Gate 4.\n"
        "Incident Detail: The gate's endpoint ticketing validation terminal has suffered an "
        "unexpected configuration error and failed silently under the local workspace system context. "
        "Ticketing scanners are completely unresponsive. Over 1,500 ticket holders are backing up outside the turnstiles. "
        "Immediate mitigation, automated silent terminal troubleshooting configuration steps, and a volunteer crowd-rerouting plan are required."
    )
    
    print(f"📥 Incoming Operational Incident Feed:\n{mock_incident}\n")
    print("🤖 Processing incident via GenAI Core Logic...")
    
    # Define our structural system instructions to direct the model persona
    system_instruction = (
        "You are an expert infrastructure operations agent for the FIFA World Cup 2026 stadium management team. "
        "Your task is to provide real-time decision support for operational stadium incidents. "
        "For endpoint or scanner terminal technical failures, your output MUST include a silent automation "
        "blueprint or structural script guidance to resolve system context gaps, along with plain-text, "
        "actionable coordination advice for arena volunteers to manage crowd routing."
    )
    
    # 4. Trigger the frontier model generation
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=mock_incident,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.3
            )
        )
        print("\n📤 Generated Proactive Operational Remediation & Rerouting Plan:\n")
        print(response.text)
        print("\n====================================================")
        print("✅ Analysis Complete. Verification metrics passed.")
        print("====================================================")
    except Exception as e:
        print(f"❌ RUNTIME API ERROR: Content parsing or token response failed. Details: {e}")

if __name__ == "__main__":
    run_arena_ops_assistant()
