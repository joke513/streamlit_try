import streamlit as st
import pandas as pd

"## hello"
name = st.text_input("请输入你的名字：")
if name:
    st.write(f"hello,{name}")

st.divider()

password = st.text_input("请输入你的密码",type='password')
st.divider()

age = st.number_input("请输入你的年龄", max_value = 150, min_value = 0, step = 1 )

st.divider()
checked = st.checkbox("我同意以上条款")
if checked:
    "感谢"

st.divider()

submitted = st.button("提交")
if( submitted ):
    "提交成功"