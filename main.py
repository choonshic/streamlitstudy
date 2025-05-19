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
    df['월'] = 1  # 임시 월 정보 (히트맵 제거됨)

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

# 3. 원 그래프 (최근 10년 비중)
st.subheader("3. 원 그래프")
fig3, ax3 = plt.subplots(figsize=(8, 8))
latest_years = df[df['연도'] >= 2015]
pie_data = latest_years.groupby('연도')[topic].mean().dropna()
ax3.pie(pie_data, labels=pie_data.index.astype(str), autopct='%1.1f%%', startangle=90)
ax3.set_title("최근 10년간 연도별 비중")
st.pyplot(fig3)

# 4. 산점도
st.subheader("4. 산점도")
fig4, ax4 = plt.subplots(figsize=(14, 6))
ax4.scatter(df['연도'], df[topic])
ax4.set_xlabel('연도')
ax4.set_ylabel(topic)
ax4.set_title(f"연도별 {topic} 산점도")
ax4.tick_params
