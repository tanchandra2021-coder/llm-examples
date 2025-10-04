import streamlit as st
from gpt4all import GPT4All

# -------------------
# 🌟 Page Config
# -------------------
st.set_page_config(page_title="💼 HerStory Finance Chatbot", page_icon="💬", layout="centered")

# -------------------
# 👩‍💼 Women Leaders Data
# -------------------
leaders = {
    "Indra Nooyi": {
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/1/10/Indra_Nooyi_2011.jpg",
        "style": "strategic, practical, and focused on global business leadership and corporate growth"
    },
    "Christine Lagarde": {
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/0/09/Christine_Lagarde_2021.jpg",
        "style": "authoritative, macroeconomic, and focused on monetary policy and global finance"
    },
    "Janet Yellen": {
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/5/50/Janet_Yellen_official_Federal_Reserve_portrait.jpg",
        "style": "thoughtful, data-driven, and focused on economic stability and policy impacts"
    },
    "Suze Orman": {
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/5/52/Suze_Orman_2010.jpg",
        "style": "approachable, empowering, and focused on personal finance and wealth building"
    }
}

# -------------------
# 🎨 UI - Header
# -------------------
st.title("💼 HerStory Finance Chatbot")
st.caption("💬 Ask questions about business, economics, or personal finance — answered in the voice of iconic women leaders.")

# -------------------
# 👩‍💻 Leader Selection
# -------------------
leader_name = st.selectbox("👩 Choose a leader to chat with:", list(leaders.keys()))
leader = leaders[leader_name]
st.image(leader["avatar"], width=180, caption=leader_name)

# -------------------
# 💬 Initialize GPT4All
# -------------------
if "model" not in st.session_state:
    st.session_state.model = GPT4All("ggml-gpt4all-j-v1.3-groovy")  # Free local model

# -------------------
# 💬 Chat History
# -------------------
if "messages" not in st.session_state:
    # Start with a system message defining the leader persona
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
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Prepare GPT4All prompt including full conversation for context
    conversation = "\n".join(
        [f"{'User' if m['role']=='user' else leader_name}: {m['content']}" for m in st.session_state.messages[1:]]
    )
    system_msg = st.session_state.messages[0]["content"]
    full_prompt = f"{system_msg}\n{conversation}\n{leader_name}:"

    # Generate assistant response
    reply = st.session_state.model.generate(full_prompt, max_tokens=300)
    
    # Display assistant response
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)

