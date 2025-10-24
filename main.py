import streamlit as st
import pandas as pd
import random

# 페이지 설정
st.set_page_config(page_title="신비한 소라의 대답 🐚", page_icon="🐚", layout="centered")

# 스타일 (글꼴, 색상, 애니메이션 효과)
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #00111a 0%, #002b36 100%);
        color: #e0f7fa;
        font-family: 'Nanum Gothic', sans-serif;
    }
    .title {
        font-size: 2.2em;
        text-align: center;
        color: #b3e5fc;
        text-shadow: 0px 0px 15px #80deea;
    }
    .question-box {
        text-align: center;
        font-size: 1.2em;
        color: #e0f7fa;
    }
    .magic-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 250px;
        cursor: pointer;
        transition: transform 0.2s;
    }
    .magic-image:hover {
        transform: scale(1.1);
        filter: drop-shadow(0px 0px 10px #80deea);
    }
    .answer-box {
        margin-top: 25px;
        text-align: center;
        font-size: 1.4em;
        color: #b2ebf2;
        text-shadow: 0px 0px 12px #4dd0e1;
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

# 엑셀 파일에서 답변 로드
try:
    df = pd.read_excel('sora.xlsx')
    answers = df.iloc[:, 0].dropna().tolist()  # 첫 번째 열의 값만 사용
except Exception as e:
    st.error("⚠️ 'sora.xlsx' 파일을 불러오지 못했습니다. 파일이 같은 폴더에 있는지 확인하세요.")
    st.stop()

# 이미지 클릭 시 동작
if st.button("🐚 소라에게 물어보기"):
    if user_question.strip() == "":
        st.warning("먼저 질문을 입력해 주세요 🌸")
    else:
        answer = random.choice(answers)
        st.markdown(
            f"<div class='answer-box'>🌊 신비한 소라의 대답 🌊<br><br><b>{answer}</b></div>",
            unsafe_allow_html=True
        )

# 이미지 (클릭 유도)
st.markdown(
    f"""
    <div style="text-align:center;">
        <img src="https://ramiteacher.github.io/conch/sora.png" class="magic-image" alt="신비한 소라" />
    </div>
    """,
    unsafe_allow_html=True
)
