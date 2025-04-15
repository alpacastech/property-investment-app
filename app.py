import streamlit as st
import pandas as pd
import numpy as np

st.title("房地產投資報酬試算")
st.write("請輸入您的投資數據以進行試算。")

price = st.number_input("房產價格", min_value=0)
rent = st.number_input("每月租金收入", min_value=0)
expenses = st.number_input("每月支出", min_value=0)

if st.button("計算投資報酬率"):
    roi = ((rent - expenses) * 12) / price * 100
    st.write(f"您的投資報酬率為：{roi:.2f}%")
