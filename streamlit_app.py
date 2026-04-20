import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

PERSONA_PROMPTS = {
    "friend": (
        "You are a friendly, supportive companion who speaks casually, offers encouragement, "
        "and shares light-hearted banter. Respond with warmth and enthusiasm, like a close friend."
    ),
    "teacher": (
        "You are a knowledgeable, patient educator who explains concepts clearly and concisely. "
        "Provide structured answers with examples, like a dedicated teacher."
    ),
    "sibling": (
        "You are a playful, relatable sibling who teases gently, shares inside jokes, and offers "
        "honest advice. Respond with a mix of humor and care, like a brother or sister."
    ),
    "custom": (
        "You are {custom_character}, a character defined by the user. Adopt the personality, tone, "
        "and traits described by the user for this character."
    ),
}


def get_groq_response(messages):
    if not GROQ_API_KEY:
        return "Error: GROQ_API_KEY is missing. Add it to .env or Streamlit secrets."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}",
    }
    payload = {
        "model": MODEL,
        "messages": messages,
        "max_tokens": 1000,
        "temperature": 0.7,
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as exc:
        return f"Error: Unable to get response from Groq API. {exc}"


st.set_page_config(page_title="PERSONA Chatbot", page_icon="🤖")
st.title("🤖 PERSONA Chatbot")
st.caption("A fast, AI-powered chatbot powered by Groq")

with st.sidebar:
    st.header("Chatbot Persona")
    persona = st.selectbox("Choose a persona:", ["friend", "teacher", "sibling", "custom"], index=0)

    custom_character = ""
    if persona == "custom":
        custom_character = st.text_input(
            "Specify your custom character",
            placeholder="e.g., a wise wizard or a sarcastic detective",
        )

    if st.button("Clear Chat History"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm ready to chat. What's on your mind?"}
        ]
        st.success("Chat history cleared")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm ready to chat. What's on your mind?"}
    ]

system_prompt = PERSONA_PROMPTS[persona]
if persona == "custom" and custom_character:
    system_prompt = PERSONA_PROMPTS["custom"].format(custom_character=custom_character)
elif persona == "custom" and not custom_character:
    system_prompt = "You are a helpful assistant with a neutral tone."

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    api_messages = [{"role": "system", "content": system_prompt}, *st.session_state.messages]

    with st.chat_message("assistant"):
        answer = get_groq_response(api_messages)
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
