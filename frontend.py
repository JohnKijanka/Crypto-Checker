import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/prices"

st.title("Real-Time Cryptocurrency Price Dashboard")

cryptos = st.text_input("Enter cryptocurrency symbols (comma-separated):", "bitcoin,ethereum")

if st.button("Get Prices"):
    response = requests.get(API_URL, params={'cryptos': cryptos})
    if response.status_code == 200:
        prices = response.json()
        for crypto, price in prices.items():
            st.write(f"{crypto.capitalize()}: ${price[crypto]['usd']}")
    else:
        st.write("Failed to fetch prices. Please try again.")
