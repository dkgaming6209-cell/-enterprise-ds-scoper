import os
import io
import streamlit as st
from pypdf import PdfReader
from google import genai
from google.genai import types

# --- STREAMLIT DASHBOARD CONFIGURATION ---
st.set_page_config(
    page_title="Enterprise DS Scoper Pro",
    page_icon="💼",
    layout="centered"
)

# Initialize Session Memory Matrix
if "summary_output" not in st.session_state:
    st.session_state.summary_output = ""

# Secure API Ingestion Layer (.streamlit/secrets.toml check)
api_key = st.secrets.get("GEMINI_API_KEY") if "GEMINI_API_KEY" in st.secrets else os.environ.get("GEMINI_API_KEY")

# =====================================================================
# 🚀 USER INTERFACE VIEWPORT
# =====================================================================
st.title("💼 Enterprise Data Science Scoper Pro")
st.caption("Convert abstract client problems into straightforward, structured developer roadmaps.")
st.markdown("---")

st.subheader("1. Ingest Client Problem Context")

# Unified Multi-Channel Intake Framework
user_input_context = st.text_area(
    "Paste client problem statements, notes, or notice text:",
    height=150,
    placeholder="Example: Client wants to reduce churn, but their data is fragmented across marketing and sales teams. They also need real-time prediction alerts."
)

uploaded_file = st.file_uploader(
    "Or upload the client's discovery PDF file:",
    type="pdf"
)

# Trigger Action Processing Block
if st.button("Generate Actionable Engineering Summary", use_container_width=True):
    if not api_key:
        st.error(
            "Missing Gemini API Key. Please configure GEMINI_API_KEY inside your local .streamlit/secrets.toml file.")
    elif not user_input_context.strip() and uploaded_file is None:
        st.error("Please provide client text or upload a discovery PDF to proceed.")
    else:
        with st.spinner("Analyzing client complexity constraints and building structural mapping trees..."):
            try:
                # Compile ingestion metrics from files or text
                combined_context = ""
                if uploaded_file is not None:
                    pdf_reader = PdfReader(uploaded_file)
                    for page in pdf_reader.pages:
                        combined_context += page.extract_text() or ""

                if user_input_context.strip():
                    combined_context += "\n\n" + user_input_context.strip()

                # Establish direct Google GenAI connection context
                client = genai.Client(api_key=api_key)

                system_prompt = (
                    "You are an Elite Technical Solutions Architect. Your job is to extract client problems and format them "
                    "for data scientists to build models instantly. Keep the output extremely punchy, straightforward, and short.\n\n"
                    "Structure your output using this exact layout:\n"
                    "### 📊 CLIENT PROBLEM BREAKDOWN TREE\n"
                    "(Create a visual structure diagram using indentation, pipes, and hyphens to illustrate problem branches if there are multiple parts/departments involved. For example:\n"
                    "Main Problem\n"
                    " ├── Branch A\n"
                    " │    └── Sub-issue\n"
                    " └── Branch B)\n\n"
                    "### 🎯 CORE ENGINE OBJECTIVE\n"
                    "(1 clear sentence summarizing the technical goal)\n\n"
                    "### 🛠️ STRIPPED-DOWN ACTIONABLE CHEATSHEET\n"
                    "(Use bullet points for up to 4 ultra-short, critical requirements maximum. Skip fluff words.)"
                )

                config = types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    temperature=0.1
                )

                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=f"Convert this client data into a straightforward roadmap:\n\n{combined_context}",
                    config=config
                )

                # Assign payload directly to state variable framework
                st.session_state.summary_output = response.text

            except Exception as ex:
                st.error(f"Scoping matrix engine failure node: {ex}")

# =====================================================================
# 📋 DATA SCIENTIST WORKSPACE WORKVIEW
# =====================================================================
if st.session_state.summary_output:
    st.markdown("---")
    st.subheader("📋 Straightforward Developer Roadmap")

    # Render native text framework using markdown styling vectors
    st.markdown(st.session_state.summary_output)

    # Clear active workspace context reset switch
    if st.button("Clear Summary Matrix", type="secondary"):
        st.session_state.summary_output = ""
        st.rerun()
