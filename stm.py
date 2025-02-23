import streamlit as st
from datetime import datetime

# Заголовок приложения
st.title("Календарь")

# Виджет для выбора даты
selected_date = st.date_input("Выберите дату", datetime.now())

# Отображение выбранной даты
st.write("Вы выбрали дату:", selected_date)
