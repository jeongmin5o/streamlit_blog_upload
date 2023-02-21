import streamlit as st 
import pandas as pd
import numpy as np



st.title('오또망')
st.write('안녕하세요 **오또망** 블로그입니다. Streamlit 재미있죠?')


import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)"))
        
        
        
    
# 데이터 프레임 
st.subheader('데이터프레임')
view = [100, 50 ,50]
view = pd.DataFrame(np.random.randn(3, 10))
st.dataframe( data = view )

with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

# 차트
st.subheader('막대차트')
st.bar_chart(view.iloc[0])


