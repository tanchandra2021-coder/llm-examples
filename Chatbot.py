import streamlit as st
from openai import OpenAI

# -------------------
# 🌟 Page Config
# -------------------
st.set_page_config(page_title="💼 HerStory Finance Chatbot", page_icon="💬", layout="centered")

# -------------------
# 📚 Sidebar - API Key
# -------------------
with st.sidebar:
    st.title("🔐 Settings")
    openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    st.markdown("[Get your API key](https://platform.openai.com/account/api-keys)")

# -------------------
# 👩‍💼 Women Leaders Data
# -------------------
leaders = {
    "Indra Nooyi": {
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/1/10/Indra_Nooyi_2011.jpg",
        "bio": "Former CEO of PepsiCo. Known for strategic thinking, sustainability, and visionary leadership in global markets.",
        "style": "Answer as Indra Nooyi would — strategic, practical, and focused on global business leadership and corporate growth."
    },
    "Christine Lagarde": {
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/0/09/Christine_Lagarde_2021.jpg",
        "bio": "President of the European Central Bank. Known for macroeconomic insights and global financial policy leadership.",
        "style": "Answer as Christine Lagarde would — authoritative, macroeconomic, and focused on monetary policy and global finance."
    },
    "Janet Yellen": {
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/5/50/Janet_Yellen_official_Federal_Reserve_portrait.jpg",
        "bio": "U.S. Secretary of the Treasury. Expert in economic policy, central banking, and fiscal responsibility.",
        "style": "Answer as Janet Yellen would — thoughtful, data-driven, and focused on economic stability and policy impacts."
    },
    "Suze Orman": {
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/5/52/Suze_Orman_2010.jpg",
        "bio": "Financial advisor and author. Renowned for empowering people to build wealth and financial security.",
        "style": "Answer as Suze Orman would — approachable, empowering, and focused on personal finance and wealth building."
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

# Display avatar + bio
st.image(leader["avatar"], width=180, caption=leader_name)
st.markdown(f"**About {leader_name}:** {leader['bio']}")

# -------------------
# 💬 Chat System
# -------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": f"You are {leader_name}. {leader['style']}"}
    ]

# Reset chat if leader changes
if "last_leader" not in st.session_state or st.session_state["last_leader"] != leader_name:
    st.session_state["messages"] = [
        {"role": "system", "content": f"You are {leader_name}. {leader['style']}"}
    ]
st.session_state["last_leader"] = leader_name

# Show previous messages
for msg in st.session_state["messages"][1:]:
    with st.chat_message("assistant" if msg["role"] == "assistant" else "user"):
        st.write(msg["content"])

# -------------------
# ✍️ Chat Input
# -------------------
if prompt := st.chat_input(f"Ask {leader_name} a finance or business question..."):
    if not openai_api_key:
        st.info("⚠️ Please enter your OpenAI API key in the sidebar to continue.")
        st.stop()

    # Display user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate assistant response
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=st.session_state["messages"]
    )
    reply = response.choices[0].message.content

    # Display assistant message
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
