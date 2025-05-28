# Streamlit HelloWorld

import streamlit as st
import pandas as pd
import numpy as np

'''
# *Streamlit* Page
## _**I**_ am ~~Streamlit~~

> So now we get some text
>> So now we get some text
>>> So now we get some text
'''

st.sidebar.title("Choose from these options")

day_list1= ('Mon','Tues','Wed','Thurs','Fri')
df = pd.DataFrame({
    'DOW':day_list1,
    'value':[1,2,3,0,0]
    })
df  # 👈 Draw the dataframe


x = st.sidebar.radio('Language',
    ('English', 'French'))

if lang == 'French':
    lang

if st.sidebar.checkbox('Choose number'):
    option = st.selectbox(
        'Which number do you like best?',
        df['DOW'])
    'You selected: ', option

x = 10
'the value of x is:', x  # 👈 Draw the string 'x' and then the value of x

if st.sidebar.checkbox('Show days'):
    day_list1

if st.sidebar.checkbox('Simple table'):
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))

if st.sidebar.checkbox('Table'):
    dataframe = pd.DataFrame(
        np.random.randn(10, 20),
        columns=('col %d' % i for i in range(20)))
    st.dataframe(dataframe.style.highlight_max(axis=0))

if st.sidebar.checkbox('Random'):
    randomdata = np.random.randn(10, 20)
    st.dataframe(randomdata)

if st.sidebar.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

if st.sidebar.checkbox('Show widget'):
    import streamlit as st
    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'squared is', x * x)

if st.sidebar.checkbox('Show dataframe2'):
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [2, 2] + [52.76, -1.4],
        columns=['lat', 'lon'])
    st.map(map_data)

if st.sidebar.checkbox('Name'):
    st.sidebar.text_input("Your name", key="name")
# You can access the value at any point with:
    st.session_state.name




#st.write("")
#st.write("### another line2")
#st.write('')
#st.write('>> So now we get some text')
#st.write('>>> So now we get some text')

#st.write('![Atom](atom.png "Atomic logo")')

