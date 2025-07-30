import streamlit as st
#选项卡组件
tab1, tab2,tab3 = st.tabs(["性别","联系方式","水果"])
with tab1:

    gender = st.radio("选择你的性别",
             ['男','女'],
             index=None

             )
with tab2:


    contact = st.selectbox("你希望通过什么方式联系",
                 ['电话','微信','邮箱'],
                 index=None
    )
with tab3:
    fruits = st.multiselect("你喜欢什么水果",
                            ["苹果","香蕉","水蜜桃","哈密瓜"]
                            )
st.divider()

#折叠选项卡
with st.expander("身高"):

    high = st.slider("你的身高",value = 170, min_value=100, max_value=230, step = 1)
    f"你的身高是{high}厘米\n"

st.divider()

file = st.file_uploader("请上传文件",type=['py'])
if file:
    st.write(f"你上传的文件名是{file.name}")
