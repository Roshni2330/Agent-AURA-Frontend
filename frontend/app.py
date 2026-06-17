import streamlit as st

from components.sidebar import show_sidebar
from utils.styles import load_css

st.set_page_config(
    page_title="Agent AURA",
    page_icon="🤖",
    layout="wide"
)

show_sidebar()
load_css()

# Session State
if "campaigns" not in st.session_state:
    st.session_state.campaigns = []

if "history" not in st.session_state:
    st.session_state.history = []

feedback_count = 0

if "feedback" in st.session_state:
    if st.session_state.feedback:
        feedback_count = 1

# Logo
st.image(
    "assets/aura_logo.jpeg",
    width=250
)

# Title
st.markdown(
    """
    <h1 style='font-size:60px;margin-bottom:0px;'>
    Agent AURA
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='color:gray;margin-top:0px;'>
    AI-Powered Content Generation Assistant
    </h4>
    """,
    unsafe_allow_html=True
)

st.write("")

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class='card'>
            <h3>📁 Campaigns</h3>
            <h1>{len(st.session_state.campaigns)}</h1>
            <p>Total Campaigns</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class='card'>
            <h3>📝 Generations</h3>
            <h1>{len(st.session_state.history)}</h1>
            <p>Total Generations</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class='card'>
            <h3>💬 Feedback</h3>
            <h1>{feedback_count}</h1>
            <p>Total Feedback</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.write("")

left, right = st.columns(2)

with left:

    st.markdown(
        """
        <div class='box'>
        <h2>Quick Navigation</h2>

        • Generate Content<br><br>

        • View History<br><br>

        • Manage Campaigns<br><br>

        • Review Revisions
        </div>
        """,
        unsafe_allow_html=True
    )

with right:

    st.markdown(
        """
        <div class='box'>
        <h2>Current Status</h2>

        ✅ Frontend Running<br><br>

        ✅ Session Storage Active<br><br>

        ✅ Logging Active<br><br>

        🚀 Ready For Backend Integration
        </div>
        """,
        unsafe_allow_html=True
    )