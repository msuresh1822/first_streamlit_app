import streamlit
streamlit.title('Hi, Good Morning Family')
streamlit.title('My Parents New Healthy Diner')
streamlit.header('❤️Breakfast Menu')
streamlit.text('🍇omega 3 & Blueberry oatmeal')
streamlit.text('🥬kale,Spinach & Rocket Smoothie')
streamlit.text('🐔	Hard_Boiled Free_range Egg')
streamlit.text("Avocado Toast")
streamlit.header('Build your own fruit smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)),['Avocado','Strawberries']
streamlit.dataframe(my_fruit_list)


