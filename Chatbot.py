import streamlit as st
import openai

# -------------------
# 👩‍💻 Leader Selection
# -------------------
leader_name = st.selectbox("👩 Choose a leader to chat with:", list(leaders.keys()))
leader = leaders[leader_name]
st.image(leader["avatar"], width=180, caption=leader_name)

# -------------------
# 🔑 OpenAI API Key
# -------------------
# Recommended: store as environment variable for security
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

# -------------------
# 💬 Chat History
# -------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": f"You are a financial expert, {leader_name}, speaking in a {leader['style']} style."}
    ]

# Reset chat if leader changes
if "last_leader" not in st.session_state or st.session_state["last_leader"] != leader_name:
    st.session_state.messages = [
        {"role": "system", "content": f"You are a financial expert, {leader_name}, speaking in a {leader['style']} style."}
    ]
st.session_state.last_leader = leader_name

# Display previous messages
for msg in st.session_state.messages[1:]:
    with st.chat_message("assistant" if msg["role"] == "assistant" else "user"):
        st.write(msg["content"])

# -------------------
# ✍️ Chat Input
# -------------------
if prompt := st.chat_input(f"Ask {leader_name} a finance or business question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Call OpenAI GPT-3.5 for response
    with st.spinner(f"{leader_name} is thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5",
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=300
        )
        reply = response['choices'][0]['message']['content']

    # Append and display assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
