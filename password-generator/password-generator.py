import streamlit as st  
import random  
import string 


# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes uppercase and lowercase letters

    if use_digits:
        characters += string.digits  

    if use_special:
        characters += (
            string.punctuation
        )  

    # Generate a password by randomly selecting characters based on the length provided
    return "".join(random.choice(characters) for _ in range(length))


# Streamlit UI setup
st.title("Simple Password Generator") 


length = st.slider("Select password length:", min_value=6, max_value=32, value=12)

# Checkbox options for including numbers and special characters in the password
use_digits = st.checkbox("Include numbers") 
use_special = st.checkbox(
    "Include special characters"
)  

# Button to generate password
if st.button("Generate Password"):
    password = generate_password(
        length, use_digits, use_special
    )  
    st.write(f"Generated Password: `{password}`")  # Display the generated password