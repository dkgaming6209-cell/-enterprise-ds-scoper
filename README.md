# 💼 Enterprise DS Scoper Pro

An ultra-focused, AI-driven automation framework designed to translate abstract client problem statements or discovery PDFs into crisp, branching engineering summaries for data science teams.

## 🌟 Core Features
- **Multi-Channel Intake**: Seamlessly processes pasted raw business text or uploaded client notice PDFs.
- **Visual Branching Trees**: Automatically structures complex, multi-department corporate problems into clear markdown hierarchical maps.
- **Actionable Engineering Cheatsheet**: Strips out narrative fluff to provide an ultra-short, critical task list for immediate development.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR_REPOSITORY_NAME
   ```

2. **Install requirements:**
   ```bash
   pip install streamlit pypdf google-genai
   ```

3. **Configure your API Secrets:**
   Create a hidden folder named `.streamlit` in the root folder, add a file named `secrets.toml` inside it, and insert your Google Gemini token:
   ```toml
   # .streamlit/secrets.toml
   GEMINI_API_KEY = "your_actual_gemini_api_key_here"
   ```

4. **Launch the application server:**
   ```bash
   streamlit run app.py
   ```

## 🔒 Security
This repository includes a `.gitignore` baseline that strictly prevents local session files and `.streamlit/secrets.toml` from being tracked or pushed to public environments.
