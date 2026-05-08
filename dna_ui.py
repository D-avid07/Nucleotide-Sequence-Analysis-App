import streamlit as st
import requests

st.title("🧬 DNA Chaos Lab")

weird_seq = st.text_input("Enter sequence")

if st.button("Run Madness"):
    r = requests.post("http://127.0.0.1:5000/dna",
                      json={"seq": weird_seq})
    data = r.json()

    st.write("Type:", data["type"])
    st.write("mRNA:", data["mrna"])
    st.write("Protein:", data["protein"])
    st.write("Complement:", data["complement"])
    st.write("Reverse Complement:", data["reverse"])