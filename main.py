import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------
# 데이터 로딩
# -----------------------
@st.cache_data
def load_data():
    df = pd.read_csv('seoul_temp.csv', parse_dates=['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['일교차'] = df['최고기온'] - df['최저기온']
    return df

df = load_data()

# -----------------------
# 주제 선택
# -----------------------
topic = st.selectbox("분석 주제를 선택하세요", ['최고기온', '최저기온', '일교차'])

# -----------------------
# 그래프 생성 함수
# -----------------------
def plot_graphs(df, topic):
    st.subheader(f"📊 {topic} 시각화 예시")

    # 1. 선 그래프
    st.markdown("### ① 선 그래프")
    fig1, ax1 = plt.subplots()
    df.groupby('year')[topic].mean().plot(ax=ax1)
    st.pyplot(fig1)

    # 2. 막대 그래프
    st.markdown("### ② 막대 그래프")
    fig2, ax2 = plt.subplots()
    df.groupby('year')[topic].mean().plot(kind='bar', ax=ax2)
    st.pyplot(fig2)

    # 3. 박스플롯
    st.markdown("### ③ 박스플롯")
    fig3, ax3 = plt.subplots()
    sns.boxplot(x='month', y=topic, data=df, ax=ax3)
    st.pyplot(fig3)

    # 4. 히트맵
    st.markdown("### ④ 히트맵 (월-연 평균)")
    fig4, ax4 = plt.subplots()
    pivot = df.pivot_table(index='month', columns='year', values=topic)
    sns.heatmap(pivot, ax=ax4)
    st.pyplot(fig4)

# -----------------------
# 그래프 표시
# -----------------------
plot_graphs(df, topic)

# -----------------------
# 투표 기능
# -----------------------
st.markdown("## ✅ 어떤 그래프가 가장 잘 표현되었나요?")
vote = st.radio("그래프 번호를 선택해주세요", ['① 선 그래프', '② 막대 그래프', '③ 박스플롯', '④ 히트맵'])

# 간단한 상태 기반 집계 (개발용: 실제 배포시 DB 또는 파일 연동 필요)
if 'vote_count' not in st.session_state:
    st.session_state.vote_count = {'①': 0, '②': 0, '③': 0, '④': 0}

if st.button("투표하기"):
    key = vote.split(' ')[0]
    st.session_state.vote_count[key] += 1
    st.success(f"'{vote}'에 투표해주셔서 감사합니다!")

# -----------------------
# 투표 결과 보기
# -----------------------
with st.expander("📊 현재 투표 현황 보기"):
    for k, v in st.session_state.vote_count.items():
        st.write(f"{k} 그래프: {v}표")

