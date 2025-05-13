import streamlit as st
import random

# 16가지 MBTI 유형과 추천 직업
mbti_jobs = {
    # 분석가형 (Analysts)
    "INTJ": ["🔬 과학자", "💻 데이터 사이언티스트", "📈 전략 컨설턴트", "🧠 AI 연구원"],
    "INTP": ["🧪 연구원", "🔧 시스템 개발자", "📚 철학자", "📐 이론 물리학자"],
    "ENTJ": ["👔 CEO", "📊 경영 컨설턴트", "🧭 기획 관리자", "🏢 조직 리더"],
    "ENTP": ["📢 마케터", "📺 방송기획자", "💡 창업가", "🎤 MC"],

    # 외교관형 (Diplomats)
    "INFJ": ["🧘 심리치료사", "📚 작가", "🕊️ NGO 활동가", "💒 종교인"],
    "INFP": ["🎨 일러스트레이터", "📚 소설가", "💖 상담사", "🌿 환경운동가"],
    "ENFJ": ["👩‍🏫 교사", "🗣️ 커뮤니케이션 전문가", "🎙️ 강연가", "💞 멘토"],
    "ENFP": ["📝 콘텐츠 크리에이터", "🎥 영상 디렉터", "🌍 여행 가이드", "🎉 이벤트 플래너"],

    # 관리자형 (Sentinels)
    "ISTJ": ["🧮 회계사", "🏛️ 공무원", "🔍 감사관", "⚖️ 법무사"],
    "ISFJ": ["👩‍⚕️ 간호사", "👨‍👩‍👧‍👦 사회복지사", "🎀 아동심리상담사", "🍰 제과제빵사"],
    "ESTJ": ["🏢 관리자", "👨‍💼 팀 리더", "💼 재무 담당자", "📦 물류 관리자"],
    "ESFJ": ["👩‍🏫 교사", "👩‍🍳 식음료 전문가", "🧴 고객 서비스", "👨‍⚕️ 의료 행정"] ,

    # 탐험가형 (Explorers)
    "ISTP": ["🔧 기계공", "🚙 자동차 정비사", "🛠️ 기술자", "🕹️ 게임 개발자"],
    "ISFP": ["🎨 디자이너", "🎵 뮤지션", "📷 포토그래퍼", "🌺 플로리스트"],
    "ESTP": ["🚓 경찰", "🏎️ 레이서", "💼 영업사원", "🎯 사업가"],
    "ESFP": ["🎤 연예인", "🎭 배우", "🎨 인플루언서", "🎉 이벤트 코디네이터"]
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
