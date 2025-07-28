
import streamlit as st
from algorithmeai import titanic

st.set_page_config(page_title="Will I Survive the Titanic?", page_icon="🚢", layout="centered")

st.title("🚢 Will I Survive the Titanic?")
st.write("Enter passenger details below and let the BlackSwan model predict your chances of survival and explain why.")

# Input form
with st.form("input_form"):
    pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
    sex = st.selectbox("Sex", ["male", "female"])
    age = st.slider("Age", 0, 100, 30)
    sibsp = st.number_input("Siblings/Spouses Aboard", 0, 10, 0)
    parch = st.number_input("Parents/Children Aboard", 0, 10, 0)
    fare = st.number_input("Fare Paid", 0.0, 600.0, 32.0)
    embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])
    ticket = st.text_input("Ticket", "A/5 21171")
    cabin = st.text_input("Cabin", "")
    name = st.text_input("Name", "John Doe")

    submitted = st.form_submit_button("Predict and Explain")

if submitted:
    row_dict = {
        "Pclass": pclass,
        "Name": name,
        "Sex": sex,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Ticket": ticket,
        "Fare": fare,
        "Cabin": cabin,
        "Embarked": embarked
    }

    result = titanic.my_graphic_function(row_dict)
    score = result['estimation']
    percent = round(score * 100, 2)

    st.markdown(f"### 🧬 Predicted Survival Probability: **{percent}%**")
    if score > 0.5:
        st.success("You would likely survive! 🎉")
    else:
        st.error("You would likely not survive. 😢")

    st.subheader("🧪 Feature Contributions")
    audit_data = result.get('features_audit', {})
    if audit_data:
        st.table({k: {"Value": v[0], "Percent": v[1]} for k, v in audit_data.items()})

    st.subheader("📊 Lookalike Passengers (CSV Similarities)")
    csv_raw = result.get('csv', '')
    if csv_raw:
        import pandas as pd
        from io import StringIO
        try:
            df_lookalikes = pd.read_csv(StringIO(csv_raw))
            st.dataframe(df_lookalikes)
        except Exception as e:
            st.error("Couldn't parse lookalike CSV data.")
            st.text(csv_raw)
