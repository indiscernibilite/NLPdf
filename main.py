import streamlit as st
from sklearn import datasets
import pandas as pd
import openai
import sys

st.title("자연어로 데이터프레임 변환하기")
st.text("데이터프레임에 적용하고 싶은 것을 자연어로 표현하면 그에 따라 변환해줍니다.\n그만 변환하고 싶으면 'stop'을 작성해주세요.")

st.subheader("📊 데이터프레임")
iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
st.dataframe(df.head())



openai.api_key = "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"

# 격리된 local variables
mylocals = {}
def myexec(code):
  global mylocals
  print("# code: \n" + code)
  exec(code, globals(), mylocals)
def myset(x, v):
  global mylocals
  mylocals[x] = v
def myget(x):
  return mylocals[x]

#chat GPT와 주고받는 대화를 기록하기 위한 함수. str을 request로 보냄. return도 받아옴.
def myrequest(req):
  mymessages.append({"role": "user", "content": req})
  response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=mymessages,
  temperature=0,
  )
  ret = response['choices'][0]['message']['content']
  mymessages.append({"role": "assistant", "content": ret})
  return ret

# ChatGPT한테 시키고 받아온 코드 실행 시킴
def myexeccode(str):
  global initialprompt
  str = initialprompt + "# " + str
  initialprompt = ""  
  code = myrequest(str)
  myexec(code)
  return myget('df')

# 초기화
def DataGPT(df):
  global mylocals
  global mymessages
  global initialprompt
  # initialization code
  initialcode = (f"import pandas as pd \ndf = pd.DataFrame({df})")
  # initialize local variables
  mylocals = {}
  myset('df', df)
  df
  # initialize message history
  mymessages = [
        {"role": "system", "content": "You are a smart python developer."},
    ]
  initialprompt = """
      DO NOT EXPLAIN! just put executable code! no double quotation.
      Write down the code that will COME AFTER the following Python code.
      Do not repeat the code I wrote!
      All task will be done in place.
      ———————————
      """ + initialcode
  while True:
    msg
    if msg == "stop":
      break
    myexeccode(msg)
  return myget('df')

textbox = st.text_input(label="명령어를 입력하세요", key="msg")
              
