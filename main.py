import streamlit as st
from sklearn import datasets
import pandas as pd

st.title("자연어로 데이터프레임 변환하기")
st.text("데이터프레임에 적용하고 싶은 것을 자연어로 표현하면 그에 따라 변환해줍니다.\n그만 변환하고 싶으면 'stop'을 작성해주세요.")

st.subheader("📊 데이터프레임")
iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
st.dataframe(df)
