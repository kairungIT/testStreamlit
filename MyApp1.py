import streamlit as st
import pandas as pd

st.title("🍌🍌Website Developing using Python🍌🍌")
#st.header("🍖🍖Website Developing using Python🍖🍖")

st.subheader("Kairung Hengpraprohm")
st.image('kairung.jpg')

dt=pd.read_csv('./data/iris.csv')

st.subheader("ข้อมูลดอกไม้ Iris")
st.write(dt.head(10))
#Index(['sepal.length', 'sepal.width', 'petal.length', 'petal.width',
#       'variety'],

st.subheader("สถิติข้อมูลดอกไม้ Iris")
st.write('ผลรวม')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].sum())
cl2.write(dt['sepal.width'].sum())
cl3.write(dt['petal.length'].sum())
cl4.write(dt['petal.width'].sum())

st.write("กราฟแท่ง")
a=dt['sepal.length'].sum()
b=dt['sepal.width'].sum()
c=dt['petal.length'].sum()
d=dt['petal.width'].sum()
dx=[a,b,c,d]
cx=pd.DataFrame(dx,index=["sepal.length", "sepal.width", "petal.length","petal.width"])
st.bar_chart(cx)

st.write('ค่าเฉลี่ย')
cl11,cl12,cl13,cl14=st.columns(4)
cl11.write(dt['sepal.length'].mean())
cl12.write(dt['sepal.width'].mean())
cl13.write(dt['petal.length'].mean())
cl14.write(dt['petal.width'].mean())

st.write("Area_Chart")
a=dt['sepal.length'].mean()
b=dt['sepal.width'].mean()
c=dt['petal.length'].mean()
d=dt['petal.width'].mean()
dx=[a,b,c,d]
cx=pd.DataFrame(dx,index=["sepal.length", "sepal.width", "petal.length","petal.width"])
st.bar_chart(cx)


st.write('ค่ามากที่สุด')
cl21,cl22,cl23,cl24=st.columns(4)
cl21.write(dt['sepal.length'].max())
cl22.write(dt['sepal.width'].max())
cl23.write(dt['petal.length'].max())
cl24.write(dt['petal.width'].max())

import numpy as np
import matplotlib.pyplot as plt

st.write("Pie_Chart")
a=dt['sepal.length'].max()
b=dt['sepal.width'].max()
c=dt['petal.length'].max()
d=dt['petal.width'].max()
dx=np.array([a,b,c,d])
labels=["sepal.length", "sepal.width", "petal.length","petal.width"]
myexplode=[0.2,0,0,0]

plt.pie(dx,labels=labels,explode=myexplode)
plt.show()

st.write('ค่าน้อยที่สุด')
cl31,cl32,cl33,cl34=st.columns(4)
cl31.write(dt['sepal.length'].min())
cl32.write(dt['sepal.width'].min())
cl33.write(dt['petal.length'].min())
cl34.write(dt['petal.width'].min())

st.write("Line_Chart")
a=dt['sepal.length'].min()
b=dt['sepal.width'].min()
c=dt['petal.length'].min()
d=dt['petal.width'].min()
dx=np.array([a,b,c,d])

plt.plot(dx,'o:r',ms=10)
plt.show()