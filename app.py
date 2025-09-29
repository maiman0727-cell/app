import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ---------------------------
# Helper to load animations
# ---------------------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---------------------------
# Load animations (placeholders – replace URLs from lottiefiles.com)
# ---------------------------
bear_attack = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_9xcyig6e.json")
snake_drop  = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_bHWmMT.json")
landslide   = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_t24tpvcu.json")
victory     = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_q5pk6p1k.json")
game_over   = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jtbfg2nb.json")

# ---------------------------
# Session state
# ---------------------------
if "level" not in st.session_state:
    st.session_state.level = 1
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "victory" not in st.session_state:
    st.session_state.victory = False

# ---------------------------
# Restart function
# ---------------------------
def restart():
    st.session_state.level = 1
    st.session_state.game_over = False
    st.session_state.victory = False

# ---------------------------
# Game logic
# ---------------------------
def play_level(level):
    if level == 1:
        st.header("🌙 Level 1: The Bear")
        st_lottie(bear_attack, height=300, key="bear")
        st.write("A bear charges at you! What will you do?")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("⬅️ Left"):
                st.session_state.level += 1
        with col2:
            if st.button("➡️ Right"):
                st.session_state.level += 1
        with col3:
            if st.button("⬆️ Jump"):
                st.session_state.game_over = True
        with col4:
            if st.button("🙈 Hide"):
                st.session_state.game_over = True

    elif level == 2:
        st.header("🐍 Level 2: The Snake")
        st_lottie(snake_drop, height=300, key="snake")
        st.write("A snake drops from the trees! What will you do?")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("⬅️ Left"):
                st.session_state.game_over = True
        with col2:
            if st.button("➡️ Right"):
                st.session_state.game_over = True
        with col3:
            if st.button("⬆️ Jump"):
                st.session_state.level += 1
        with col4:
            if st.button("🙈 Hide"):
                st.session_state.game_over = True

    elif level == 3:
        st.header("⛰️ Level 3: Landslide")
        st_lottie(landslide, height=300, key="landslide")
        st.write("The mountain is collapsing! What will you do?")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("⬅️ Left"):
                st.session_state.game_over = True
        with col2:
            if st.button("➡️ Right"):
                st.session_state.game_over = True
        with col3:
            if st.button("⬆️ Jump"):
                st.session_state.game_over = True
        with col4:
            if st.button("🙈 Hide"):
                st.session_state.victory = True

# ---------------------------
# Game rendering
# ---------------------------
st.title("🌌 Endless Jungle Night (Demo v1)")

if st.session_state.game_over:
    st.error("☠️ The jungle has claimed you...")
    st_lottie(game_over, height=250, key="over")
    st.button("🔄 Restart", on_click=restart)

elif st.session_state.victory:
    st.success("🌞 You survived the Jungle Night!")
    st_lottie(victory, height=250, key="victory")
    st.button("🔄 Restart", on_click=restart)

else:
    play_level(st.session_state.level)
