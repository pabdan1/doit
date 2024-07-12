import streamlit as st
import csv
import pickle as pk
import pandas as pd
import mysql.connector  		#importing database
from sklearn.preprocessing import OrdinalEncoder
ord_enc = OrdinalEncoder()


#database connection
database = mysql.connector.connect(host="localhost",
									user="root",
									password="",
								   	database = "covid"
									)

#create a form
name = st.text_input("Enter name")
Age = st.number_input("Enter Age: ", 20, 65)
Gender = st.selectbox("Gender: ", ["Male", "Female"])
Experience = st.number_input("Enter Experience: ", 0, 40)
Education = st.selectbox("Education:", ["Bachelor's", "Master's", "PhD"])

if st.button("Submit"):
	if Gender == "Male":
		g = True
	else:
		g = False

	if Education == "Bachelor's":
		b = True; m = False; p = False
	elif Education == "Master's":
		b = False; m = True; p = False
	else:
		b = False; m = False; p = True

	df = pd.DataFrame({
		"Age":[Age],
		"Years of Experience":[Experience],
		#"Gender":[Gender],
		"Bachelor's":[b],
		"Master's":[m],
		"PhD":[p]
		})

	#Load and predict model
	file . = . open('model.pickle', 'rb')
	#dump information to theat file
	my_model . = . pk..oad(file)
	salary = my_model.predict(df)[0]
	st.write(salary)
	df['name'] = name
	df['salary'] = salary

	#sql query; triple apostrophe is used to write code in multiple lines
	sql = f'''INSERT INTO salary (sn, name, age, gender, experience, education, salary) 
	VALUES ('{name}', {Age}, '{Gender}', {Experience}, '{Education}', {salary});'''
	db.execute(sql)
	database.commit()
	st.write('Record inserted.')
	df
