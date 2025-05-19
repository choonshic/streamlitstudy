import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib  # 한글 깨짐 방지용 패키지

# GitHub에서 raw CSV 불러오기
DATA_URL = "https://raw.githubusercontent.com/choonshic/streamlitstudy/main/seoul.csv"

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(DATA_URL)
    except UnicodeDecodeError:
        df = pd.read_csv(DATA_URL, encoding='ISO-8859-1')

    # 실제 데이터 컬럼명에 맞게 설정
    df.columns = ['년', '지점', '평균기온(℃)', '평균최저기온(℃)', '평균최고기온(℃)']

    # 타입 변환
    df['년'] = pd.to_numeric(df['년'], errors='coerce').astype(int)
    df['평균기온'] = pd.to_numeric(df['평균기온(℃)'], errors='coerce')
    df['평균최저기온'] = pd.to_numeric(df['평균최저기온(℃)'], errors='coerce')
    df['평균최고기온'] = pd.to_numeric(df['평균최고기온(℃)'], errors='coerce')
    df['일교차'] = df['평균최고기온'] - df['평균최저기온']

    df.rename(columns={'년': '연도'}, inplace=True)
    df['월'] = 1  # 히트맵용 임시 월 정보

    return df

df = load_data()

st.title("서울 기온 데이터 시각화 및 그래프 투표")

# 주제 선택
topic = st.selectbox("분석할 항목을 선택하세요:", ['평균최고기온', '평균최저기온', '일교차'])

st.header(f"\U0001F4CA {topic} 시각화 예시")

# 1. 선 그래프
st.subheader("1. 선 그래프")
fig1, ax1 = plt.subplots(figsize=(14, 6))
df_line = df.groupby('연도')[topic].mean().dropna()
ax1.plot(df_line.index.astype(int), df_line.values, marker='o')
ax1.set_xlim(1955, 2024)
ax1.set_xticks(range(1955, 2025, 5))
ax1.set_xlabel('연도')
ax1.set_ylabel(topic)
ax1.tick_params(axis='x', labelrotation=45)
st.pyplot(fig1)

# 2. 막대 그래프
st.subheader("2. 막대 그래프")
fig2, ax2 = plt.subplots(figsize=(14, 6))
df_bar = df.groupby('연도')[topic].mean().dropna()
ax2.bar(df_bar.index.astype(int), df_bar.values)
ax2.set_xlim(1955, 2024)
ax2.set_xticks(range(1955, 2025, 5))
ax2.set_xlabel('연도')
ax2.set_ylabel(topic)
ax2.tick_params(axis='x', labelrotation=45)
st.pyplot(fig2)

# 3. 박스플롯 (의미 없음으로 대체 텍스트 출력)
st.subheader("3. 박스플롯")
st.info("해당 데이터는 연도별 평균값만 포함하고 있어 월별 박스플롯은 의미가 없습니다.")

# 4. 히트맵
st.subheader("4. 히트맵")
fig4, ax4 = plt.subplots(figsize=(14, 6))
pivot = df.pivot_table(index='월', columns='연도', values=topic, aggfunc='mean')
if pivot.isnull().values.all():
    st.warning("히트맵을 생성할 수 없습니다. 선택한 항목에 유효한 데이터가 없습니다.")
else:
    sns.heatmap(pivot, ax=ax4, cmap="YlOrRd")
    ax4.set_xlabel('연도')
    ax4.set_ylabel('월')
    ax4.tick_params(axis='x', labelrotation=45)
    st.pyplot(fig4)

# 투표 기능
st.markdown("## ✅ 가장 효과적인 그래프는?")
vote = st.radio("가장 잘 표현된 그래프를 선택해주세요:", ['1. 선 그래프', '2. 막대 그래프', '4. 히트맵'])

if 'vote_count' not in st.session_state:
    st.session_state.vote_count = {'1': 0, '2': 0, '4': 0}

if st.button("투표하기"):
    st.session_state.vote_count[vote[0]] += 1
    st.success(f"'{vote}'에 투표해주셔서 감사합니다!")

with st.expander("📊 현재 투표 현황 보기"):
    for k, v in st.session_state.vote_count.items():
        st.write(f"{k}번 그래프: {v}표")
