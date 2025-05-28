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

data_list1= ('Mon','Tues','Wed','Thurs','Fri')
df = pd.DataFrame({
    'DOW':data_list1,
    'value':[1,2,3,0,0]
    })
df  # 👈 Draw the dataframe

x = 10
'the value of x is:', x  # 👈 Draw the string 'x' and then the value of x
x
data_list1

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))

randomdata = np.random.randn(10, 20)
st.dataframe(randomdata)


st.write("")
st.write("### another line2")
st.write('')
st.write('>> So now we get some text')
st.write('>>> So now we get some text')

st.write('![Atom](atom.png "Atomic logo")')

