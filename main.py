import streamlit as st
import pandas as pd
import random
from st_click_detector import click_detector

st.set_page_config(
    page_title="신비한 소라의 대답",
    page_icon="🐚",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #0077b6 0%, #00b4d8 50%, #90e0ef 100%);
    color: white;
}

h1, h2, h3, p, label, div {
    color: white !important;
}

[data-testid="stTextInput"] label {
    color: white !important;
    font-weight: bold;
}

.stTextInput input {
    background-color: rgba(255, 255, 255, 0.95);
    color: black !important;
    border-radius: 12px;
}

.title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    margin-top: 30px;
}

.subtitle {
    text-align: center;
    font-size: 1.2rem;
    margin-bottom: 25px;
}

.answer-box {
    margin-top: 25px;
    padding: 24px;
    border-radius: 20px;
    background-color: rgba(0, 48, 73, 0.65);
    text-align: center;
    box-shadow: 0 6px 20px rgba(0,0,0,0.25);
}

.answer-title {
    font-size: 1.4rem;
    font-weight: bold;
    margin-bottom: 10px;
}

.answer-text {
    font-size: 1.8rem;
    font-weight: bold;
}

.warning-box {
    margin-top: 20px;
    padding: 16px;
    border-radius: 16px;
    background-color: rgba(255, 255, 255, 0.25);
    text-align: center;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🐚 신비한 소라의 대답</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>마음속으로 생각한 질문을 말해 보세요...</div>", unsafe_allow_html=True)

user_question = st.text_input(
    "✨ 당신의 질문을 입력하세요",
    placeholder="예: 내일은 좋은 일이 생길까?",
    key="user_question"
)

try:
    df = pd.read_excel("sora.xlsx")
    answers = df.iloc[:, 0].dropna().tolist()
except Exception:
    st.error("⚠️ 'sora.xlsx' 파일을 불러오지 못했습니다. 파일이 같은 폴더에 있는지 확인하세요.")
    st.stop()

if "last_answer" not in st.session_state:
    st.session_state.last_answer = None

img_url = "https://ramiteacher.github.io/conch/sora.png"

html = f"""
<div style="text-align:center;">
    <a href="#" id="sora_click">
        <img src="{img_url}"
             style="width:280px; max-width:90%; cursor:pointer; border-radius:20px;">
    </a>
    <p style="font-size:0.95rem; margin-top:8px;">👆 소라 사진을 눌러 답변을 들어보세요!</p>
</div>
"""

clicked = click_detector(html, key="sora_image_click")

if clicked == "sora_click":
    if st.session_state.user_question.strip() == "":
        st.session_state.last_answer = None
        st.markdown(
            "<div class='warning-box'>먼저 질문을 입력해 주세요 😊</div>",
            unsafe_allow_html=True
        )
    else:
        st.session_state.last_answer = random.choice(answers)

if st.session_state.last_answer:
    st.markdown(
        f"""
        <div class="answer-box">
            <div class="answer-title">🌊 신비한 소라의 대답</div>
            <div class="answer-text">{st.session_state.last_answer}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
