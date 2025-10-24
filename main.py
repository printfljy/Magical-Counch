import streamlit as st
import pandas as pd
import random
import base64
import requests

# 페이지 기본 설정
st.set_page_config(page_title="신비한 소라의 대답 🐚", page_icon="🐚", layout="centered")

# CSS 스타일 (검은 배경 + 반투명 답변 박스 + 애니메이션 효과)
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Nanum Gothic', sans-serif;
    }
    .title {
        font-size: 2.2em;
        text-align: center;
        color: #b3e5fc;
        text-shadow: 0px 0px 15px #80deea;
        margin-top: 20px;
    }
    .question-box {
        text-align: center;
        font-size: 1.2em;
        color: #e0f7fa;
        margin-bottom: 10px;
    }
    .magic-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 250px;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    .magic-image:hover {
        transform: scale(1.1);
        filter: drop-shadow(0px 0px 10px #80deea);
    }
    .answer-box {
        margin-top: 25px;
        text-align: center;
        font-size: 1.4em;
        color: #000000;
        background-color: rgba(255, 255, 255, 0.5);
        border-radius: 15px;
        padding: 20px;
        width: 80%;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0px 0px 15px rgba(255,255,255,0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 제목
st.markdown("<div class='title'>🔮 신비한 소라의 대답 🐚</div>", unsafe_allow_html=True)
st.markdown("<div class='question-box'>마음 속으로 생각한 질문을 말해 보세요... 🌙</div>", unsafe_allow_html=True)

# 사용자 질문 입력
user_question = st.text_input("✨ 당신의 질문을 입력하세요", placeholder="예: 내일은 좋은 일이 생길까?")

# 엑셀 파일에서 답변 불러오기
try:
    df = pd.read_excel('sora.xlsx')
    answers = df.iloc[:, 0].dropna().tolist()
except Exception as e:
    st.error("⚠️ 'sora.xlsx' 파일을 불러오지 못했습니다. 파일이 같은 폴더에 있는지 확인하세요.")
    st.stop()

# 이미지 로드 (base64 인코딩으로 클릭 이벤트 구현)
img_url = "https://ramiteacher.github.io/conch/sora.png"
response = requests.get(img_url)
img_bytes = base64.b64encode(response.content).decode()

# 이미지 클릭 처리 (st.image 자체로는 on_click 지원 안 함 → HTML image map 활용)
st.markdown(
    f"""
    <div style="text-align:center;">
        <form action="?clicked=true" method="get">
            <input type="image" src="data:image/png;base64,{img_bytes}" class="magic-image" alt="신비한 소라" />
        </form>
    </div>
    """,
    unsafe_allow_html=True
)

# 클릭 감지
clicked = st.query_params.get("clicked", ["false"])[0] == "true"

# 클릭 시 답변 출력
if clicked:
    if user_question.strip() == "":
        st.warning("먼저 질문을 입력해 주세요 🌸")
    else:
        answer = random.choice(answers)
        st.markdown(
            f"<div class='answer-box'>🌊 신비한 소라의 대답 🌊<br><br><b>{answer}</b></div>",
            unsafe_allow_html=True
        )
