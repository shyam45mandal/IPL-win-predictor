import streamlit as st
import pandas as pd
import pickle

# Available Teams
Avail_teams = [
    'Royal Challengers Bangalore',
    'Chennai Super Kings',
    'Punjab Kings',
    'Delhi Capitals',
    'Mumbai Indians',
    'Kolkata Knight Riders',
    'Rajasthan Royals',
    'Sunrisers Hyderabad',
    'Gujarat Titans',
    'Lucknow Super Giants',
]
# HEX colors from your mapping
team_colors = {
    "Chennai Super Kings": "#FFF100",
    "Delhi Capitals": "#0116CF",
    "Gujarat Titans": "#1B2133",
    "Kolkata Knight Riders": "#2E0854",
    "Lucknow Super Giants": "#0057E2",
    "Mumbai Indians": "#004BA0",
    "Punjab Kings": "#ED1B24",
    "Rajasthan Royals": "#FC4CFC",
    "Royal Challengers Bangalore": "#CC1213",
    "Sunrisers Hyderabad": "#FF6600"
}

# Cities
cities = [
    'Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
    'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
    'Centurion', 'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
    'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune',
    'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Dubai', 'Bengaluru',
    'Indore', 'Navi Mumbai', 'Lucknow', 'Guwahati', 'Mohali'
]

# Streamlit page setup
st.set_page_config(page_title="🏏 IPL Live Win Predictor", layout="centered")
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title("🏏 IPL Live Win Predictor")

# Select inputs
selected_city = st.selectbox("Select Match City", cities)

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Batting Team', Avail_teams)
with col2:
    bowling_team = st.selectbox('Bowling Team', Avail_teams)

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('Score', min_value=0)
with col4:
    over = st.number_input('Overs', min_value=0.0, max_value=20.0, step=0.1)

with col5:
    wicket = st.number_input('Wicket', min_value=0, max_value=10)

target = st.number_input('Target', min_value=0)

# ---- Calculations ----
runs_left = target - score
balls_bowled = ((over * 10) // 10) * 6 + ((over * 10) % 10)  # converting overs.x to balls
balls_left = 120 - balls_bowled
wickets_left = 10 - wicket
crr = score / ((120 - balls_left) / 6) if (120 - balls_left) != 0 else 0
rrr = runs_left / (balls_left / 6) if balls_left != 0 else 0

# ---- Display Calculations ----
st.markdown("### 📊 Scoreboard")

col_a, col_b, col_c = st.columns(3)
col_a.metric("Runs Left", runs_left)
col_b.metric("Balls Left", balls_left)
col_c.metric("Wickets Left", wickets_left)

col_d, col_e, col_f = st.columns(3)
col_d.metric("Current Run Rate", round(crr, 2))
col_e.metric("Required Run Rate", round(rrr, 2))
col_f.metric("Target", target)


if st.button("Predict"):
    input_df=pd.DataFrame({
        'batting_team': [batting_team],'bowling_team':[ bowling_team],'city': [selected_city],'run_left':[runs_left],'ball_left':[balls_left],'wicket_left':[wickets_left],'Run_rate':[crr],'Required_rate':[rrr],'target_runs':[target]
    })

    result = pipe.predict_proba(input_df)

    loss=result[0][0]
    win=result[0][1]

    batting_pct = round(win*100)
    bowling_pct = round(loss*100)

    st.markdown(
        f"""
        <div style='display: flex; width: 100%; height: 50px; border: 1px solid black;'>
            <div style='flex: {batting_pct}; background-color: {team_colors[batting_team]}; 
                        display: flex; align-items: center; justify-content: center; font-weight: bold;'>
                {batting_pct}%
            </div>
            <div style='flex: {bowling_pct}; background-color: {team_colors[bowling_team]}; 
                        display: flex; align-items: center; justify-content: center; font-weight: bold; color: white;'>
                {bowling_pct}%
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.header(batting_team+'-     '+str(round(win*100))+"%")
    st.header(bowling_team + '-   ' + str(round(loss*100))+"%")

