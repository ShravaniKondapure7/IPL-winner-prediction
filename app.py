
import os
import pickle
import streamlit as st
import pandas as pd

st.write("Current Files:", os.listdir())
model = pickle.load(open("ipl_model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

st.title("🏏 IPL Match Winner Prediction")

batting_team = st.text_input("Enter Batting Team")
bowling_team = st.text_input("Enter Bowling Team")
city = st.text_input("Enter City")
toss_winner = st.text_input("Enter Toss Winner")
toss_decision = st.selectbox("Toss Decision", ["bat", "field"])

if st.button("Predict Winner"):

    input_dict = {
        "batting_team": batting_team,
        "bowling_team": bowling_team,
        "city": city,
        "toss_winner": toss_winner,
        "toss_decision": toss_decision,
        "team1_win_rate": 0,
        "team2_win_rate": 0
    }

    input_df = pd.DataFrame([input_dict])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_df)

    st.success(f"🏆 Predicted Winner: {prediction[0]}")
