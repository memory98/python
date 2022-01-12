import streamlit as st
import numpy as np
import pandas as pd
import re

file_path = './export_sample.xml'
df = pd.DataFrame([], columns=['date', 'bpm'])

pattern = '^.*IdentifierHeartRate".*startDate="(.{19}).*value="([0-9]*).*$'

with open(file_path, 'r',encoding="utf-8") as f:
    for line in f:
        search = re.search(pattern, line)
        if search is not None:
            
            df = df.append({
                'date': search.group(1),
                'bpm': search.group(2)
            }, ignore_index=True)

df.date = pd.to_datetime(df.date)
df.bpm = pd.to_numeric(df.bpm)

df = df.set_index('date')
df = df.sort_index()

# st.table(df)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)