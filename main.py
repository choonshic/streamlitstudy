import streamlit as st
import random

# MBTI별 추천 직업 데이터 (좀 더 다양하고 풍부하게 구성)
mbti_jobs = {
    "INTJ": ["🔬 과학자", "💻 데이터 사이언티스트", "📈 전략 컨설턴트", "🧠 AI 연구원"],
    "INFP": ["🎨 일러스트레이터", "📚 소설가", "💖 심리상담사", "🌿 환경운동가"],
    "ENTP": ["📢 마케터", "📺 방송기획자", "💡 스타트업 창업가", "🎤 MC"],
    "ESFP": ["🎤 가수", "🎭 배우", "🎨 인플루언서", "🎉 이벤트 플래너"],
    "ISTJ": ["🧮 회계사", "🏛️ 공무원", "🔍 감사관", "⚖️ 법무사"],
    "ENFP": ["🧑‍🏫 교사", "📝 콘텐츠 크리에이터", "🎥 영상 디렉터", "🌍 여행 가이드"],
    "ISFJ": ["👩‍⚕️ 간호사", "👨‍👩‍👧‍👦 사회복지사", "🎀 아동심리상담사", "🍰 제과제빵사"],
    "ESTP": ["🚗 레이서", "🛠️ 기술자", "🕵️ 경찰", "🚒 소방관"]
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
selected_mbti = st.selectbox("🔍 MBTI 유형 선택하기", list(mbti_jobs.keys()))

# 추천 결과 보여주기
if selected_mbti:
    st.subheader(f"✨ {selected_mbti} 유형에게 어울리는 직업들 ✨")
    selected_jobs = random.sample(mbti_jobs[selected_mbti], k=min(3, len(mbti_jobs[selected_mbti])))
    for job in selected_jobs:
        st.markdown(f"- {job}")

    st.success("🌈 당신에게 맞는 직업을 향해 한 걸음 더 가까워졌어요!")

# 귀여운 하단 이미지나 메시지
st.markdown("""
---
🎓 **주의사항**: 이 앱은 재미와 참고용입니다. 실제 진로는 다양한 경험과 상담을 통해 결정하는 것이 좋아요!

🧸 귀엽고 알찬 진로 탐색 앱, 마음에 드셨나요? 감사합니다 💕

Made with 💖 by ChatGPT
""")
