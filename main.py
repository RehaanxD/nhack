import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = "given in doc"

# Function to get government schemes and subsidies suggestions
def get_schemes(topic, situation):
    prompt = f"Topic: {topic}\nSituation: {situation}\nSuggest government schemes and subsidies for the given situation provided by the indian government act as a professioal in this field."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a user."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message["content"].strip()

# Main Streamlit app
def main():
    st.title("Government Schemes and Subsidies Chat")

    # Sidebar selection for topic
    topic = st.sidebar.selectbox("Select Topic", ["Women", "Farmer", "Startups", "Cottage industries", "Cooperatives", "Unorganised business"])

    # Display the selected topic
    st.subheader(f"Selected Topic: {topic}")

    # Text input for situation
    situation = st.text_area(f"Enter the situation for the {topic} topic:")

    if st.button("Get Suggestions"):
        # Get suggestions from OpenAI
        schemes = get_schemes(topic, situation)

        # Display suggestions
        st.subheader("Government Schemes and Subsidies:")
        st.write(schemes)

if __name__ == "__main__":
    main()
