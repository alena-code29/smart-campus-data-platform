from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
GOLD_FILE = PROJECT_ROOT / 'data' / 'lake' / 'gold' / 'learning_analytics' / 'student_risk_features.csv'

st.set_page_config(page_title='Smart Campus Analytics', layout='wide')
st.title('Smart Campus Learning Analytics')
st.caption('Embedded Analytics интерфейс для анализа учебной активности и риска студентов')

if not GOLD_FILE.exists():
    st.warning('Gold table not found. Run pipelines/load_raw_to_bronze.py, bronze_to_silver.py and silver_to_gold.py first.')
    st.stop()

df = pd.read_csv(GOLD_FILE)

faculty_options = ['Все факультеты'] + sorted(df['faculty'].unique().tolist())
faculty = st.sidebar.selectbox('Факультет', faculty_options)

filtered = df.copy()
if faculty != 'Все факультеты':
    filtered = filtered[filtered['faculty'] == faculty]

group_options = ['Все группы'] + sorted(filtered['group_id'].unique().tolist())
group_id = st.sidebar.selectbox('Группа', group_options)
if group_id != 'Все группы':
    filtered = filtered[filtered['group_id'] == group_id]

col1, col2, col3, col4 = st.columns(4)
col1.metric('Студентов', len(filtered))
col2.metric('Средний балл', round(filtered['avg_grade'].mean(), 2) if len(filtered) else 0)
col3.metric('Средняя посещаемость', round(filtered['attendance_rate'].mean(), 2) if len(filtered) else 0)
col4.metric('High risk', int((filtered['risk_level'] == 'high').sum()))

st.subheader('Средний балл по факультетам')
fig_grade = px.bar(df.groupby('faculty', as_index=False)['avg_grade'].mean(), x='faculty', y='avg_grade')
st.plotly_chart(fig_grade, use_container_width=True)

st.subheader('Распределение риска по группам')
risk_by_group = df.groupby(['group_id', 'risk_level']).size().reset_index(name='students')
fig_risk = px.bar(risk_by_group, x='group_id', y='students', color='risk_level', barmode='group')
st.plotly_chart(fig_risk, use_container_width=True)

st.subheader('Drill-down таблица студентов')
st.dataframe(filtered, use_container_width=True)
