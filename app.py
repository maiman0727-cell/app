import streamlit as st
import sqlite3
import datetime
from streamlit_autorefresh import st_autorefresh

# ---------------------------
# DB setup
# ---------------------------
conn = sqlite3.connect("chat.db", check_same_thread=False)
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nickname TEXT,
                message TEXT,
                timestamp TEXT
            )""")
conn.commit()

# ---------------------------
# Session setup
# ---------------------------
if "nickname" not in st.session_state:
    st.session_state.nickname = None

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
    <style>
        body, .stApp {
            background-color: #FFD700; /* Yellow background */
            color: black;
        }
        .chat-box {
            padding: 10px;
            margin: 5px 0;
            border-radius: 10px;
            background: rgba(0,0,0,0.05);
        }
        .nickname {
            font-weight: bold;
        }
        .time {
            font-size: 0.8em;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# Nickname input
# ---------------------------
if not st.session_state.nickname:
    st.title("🕵️ Secret Hub")
    st.subheader("Enter your nickname to join the chat")
    nickname = st.text_input("Nickname:")
    if st.button("Join Chat") and nickname.strip() != "":
        st.session_state.nickname = nickname.strip()
        st.experimental_rerun()
else:
    st.title("🕵️ Secret Hub")
    st.caption(f"Logged in as: **{st.session_state.nickname}**")

    # ---------------------------
    # Auto refresh every 3s
    # ---------------------------
    st_autorefresh(interval=3000, key="chatrefresh")

    # ---------------------------
    # Chat input
    # ---------------------------
    with st.form("chat_form", clear_on_submit=True):
        message = st.text_input("Type a message:")
        send = st.form_submit_button("Send")
        if send and message.strip() != "":
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.execute("INSERT INTO messages (nickname, message, timestamp) VALUES (?, ?, ?)",
                      (st.session_state.nickname, message.strip(), now))
            conn.commit()

    # ---------------------------
    # Display messages
    # ---------------------------
    st.subheader("💬 Community Chat")
    c.execute("SELECT nickname, message, timestamp FROM messages ORDER BY id DESC LIMIT 30")
    rows = c.fetchall()[::-1]  # show newest at bottom
    for nick, msg, ts in rows:
        st.markdown(f"""
            <div class="chat-box">
                <span class="nickname">{nick}:</span> {msg}<br>
                <span class="time">🕒 {ts}</span>
            </div>
        """, unsafe_allow_html=True)
