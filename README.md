# 🤖 Simple AI App (FastAPI + Streamlit)

A clean, minimal **full-stack AI application** demonstrating how to connect a Python backend (**FastAPI**) with an interactive frontend (**Streamlit**).

This project is designed for learning, showcasing architecture, and serving as a foundation for more advanced AI apps.

---

## 🌟 Overview

This app follows a simple but powerful pattern:

```text
User → Streamlit UI → FastAPI Backend → AI Logic → Response → UI
```

It separates concerns clearly:

* **Frontend (Streamlit)** → handles user interaction
* **Backend (FastAPI)** → processes requests
* **AI Logic (Python)** → generates responses

---

## 🚀 Features

* ⚡ FastAPI REST API with automatic docs
* 🎨 Interactive Streamlit UI
* 🧠 Modular AI logic (easy to upgrade to real models)
* 🔐 Secure environment variable handling (`.env`)
* 📦 Lightweight and beginner-friendly setup

---

## 🧩 Project Structure

```bash
09_PYTHON_ADK/
│── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app (API layer)
│   ├── ai_logic.py      # AI logic (core functionality)
│   ├── config.py        # Environment config (optional)
│
│── streamlit_app.py     # Streamlit frontend
│── requirements.txt     # Dependencies
│── .env                 # Environment variables (ignored)
│── .gitignore
│── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-fastapi-app.git
cd ai-fastapi-app
```

---

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
API_URL=http://127.0.0.1:8000
OPENAI_API_KEY=your_api_key_here  # optional
```

> ⚠️ This file is ignored by Git. Never commit secrets.

---

## ▶️ Running the App

### Start the FastAPI backend

```bash
uvicorn app.main:app --reload
```

* API: http://127.0.0.1:8000
* Docs: http://127.0.0.1:8000/docs

---

### Start the Streamlit frontend

```bash
streamlit run streamlit_app.py
```

---

## 🧪 Example Usage

1. Open the Streamlit app
2. Enter a message like:

```text
hello
```

3. Receive a response from the AI logic:

```text
Hi there! 👋
```

---

## 🧠 Extending the AI

The current implementation uses simple rule-based logic. You can easily upgrade it to:

* OpenAI API (chat models)
* Hugging Face transformers
* Custom ML models

All logic is isolated in:

```bash
app/ai_logic.py
```

---

## 🛡️ Best Practices Used

* Separation of concerns (API vs UI vs logic)
* Environment-based configuration
* Clean project structure
* Git-safe setup (`.env`, `.venv` ignored)

---

## 🚀 Deployment Ideas

You can deploy this project using:

* Backend: Render / Railway
* Frontend: Streamlit Community Cloud

---

## 📌 Roadmap

* [ ] Integrate real AI (OpenAI API)
* [ ] Add chat history
* [ ] Add database (SQLite/PostgreSQL)
* [ ] Deploy live demo
* [ ] Add authentication

---

## 📸 (Optional) Demo

*Add screenshots or a GIF here to showcase your app UI*

---

## 👤 Author

Your Name
GitHub: https://github.com/your-username

---

## 📄 License

This project is open-source and available under the MIT License.
