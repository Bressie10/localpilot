import streamlit as st
from command import commandCallingWeb

st.set_page_config(
    page_title="LocalPilot"
)

st.title("LocalPilot")
st.write("A simple computer assistant(That needs a lot of improvement....)")

user_command = st.text_input(
    "Enter a command (50/50 if it works :))",
    placeholder="Use help so see alll commands"
)

if st.button("Run"):
    output = commandCallingWeb(user_command)
    st.code(str(output), language=None)