import streamlit as st

def show_sidebar():

    st.sidebar.image(
        "assets/aura_logo.jpeg",
        use_container_width=True
    )

    st.sidebar.markdown("# Agent AURA")

    st.sidebar.caption(
        "AI for Understanding, Relevance & Action"
    )

    st.sidebar.markdown("---")