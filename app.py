import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Love Diana",page_icon=":kissing_heart:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


# ----- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jvxwtdtp.json")

# ---- HEADER SECTION ----
st.subheader("I am your labidabdab forever")
st.title("I LOVE YOU!!!" ":kissing_heart:")
st.write("I will always be yours forever and ever")

st_lottie(lottie_coding, height=300,key="coding")
