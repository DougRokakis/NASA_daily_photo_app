import requests
import streamlit as st
from datetime import date

today = date.today()
api_key = "6aDob2MMK1jfweY4hQjyRoWjXfV4zSJKzbevhm9S"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={today}"

# random_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&count"

# Make request
response = requests.get(url)

# Get a dictionary with data
content = response.json()

todays_date = content["date"]
image_hdurl = content["hdurl"]
explanation = content["explanation"]
title = content["title"]
image_url = content["url"]

st.header("Your NASA image of the day!")

st.subheader(title)

st.image(image_hdurl)

st.write(explanation)



