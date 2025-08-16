import streamlit as st
import random

# Wide layout so everything fits without scrolling
st.set_page_config(page_title="🤖 Rock-Paper-Scissors AI", layout="wide")
# Game Options & Dummy Image Paths (you can replace the image paths) -
options = {0: ("Rock", "images/rock.png"), 1: ("Paper", "images/paper.png"), 2: ("Scissor", "images/scissor.png")}



# --- Session State Initialization ---
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.draws = 0
    st.session_state.user_moves = {0: 0, 1: 0, 2: 0}
    st.session_state.user_choice = None
    st.session_state.computer_choice = None
    st.session_state.result = None


# --- AI Choice Function (same logic as before) ---
def ai_choice():
    if sum(st.session_state.user_moves.values()) <= 1:
        return random.randint(0, 2)
    predicted_user_move = max(st.session_state.user_moves, key=st.session_state.user_moves.get)
    return (predicted_user_move + 1) % 3


# --- Determine Winner (same logic as before) ---
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        st.session_state.draws += 1
        return "DRAW!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        st.session_state.user_score += 1
        return "YOU WIN!"
    else:
        st.session_state.computer_score += 1
        return "COMPUTER WINS!"



# ---------------- UI ----------------
st.title("✊✋✌️ Rock-Paper-Scissors with AI Opponent")

# LEFT SIDEBARRrr: Scoreboard + Make Your Move 
with st.sidebar:
    st.header("📊 Scoreboard")
    st.write(f"You: {st.session_state.user_score}")
    st.write(f"Computer: {st.session_state.computer_score}")
    st.write(f"Draws: {st.session_state.draws}")

    st.markdown("---")
    st.header("🕹️ Make Your Move")

    sb1, sb2, sb3 = st.columns(3)
    with sb1:
        if st.button("✊ Rock"):
            st.session_state.user_choice = 0
            st.session_state.user_moves[0] += 1
            st.session_state.computer_choice = ai_choice()
            st.session_state.result = determine_winner(st.session_state.user_choice, st.session_state.computer_choice)
    with sb2:
        if st.button("✋ Paper"):
            st.session_state.user_choice = 1
            st.session_state.user_moves[1] += 1
            st.session_state.computer_choice = ai_choice()
            st.session_state.result = determine_winner(st.session_state.user_choice, st.session_state.computer_choice)
    with sb3:
        if st.button("✌️ Scissor"):
            st.session_state.user_choice = 2
            st.session_state.user_moves[2] += 1
            st.session_state.computer_choice = ai_choice()
            st.session_state.result = determine_winner(st.session_state.user_choice, st.session_state.computer_choice)




# MAIN AREA: Left = You (image), Right = Computer (image) 
col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 You")
    if st.session_state.user_choice is not None:
        st.image(options[st.session_state.user_choice][1], caption=options[st.session_state.user_choice][0], use_container_width=True)
    else:
        st.image("images/placeholder.png", caption="Your Move", use_container_width=True)

with col2:
    st.subheader("💻 Computer")
    if st.session_state.computer_choice is not None:
        st.image(options[st.session_state.computer_choice][1], caption=options[st.session_state.computer_choice][0], use_container_width=True)
    else:
        st.image("images/placeholder.png", caption="AI Move", use_container_width=True)

st.markdown("---")


# Result text beneath the images
if st.session_state.result:
    st.subheader(st.session_state.result)
    # Visuals
    if st.session_state.result == "YOU WIN!":
        st.balloons()
    elif st.session_state.result == "COMPUTER WINS!":
        st.error("💥 You Lost!")
    else:
        st.info("🤝 It's a Draw!")

