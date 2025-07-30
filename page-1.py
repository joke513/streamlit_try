import streamlit as st
import pandas as pd
st.title("我的个人网页🏐")

st.write("## hello welcome!")

df = pd.DataFrame({
    "学号" : [ '01','02','03','04'],
    "班级" : [ '一班','一班','一班','一班'],
    "成绩" : [ 9,39,999,99]
})
st.dataframe(df)
st.divider()
st.table(df)

