import streamlit as st
import pandas as pd

c1, c2, c3, c4, c5 = st.columns(5)
count = 1
songs = [' ', '7-11'] + pd.read_csv('./songs_full.csv')['0'].tolist()
board = []

e = st.empty()

for i in range(5):
    row = []
    r1 = c1.selectbox('', songs, key=str(count))
    count += 1
    r2 = c2.selectbox('', songs, key=str(count))
    count += 1
    r3 = c3.selectbox('', songs, key=str(count))
    count += 1
    r4 = c4.selectbox('', songs, key=str(count))
    count += 1
    r5 = c5.selectbox('', songs, key=str(count))
    count += 1
    row = [r1, r2, r3, r4, r5]
    
    board.append(row)


df = pd.DataFrame(board)
e.dataframe(df)

submit = st.checkbox('sumbit')

if submit:
    for i in board:
        print(i)
