
import streamlit as st
import random

# 16가지 MBTI 유형과 추천 직업 및 설명
mbti_jobs = {
    # 분석가형
    "INTJ": [
        ("🔬 과학자", "논리적 사고와 독립성을 살려 연구에 집중하는 직업입니다."),
        ("💻 데이터 사이언티스트", "데이터를 분석하고 의미를 도출하는 전문가입니다."),
        ("📈 전략 컨설턴트", "기업 전략을 분석하고 방향을 제시합니다."),
        ("🧠 AI 연구원", "인공지능 알고리즘을 연구하고 개발하는 역할입니다.")
    ],
    "INTP": [
        ("🧪 연구원", "이론과 실험을 바탕으로 새로운 지식을 창출합니다."),
        ("🧬 생명과학자", "생명 현상에 대해 탐구하고 연구합니다."),
        ("📐 이론물리학자", "우주의 근본 원리를 수학으로 탐구하는 직업입니다."),
        ("🔧 소프트웨어 엔지니어", "창의적인 문제 해결로 프로그램을 설계합니다.")
    ],
    "ENTJ": [
        ("👔 CEO", "조직을 이끄는 리더십과 결단력을 가진 직업입니다."),
        ("📊 경영 컨설턴트", "기업의 전략을 분석하고 조언합니다."),
        ("🧭 프로젝트 매니저", "목표를 향해 팀을 이끄는 중추적인 역할입니다."),
        ("💼 기획자", "사업 아이디어를 구체화하고 실행 계획을 세웁니다.")
    ],
    "ENTP": [
        ("📢 마케터", "사람들의 관심을 이끌 아이디어를 설계합니다."),
        ("📺 방송기획자", "흥미롭고 창의적인 콘텐츠를 기획합니다."),
        ("💡 창업가", "새로운 아이디어를 사업으로 구현합니다."),
        ("🎤 MC", "사람들과 소통하며 분위기를 이끄는 역할입니다.")
    ],

    # 외교관형
    "INFJ": [
        ("🧘 심리치료사", "마음의 아픔을 돌보는 조력자입니다."),
        ("📚 작가", "깊은 통찰과 감성으로 이야기를 전합니다."),
        ("🕊️ NGO 활동가", "사회적 정의와 평화를 위해 일합니다."),
        ("💒 종교인", "영적인 가르침과 상담을 제공하는 역할입니다.")
    ],
    "INFP": [
        ("🎨 일러스트레이터", "감성을 담아 그림을 그리는 예술가입니다."),
        ("📚 소설가", "이야기를 창조하며 독자의 마음을 움직입니다."),
        ("💖 상담사", "사람들의 마음을 이해하고 도와주는 역할입니다."),
        ("🌿 환경운동가", "지구와 자연을 보호하기 위해 활동합니다.")
    ],
    "ENFJ": [
        ("👩‍🏫 교사", "학생들을 이끌고 가르치는 따뜻한 리더입니다."),
        ("🗣️ 커뮤니케이션 전문가", "사람들과 효과적으로 소통하는 역할입니다."),
        ("🎙️ 강연가", "사람들에게 영감을 주는 메시지를 전달합니다."),
        ("💞 멘토", "타인의 성장을 도와주는 조언자입니다.")
    ],
    "ENFP": [
        ("📝 콘텐츠 크리에이터", "창의적인 아이디어로 콘텐츠를 만듭니다."),
        ("🎥 영상 디렉터", "감성을 담아 스토리를 영상으로 풀어냅니다."),
        ("🌍 여행 가이드", "세계를 누비며 사람들과 즐거움을 나눕니다."),
        ("🎉 이벤트 플래너", "행사를 기획하고 실행하는 창의적 직업입니다.")
    ],

    # 관리자형
    "ISTJ": [
        ("🧮 회계사", "정확함과 책임감을 기반으로 재무를 관리합니다."),
        ("🏛️ 공무원", "공공의 이익을 위해 봉사하는 안정적인 직업입니다."),
        ("🔍 감사관", "규칙과 절차를 점검하고 평가합니다."),
        ("⚖️ 법무사", "법률 문서와 관련된 전문적인 업무를 수행합니다.")
    ],
    "ISFJ": [
        ("👩‍⚕️ 간호사", "환자에게 따뜻한 돌봄을 제공합니다."),
        ("👨‍👩‍👧‍👦 사회복지사", "사회적 약자를 돕는 따뜻한 직업입니다."),
        ("🎀 아동심리상담사", "어린이들의 마음을 보듬고 성장시키는 직업입니다."),
        ("🍰 제과제빵사", "달콤한 빵과 케이크로 사람들의 미소를 만듭니다.")
    ],
    "ESTJ": [
        ("🏢 관리자", "조직을 효율적으로 운영하는 역할입니다."),
        ("👨‍💼 팀 리더", "팀의 목표를 달성하도록 이끄는 관리자입니다."),
        ("💼 재무 담당자", "회사의 자산과 지출을 관리합니다."),
        ("📦 물류 관리자", "제품의 유통과 공급을 책임지는 직업입니다.")
    ],
    "ESFJ": [
        ("👩‍🏫 교사", "학생을 사랑하고 이끄는 교육자입니다."),
        ("👩‍🍳 식음료 전문가", "사람들의 입맛을 사로잡는 전문가입니다."),
        ("🧴 고객 서비스", "고객과의 소통을 책임지는 직업입니다."),
        ("👨‍⚕️ 의료 행정", "병원에서 행정과 운영을 관리합니다.")
    ],

    # 탐험가형
    "ISTP": [
        ("🔧 기계공", "기계를 다루고 수리하는 기술직입니다."),
        ("🚙 자동차 정비사", "자동차를 진단하고 고치는 전문가입니다."),
        ("🛠️ 기술자", "다양한 도구와 장비를 다루는 현장 전문가입니다."),
        ("🕹️ 게임 개발자", "게임을 설계하고 프로그래밍하는 창의직입니다.")
    ],
    "ISFP": [
        ("🎨 디자이너", "시각적으로 아름다움을 창조하는 직업입니다."),
        ("🎵 뮤지션", "음악으로 감정을 표현하는 예술가입니다."),
        ("📷 포토그래퍼", "순간을 예술로 남기는 전문가입니다."),
        ("🌺 플로리스트", "꽃을 활용해 아름다움을 창조합니다.")
    ],
    "ESTP": [
        ("🚓 경찰", "현장에서 시민의 안전을 지키는 역할입니다."),
        ("🏎️ 레이서", "스피드와 기술을 겨루는 스포츠 전문가입니다."),
        ("💼 영업사원", "고객과의 관계를 통해 제품을 소개합니다."),
        ("🎯 사업가", "비즈니스 기회를 찾아 성공을 이루는 사람입니다.")
    ],
    "ESFP": [
        ("🎤 연예인", "무대 위에서 대중을 즐겁게 하는 예술가입니다."),
        ("🎭 배우", "다양한 인물을 연기하며 감정을 표현합니다."),
        ("🎨 인플루언서", "개성을 콘텐츠로 표현하는 SNS 스타입니다."),
        ("🎉 이벤트 코디네이터", "행사와 파티를 기획하고 운영합니다.")
    ]
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
