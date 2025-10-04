import streamlit as st

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
        "style": "Answer as Indra Nooyi would — strategic, practical, and focused on global business leadership and corporate growth."
    },
    "Christine Lagarde": {
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/0/09/Christine_Lagarde_2021.jpg",
        "style": "Answer as Christine Lagarde would — authoritative, macroeconomic, and focused on monetary policy and global finance."
    },
    "Janet Yellen": {
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/5/50/Janet_Yellen_official_Federal_Reserve_portrait.jpg",
        "style": "Answer as Janet Yellen would — thoughtful, data-driven, and focused on economic stability and policy impacts."
    },
    "Suze Orman": {
        "avatar": "https://upload.wikimedia.org/wikipedia/commons/5/52/Suze_Orman_2010.jpg",
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
st.image(leader["avatar"], width=180, caption=leader_name)

# -------------------
# 💬 Chat Component with Puter.js
# -------------------
chat_html = f"""
<div>
  <input type="text" id="userInput" placeholder="Ask {leader_name} a finance or business question..." style="width: 80%;" />
  <button onclick="askGPT()">Send</button>
  <div id="output" style="margin-top: 20px;"></div>
</div>

<script src="https://js.puter.com/v2/"></script>
<script>
async function askGPT() {{
    const question = document.getElementById("userInput").value;
    const response = await puter.ai.chat(
        "You are {leader_name}. {leader['style']}\\nQuestion: " + question,
        {{ model: "gpt-5-mini" }}
    );
    document.getElementById("output").innerText = response;
}}
</script>
"""

st.components.v1.html(chat_html, height=400)

