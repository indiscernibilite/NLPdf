import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris


st.title("자연어로 데이터프레임 변환하기")
st.text("데이터프레임에 적용하고 싶은 것을 자연어로 표현하면 그에 따라 변환해줍니다.\n그만 변환하고 싶으면 'stop'을 작성해주세요.")

iris = load_iris() # sample data load
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df
st.table(df)
