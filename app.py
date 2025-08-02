import streamlit as st
import random

# --- Setup ---
st.set_page_config(page_title="Monikers 🇮🇳", layout="centered")
st.title("🎭 Monikers – Indian Edition")

# --- Card Data ---
cards = [
    {
        "name": "Shah Rukh Khan",
        "description": "King of Bollywood, known for DDLJ.",
        "points": 2,
    },
    {
        "name": "Draupadi",
        "description": "Wife of the Pandavas in the Mahabharata.",
        "points": 3,
    },
    {
        "name": "Rasode Mein Kaun Tha",
        "description": "Viral meme with Kokilaben.",
        "points": 1,
    },
    {"name": "Sachin Tendulkar", "description": "God of Cricket.", "points": 2},
    {
        "name": "Bahubali",
        "description": "Warrior who lifted the shivling.",
        "points": 2,
    },
    {
        "name": "Chandrayaan-3",
        "description": "India’s successful moon mission.",
        "points": 3,
    },
    {
        "name": "Rajnikanth",
        "description": "Superstar with legendary stunts.",
        "points": 2,
    },
    {"name": "MS Dhoni", "description": "Cool-headed cricket captain.", "points": 2},
    {"name": "Yogi Adityanath", "description": "CM of Uttar Pradesh.", "points": 2},
]

# --- Initialize session state ---
if "round" not in st.session_state:
    st.session_state.round = 1
if "active_team" not in st.session_state:
    st.session_state.active_team = "Team A"
if "scores" not in st.session_state:
    st.session_state.scores = {"Team A": 0, "Team B": 0}
if "round_deck" not in st.session_state:
    st.session_state.round_deck = random.sample(cards, len(cards))
if "guessed_cards" not in st.session_state:
    st.session_state.guessed_cards = []
if "current_card" not in st.session_state:
    st.session_state.current_card = None


# --- Helper Functions ---
def draw_new_card():
    if st.session_state.round_deck:
        st.session_state.current_card = st.session_state.round_deck.pop(0)
    else:
        st.session_state.current_card = None


def handle_guess():
    card = st.session_state.current_card
    if card:
        st.session_state.scores[st.session_state.active_team] += card["points"]
        st.session_state.guessed_cards.append(card)
        st.session_state.current_card = None
        draw_new_card()


def handle_skip():
    card = st.session_state.current_card
    if card:
        st.session_state.round_deck.append(card)
        st.session_state.current_card = None
        draw_new_card()


def switch_team():
    st.session_state.active_team = (
        "Team B" if st.session_state.active_team == "Team A" else "Team A"
    )
    random.shuffle(st.session_state.round_deck)
    st.session_state.current_card = None
    draw_new_card()


def next_round():
    if st.session_state.round_deck:
        st.warning("⛔ Finish all cards before starting the next round!")
        return
    if st.session_state.round == 1:
        # Move to round 2 with guessed cards from round 1
        if not st.session_state.guessed_cards:
            st.warning("No guessed cards to proceed with for next round!")
            return
        st.session_state.round += 1
        st.session_state.round_deck = random.sample(
            st.session_state.guessed_cards, len(st.session_state.guessed_cards)
        )
        st.session_state.guessed_cards = []
    else:
        # Subsequent rounds continue with previously guessed cards
        if not st.session_state.guessed_cards:
            st.warning("No guessed cards to proceed with for next round!")
            return
        st.session_state.round += 1
        st.session_state.round_deck = random.sample(
            st.session_state.guessed_cards, len(st.session_state.guessed_cards)
        )
        st.session_state.guessed_cards = []
    st.session_state.current_card = None
    draw_new_card()


# --- Game UI ---
st.markdown(f"### 🎯 Round {st.session_state.round}")
st.markdown(f"**Current Team:** {st.session_state.active_team}")
st.markdown(
    f"**Team A Score:** {st.session_state.scores['Team A']} | **Team B Score:** {st.session_state.scores['Team B']}"
)

if not st.session_state.current_card:
    draw_new_card()

card = st.session_state.current_card
if card:
    st.markdown("----")
    st.markdown(f"🃏 **Card**: `{card['name']}`")
    st.markdown(f"💡 **Hint**: _{card['description']}_")
    st.markdown(f"🏅 **Points**: {card['points']}")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Guessed"):
            handle_guess()
    with col2:
        if st.button("⏭️ Skip"):
            handle_skip()
else:
    st.success("✅ All cards in this round are done!")

st.markdown("----")
col3, col4 = st.columns(2)
with col3:
    if st.button("🔁 Switch Team"):
        switch_team()
with col4:
    if st.button("➡️ Next Round"):
        next_round()
