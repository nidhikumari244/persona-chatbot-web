# PERSONA Chatbot (Streamlit + Groq)

A persona-based AI chatbot built with Streamlit and Groq API. Users can chat with different personalities (`friend`, `teacher`, `sibling`, and `custom`).

## Live Demo

- https://persona-chatbot-web.streamlit.app/

## Features

- Chat UI using `st.chat_message` and `st.chat_input`
- Persona switching from sidebar
- Custom persona prompt support
- Session-based chat history
- One-click clear chat history
- Secure API key usage via `.env` (local) or Streamlit secrets (cloud)

## Project Structure

```text
persona-chatbot-web/
  streamlit_app.py
  requirements.txt
  .gitignore
  .env.example
  README.md
```

## Local Setup

1. Clone or open the project folder.
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create `.env` file from `.env.example` and add your Groq API key:
   ```env
   GROQ_API_KEY=your_actual_key
   ```
5. Run app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Deploy on Streamlit Community Cloud

1. Push this folder to a new GitHub repo.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click **New app** and connect your GitHub repo.
4. Set main file path as: `streamlit_app.py`.
5. In app settings, add secret:
   ```toml
   GROQ_API_KEY="your_actual_key"
   ```
6. Deploy.

## Add to Resume

Use this format in your resume:

- **PERSONA Chatbot** | Python, Streamlit, Groq API
- Built and deployed a persona-driven conversational AI app with configurable system prompts and session-based memory.
- Live demo: https://persona-chatbot-web.streamlit.app/
- GitHub: https://github.com/<your-username>/<your-repo-name>

## Notes

- Never commit `.env` or any secret keys.
- If you change model name, update `MODEL` in `streamlit_app.py`.
