import streamlit as st

from datetime import date
from dateutil.relativedelta import relativedelta

import datetime

title=st.title("Age Checker 🎂")

current_date=date.today()


current_date_shower=st.subheader(f"Current Data Is :{current_date} (YYYY/DD/MM) " )



name=st.text_input("Can i know your name :").upper()
dob=st.date_input("Enter DOB",value=date(2000,1,1),min_value= date(1900,1,1),max_value=current_date)


if st.button("what's my age"):
    age=relativedelta(current_date,dob)
    st.success(f"{name} your age is {age.years} years {age.months} month and {age.days} days")
if age.years>18:
    st.info(f" {name} ✅ You are a adult")
else:
    st.info(f"{name}you are a teenager ")