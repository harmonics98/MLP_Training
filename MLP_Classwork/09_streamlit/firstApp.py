import numpy as np
import pandas as pd
import streamlit as st


st.title('Streamlit 맛보기')
st.header('1. 텍스트 요소', divider='rainbow')
st.subheader('1.1 제목 작성을 위한 API', divider=False)
st.write('hello world')
st.write("""st.title()
st.header()
st.subheader()
""")
st.subheader('1.2 텍스트 _본문_ 작성을 위한 :red[API]')
st.write("""
st.caption()
st.text()
st.code()
st.markdown()
""")
st.text('this is a text')
st.caption('this is a caption')
sample_code = '''
def fun():
    print('Hello')
'''
st.code(sample_code, language='python')
st.markdown('''한 줄 끝에 공백(space) 두 칸 입력 시 다음 줄로 사용(soft return)  

한 행에 두 개 이상의 newline은 hard return
'''         )

st.write('[st.latex]')
st.latex('b \over a')
st.latex('\sqrt{x^2 + y^2}')

st.write('Emoji : https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/')


st.divider()
with st.echo():
    st.write('This code will be printed')


df = pd.DataFrame({'col1' : [1,2,3,4],
                    'col2' : [10,20,30,40]})
with st.echo():
    st.dataframe(df, use_container_width=True)


df1 = pd.DataFrame(np.random.randn(5,10), columns=['col_%d' % i for i in range(10)])

st.dataframe(df1)
st.dataframe(df1, width=400, height=200)
st.dataframe(df1, width=400, height=150, hide_index=True)

st.dataframe(df1.style.highlight_max(axis=0))
st.dataframe(df1.style.highlight_max(axis=1))

df2 = pd.DataFrame(
    [
        {'command' : 'st.write', 'rating' : 4, 'is_widget' : False},
        {'command' : 'st.dataframe', 'rating' : 5, 'is_widget' : True},
        {'command' : 'st.time_input', 'rating' : 3, 'is_widget' : True},
        {'command' : 'st.metric', 'rating' : 4, 'is_widget' : True},
    ]
)
st.write(df2)
st.dataframe(df2, use_container_width=True)
edited_df = st.data_editor(df2)
fav_com = edited_df.loc[edited_df['rating'].idxmax()]['command']
st.markdown(f' :red[{fav_com}] :+1:')