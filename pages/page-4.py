import streamlit as st
import pandas as pd

"## hello"
# 侧边栏
with st.sidebar:

    name = st.text_input("请输入你的id：")
    if name:
        st.write(f"hello,{name}")

st.divider()

column1, column2, column3 = st.columns([1,1,3])
with column1:

    password = st.text_input("请输入你的密码",type='password')

with column2:
    age = st.number_input("请输入你的年龄", max_value = 150, min_value = 0, step = 1 )

with column3:
    paragragh = st.text_area("请输入你的自我介绍")
st.divider()

checked = st.checkbox("我同意以上条款")
if checked:
    "感谢"

st.divider()

submitted = st.button("提交")
if( submitted ):
    "提交成功"