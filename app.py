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
# Load animations (your chosen set)
# ---------------------------
bear_attack = load_lottieurl("https://lottie.host/6ad9a891-4efc-4f6a-8962-0f612cb6ec65/w6vP4vXhVR.json")
snake_drop  = load_lottieurl("https://lottie.host/8b9e92fd-9b58-482b-a4a2-3cce30a3c2fa/1BwnXKw53G.json")
landslide   = load_lottieurl("https://lottie.host/52a98672-944e-4eb3-8e4e-43bbd9866f68/Zv6jQtvF2u.json")
victory     = load_lottieurl("https://lottie.host/1ef42a32-bb25-4474-a31a-f4a9b8c25b69/QQfM0gF6Q0.json")
game_over   = load_lottieurl("https://lottie.host/4b3fdf5a-4084-437e-b6c3-573a1a233acd/Rm4KqWbN2p.json")

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
        if bear_attack:
            st_lottie(bear_attack, height=300, key="bear")
        else:
            st.warning("⚠️ Bear animation failed to load")
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
        if snake_drop:
            st_lottie(snake_drop, height=300, key="snake")
        else:
            st.warning("⚠️ Snake animation failed to load")
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
        if landslide:
            st_lottie(landslide, height=300, key="landslide")
        else:
            st.warning("⚠️ Landslide animation failed to load")
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
    if game_over:
        st_lottie(game_over, height=250, key="over")
    st.button("🔄 Restart", on_click=restart)

elif st.session_state.victory:
    st.success("🌞 You survived the Jungle Night!")
    if victory:
        st_lottie(victory, height=250, key="victory")
    st.button("🔄 Restart", on_click=restart)

else:
    play_level(st.session_state.level)
