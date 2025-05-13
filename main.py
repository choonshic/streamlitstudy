import streamlit as st
import random

# 16가지 MBTI 유형과 추천 직업 및 설명
mbti_jobs = {
    "INTJ": [
        ("🔬 과학자", "논리적 사고와 독립성을 살려 연구에 집중하는 직업입니다."),
        ("💻 데이터 사이언티스트", "데이터를 분석하고 의미를 도출하는 전문가입니다."),
        ("📈 전략 컨설턴트", "기업 전략을 분석하고 방향을 제시합니다."),
        ("🧠 AI 연구원", "인공지능 알고리즘을 연구하고 개발하는 역할입니다.")
    ],
    "INFP": [
        ("🎨 일러스트레이터", "감성을 담아 그림을 그리는 예술가입니다."),
        ("📚 소설가", "이야기를 창조하며 독자의 마음을 움직입니다."),
        ("💖 상담사", "사람들의 마음을 이해하고 도와주는 역할입니다."),
        ("🌿 환경운동가", "지구와 자연을 보호하기 위해 활동합니다.")
    ],
    # 생략된 유형은 동일한 형식으로 추가 가능
    # 아래는 예시로 한두 개 유형만 포함하였습니다.
}

# Streamlit 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천기 💼✨", page_icon="🌈", layout="centered")

# 페이지 상단 타이틀
st.title("🌟 MBTI로 알아보는 나의 미래 직업! ✨")

# 귀여운 설명 문구
st.markdown("""
안녕하세요! 🐣

당신의 성격 유형(MBTI)을 기반으로 어울릴 수 있는 직업을 추천해드려요.

자, 시작해볼까요? MBTI 유형을 선택해주세요! 💌
""")

# 사용자 입력 받기
selected_mbti = st.selectbox("🔍 MBTI 유형 선택하기", sorted(mbti_jobs.keys()))

# 추천 결과 보여주기
if selected_mbti:
    st.subheader(f"✨ {selected_mbti} 유형에게 어울리는 직업들 ✨")
    selected_jobs = random.sample(mbti_jobs[selected_mbti], k=4)

    for title, description in selected_jobs:
        with st.expander(title):
            st.markdown(f"💡 {description}")
            st.balloons()

    st.success("🌈 당신에게 맞는 직업을 향해 한 걸음 더 가까워졌어요!")

# 귀여운 하단 이미지나 메시지
st.markdown("""
---
🎓 **주의사항**: 이 앱은 재미와 참고용입니다. 실제 진로는 다양한 경험과 상담을 통해 결정하는 것이 좋아요!

🧸 귀엽고 알찬 진로 탐색 앱, 마음에 드셨나요? 감사합니다 💕

Made with 💖 by ChatGPT
""")
