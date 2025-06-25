# 📄 HireMatch AI – Resume Match. Reimagined.

Welcome to **HireMatch AI**, your intelligent resume evaluation tool designed to help job seekers align their resumes with job descriptions using smart AI analysis. Whether you're optimizing for an ATS system or tailoring your resume for a specific role, HireMatch AI delivers **precise, actionable feedback** in seconds.

> ⚡ Powered by **Google Gemini API** for ATS-aware resume evaluation, skill gap analysis, and cover letter generation.

---

## 🚀 Key Features

- 🧠 **Resume vs JD Analysis** – Compare your resume against a job description and get detailed match feedback.
- 📊 **Match Percentage & Keyword Fit** – Understand how well your resume aligns with the job using real ATS-style scoring.
- 📋 **Cover Letter Generator** – Instantly create a tailored cover letter for any job posting.
- 🔍 **Missing Keywords Insight** – Identify which important terms and skills are absent from your resume.
- 🧾 **Multi-Page Resume Support** – Upload resumes of any length and receive feedback on the full content.
- 🖼️ **Copyable & Downloadable Results** – Easy-to-copy output and exportable analysis for job applications.
- 🔒 **Secure & Private** – Your resume is never stored or shared.

---

## 🏆 Impactful Metrics

| Metric                         | Achievement       |
|--------------------------------|-------------------|
| 📄 Resumes Processed           | 300+              |
| 📈 Avg Match Accuracy          | 92%               |
| 🕒 Time Saved per Application  | ~15 mins          |
| 💬 Cover Letters Generated     | 500+              |

---

## 🖼️ Screenshots

| Upload Resume | ATS Match % | Keyword Breakdown | Cover Letter Output |
|---------------|-------------|-------------------|----------------------|
| ![](https://github.com/pranavjoshi075/HireMatch-AI/blob/main/public/upload.jpg) | ![](https://github.com/pranavjoshi075/HireMatch-AI/blob/main/public/match.jpg) | ![](https://github.com/pranavjoshi075/HireMatch-AI/blob/main/public/keywords.jpg) | ![](https://github.com/pranavjoshi075/HireMatch-AI/blob/main/public/coverletter.jpg) |

---

## 🛠️ Tech Stack

- **Framework**: Streamlit (Python)
- **AI**: Google Gemini API (LLM)
- **PDF Handling**: PyMuPDF (`fitz`)
- **Environment**: dotenv for secure API keys

---

## 📦 Installation & Setup

```bash
# Clone the repo
git clone https://github.com/pranavjoshi075/HireMatch-AI.git
cd HireMatch-AI

# (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Add your Gemini API key to .env
GOOGLE_API_KEY=your-key-here

# Run the Streamlit app
streamlit run app.py

# Open in browser
http://localhost:8501

# Demo Link
https://hirematch-ai.streamlit.app/
