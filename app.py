import streamlit as st
import random

# --- Setup ---
st.set_page_config(page_title="Monikers 🇮🇳", layout="centered")
st.title("🎭 Monikers – Indian Edition")

# --- Card Data ---
cards = [
    {
        "name": "Shah Rukh Khan",
        "description": "King of Bollywood, known for DDLJ.\nRomantic hero with signature arm spread.\nOwner of Kolkata Knight Riders.\nFamous dialogue: 'Bade bade deshon mein'.\nReferred to as SRK by fans.",
        "points": 2,
    },
    {
        "name": "Draupadi",
        "description": "Wife of the Pandavas in the Mahabharata.\nCause of the great Kurukshetra war.\nBorn from sacrificial fire.\nHumiliated in the royal court.\nSymbol of women's strength and dignity.",
        "points": 3,
    },
    {
        "name": "Rasode Mein Kaun Tha",
        "description": "Viral meme with Kokilaben.\nFrom the TV serial Saath Nibhaana Saathiya.\nRapped version became internet sensation.\nQuestion about who was in the kitchen.\nYashraj Mukhate's musical creation.",
        "points": 1,
    },
    {
        "name": "Sachin Tendulkar",
        "description": "God of Cricket.\nHighest run scorer in international cricket.\n100 international centuries.\nFamous for his straight drives.\nRetired in 2013 at Wankhede Stadium.",
        "points": 2,
    },
    {
        "name": "Bahubali",
        "description": "Warrior who lifted the shivling.\nSS Rajamouli's epic film series.\nPrabhas played the titular role.\n'Why did Kattappa kill Bahubali?'\nHighest grossing Indian film franchise.",
        "points": 2,
    },
    {
        "name": "Chandrayaan-3",
        "description": "India's successful moon mission.\nLanded on lunar south pole.\nMade India 4th country to land on moon.\nVikram lander and Pragyan rover.\nISRO's proudest achievement in 2023.",
        "points": 3,
    },
    {
        "name": "Rajinikanth",
        "description": "Superstar with legendary stunts.\nTamil cinema's biggest icon.\nFamous for his style and punch dialogues.\nFilms defy gravity and logic.\n'Thalaiva' to millions of fans.",
        "points": 2,
    },
    {
        "name": "MS Dhoni",
        "description": "Cool-headed cricket captain.\nCaptain Cool who won 2011 World Cup.\nFinishing six in World Cup final.\nWicket-keeper batsman from Ranchi.\nRetired from international cricket in 2020.",
        "points": 2,
    },
    {
        "name": "Yogi Adityanath",
        "description": "CM of Uttar Pradesh.\nSaffron-clad leader from Gorakhpur.\nHead priest of Gorakhnath temple.\nKnown for law and order focus.\nReal name is Ajay Singh Bisht.",
        "points": 2,
    },
    {
        "name": "Amitabh Bachchan",
        "description": "Big B of Bollywood.\nHost of Kaun Banega Crorepati.\nAngry young man of the 70s.\nBachchan family patriarch.\nVoice of a generation.",
        "points": 1,
    },
    {
        "name": "Priyanka Chopra",
        "description": "Global icon and former Miss World.\nQuantico star who conquered Hollywood.\nMarried to Nick Jonas.\nFounder of Purple Pebble Pictures.\nUNICEF Goodwill Ambassador.",
        "points": 2,
    },
    {
        "name": "Virat Kohli",
        "description": "King Kohli of modern cricket.\nAggressive batting style and celebrations.\nMarried to Anushka Sharma.\nRoyal Challengers Bangalore captain.\nChase master in cricket.",
        "points": 1,
    },
    {
        "name": "Taj Mahal",
        "description": "Monument of love in Agra.\nBuilt by Shah Jahan for Mumtaz.\nOne of Seven Wonders of World.\nWhite marble mausoleum.\nSymbol of eternal love.",
        "points": 2,
    },
    {
        "name": "Mahatma Gandhi",
        "description": "Father of the Nation.\nLed India's independence movement.\nPhilosophy of non-violence (Ahimsa).\nBorn in Porbandar, Gujarat.\nAssassinated on January 30, 1948.",
        "points": 2,
    },
    {
        "name": "Narendra Modi",
        "description": "Prime Minister of India.\nFrom tea seller to PM.\nGujarat CM for 13 years.\nMann Ki Baat radio program host.\nDigital India campaign leader.",
        "points": 1,
    },
    {
        "name": "APJ Abdul Kalam",
        "description": "Missile Man and People's President.\nScientist who became 11th President.\nWorked on Pokhran nuclear tests.\nInspirational speaker and author.\nDied while delivering a lecture.",
        "points": 2,
    },
    {
        "name": "Holi",
        "description": "Festival of colors.\nCelebrates victory of good over evil.\nHolika dahan the night before.\nPeople throw gulal and colored water.\nMarks the arrival of spring.",
        "points": 1,
    },
    {
        "name": "Biryani",
        "description": "Aromatic rice dish with meat/vegetables.\nHyderabadi and Lucknowi variants famous.\nSaffron gives it golden color.\nCooked in dum style.\nServed with raita and shorba.",
        "points": 2,
    },
    {
        "name": "Kashmir",
        "description": "Paradise on Earth.\nDisputed territory between India-Pakistan.\nFamous for houseboats and shikaras.\nSaffron and apple orchards.\nDal Lake and Gulmarg attractions.",
        "points": 3,
    },
    {
        "name": "Sholay",
        "description": "Cult classic Bollywood film.\nJai-Veeru friendship epic.\nGabbar Singh the iconic villain.\n'Kitne aadmi the?' dialogue.\nAmitabh and Dharmendra starrer.",
        "points": 2,
    },
    {
        "name": "IPL",
        "description": "Indian Premier League cricket.\nT20 tournament with franchise teams.\nCheerleaders and entertainment.\nMakes cricketers millionaires.\nApril-May cricket carnival.",
        "points": 1,
    },
    {
        "name": "Lata Mangeshkar",
        "description": "Nightingale of India.\nPlayback singing legend.\nSang in multiple Indian languages.\nReceived Bharat Ratna.\nVoice of Bollywood for decades.",
        "points": 2,
    },
    {
        "name": "Kumbh Mela",
        "description": "Largest peaceful gathering on Earth.\nHindu pilgrimage festival.\nHeld every 12 years at four locations.\nSadhus take holy dip in rivers.\nUNESCO Intangible Cultural Heritage.",
        "points": 3,
    },
    {
        "name": "Bollywood",
        "description": "Hindi film industry.\nBased in Mumbai.\nLargest film industry by output.\nSong and dance sequences.\nInfluences fashion and culture.",
        "points": 1,
    },
    {
        "name": "Ratan Tata",
        "description": "Business tycoon and philanthropist.\nFormer chairman of Tata Group.\nLaunched Tata Nano car.\nReceived Padma Vibhushan.\nKnown for ethical business practices.",
        "points": 2,
    },
    {
        "name": "Yoga",
        "description": "Ancient Indian practice.\nCombines physical and spiritual elements.\nInternational Yoga Day June 21.\nPatanjali's Yoga Sutras.\nBenefits mind, body and soul.",
        "points": 2,
    },
    {
        "name": "Mangalyaan",
        "description": "Mars Orbiter Mission.\nIndia's first Mars mission.\nSuccess in first attempt.\nCost less than Hollywood movie.\nISRO's cost-effective achievement.",
        "points": 3,
    },
    {
        "name": "Dosa",
        "description": "South Indian crepe delicacy.\nMade from rice and lentil batter.\nServed with sambar and chutney.\nMasala dosa most popular variant.\nCrispy and golden when cooked well.",
        "points": 2,
    },
    {
        "name": "Akshay Kumar",
        "description": "Khiladi of Bollywood.\nCanadian-born Indian actor.\nKnown for action and comedy films.\nEarly morning workout routine.\nPatriotic film specialist.",
        "points": 2,
    },
    {
        "name": "Ganga",
        "description": "Holiest river in Hinduism.\nOriginates from Gangotri glacier.\nFlows through North India.\nWorshipped as goddess.\nLifeline of millions of people.",
        "points": 2,
    },
    {
        "name": "Cricket World Cup 1983",
        "description": "India's first World Cup victory.\nKapil Dev's team defeated West Indies.\nFamous catch by Kapil at Lord's.\nChanged Indian cricket forever.\n83 film made on this victory.",
        "points": 3,
    },
    {
        "name": "Deepika Padukone",
        "description": "Bollywood actress and producer.\nBadminton player turned actor.\nMarried to Ranveer Singh.\nMental health awareness advocate.\nPadmaavat and Piku star.",
        "points": 2,
    },
    {
        "name": "Red Fort",
        "description": "Mughal fortress in Delhi.\nPrime Minister hoists flag here.\nIndependence Day celebrations venue.\nBuilt by Shah Jahan.\nUNESCO World Heritage Site.",
        "points": 2,
    },
    {
        "name": "Harmanpreet Kaur",
        "description": "Indian women's cricket captain.\nPowerful middle-order batter.\nFirst Indian to play in overseas T20 leagues.\nPunjab's pride in cricket.\nWomen's cricket pioneer.",
        "points": 3,
    },
    {
        "name": "Aadhaar",
        "description": "Unique identification system.\n12-digit biometric ID.\nWorld's largest ID program.\nUsed for government services.\nControversial privacy debates.",
        "points": 2,
    },
    {
        "name": "Dangal",
        "description": "Aamir Khan wrestling film.\nBased on Geeta Phogat's story.\nHighest grossing Bollywood film.\nWomen empowerment theme.\n'Haanikaarak Bapu' famous song.",
        "points": 2,
    },
    {
        "name": "Kailash Satyarthi",
        "description": "Nobel Peace Prize winner.\nChild rights activist.\nFought against child labor.\nBachpan Bachao Andolan founder.\nShared Nobel with Malala Yousafzai.",
        "points": 3,
    },
    {
        "name": "Chai",
        "description": "Indian spiced tea.\nMilk tea with cardamom, ginger.\nStreet-side vendors called chaiwalas.\nNational drink of India.\nBest companion for conversations.",
        "points": 1,
    },
    {
        "name": "Punjab",
        "description": "Land of Five Rivers.\nWheat bowl of India.\nSikh majority state.\nGolden Temple in Amritsar.\nBhangra dance originates here.",
        "points": 2,
    },
    {
        "name": "Chhatrapati Shivaji",
        "description": "Maratha warrior king.\nFounded Maratha Empire.\nGuerrilla warfare tactics.\nBuilt strong naval force.\nIconic figure of Hindu resistance.",
        "points": 3,
    },
    {
        "name": "ISRO",
        "description": "Indian Space Research Organisation.\nLaunches satellites cost-effectively.\nDr. Vikram Sarabhai founded it.\nBased in Bengaluru.\nMade India space power.",
        "points": 2,
    },
    {
        "name": "Dilwale Dulhania Le Jayenge",
        "description": "DDLJ - longest running film.\nShah Rukh Khan and Kajol starrer.\nYash Raj Films production.\nEurotrip romance story.\nMaratha Mandir still shows it.",
        "points": 2,
    }
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
