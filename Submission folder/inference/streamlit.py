import streamlit as st
import inference  # This is your inference.py

# Optional: Use Streamlit's caching to avoid reloading for every user interaction
# However, since the model is loaded once in inference.py, this might not be necessary.
# from inference import predict_category

# 1. Set up your page configuration
st.set_page_config(
    page_title="Text Classification App",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Create a title and description
st.title("Text Classification App")
st.markdown("""
Welcome to the **Text Classification** application! 
Enter your text in the box below and click **Predict** to see the category.
""")

# 3. Text input widget
input_text = st.text_area("Enter text here", height=200)

# 4. When user clicks predict
if st.button("Predict Category"):
    if input_text.strip():
        # Pass the text to your inference function
        predicted_category = inference.predict_category(input_text)
        
        # Display the result
        st.success(f"**Predicted Category:** {predicted_category}")
    else:
        st.warning("Please enter some text to classify.")
