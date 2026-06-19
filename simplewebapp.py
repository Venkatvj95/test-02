import streamlit as st

st.set_page_config(
    page_title="Simple Chatbot",
    page_icon="🤖"
)

st.title("🤖 Simple Streamlit Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Simple bot response
    bot_response = f"You said: {user_input}"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_response
        }
    )

    with st.chat_message("assistant"):
        st.write(bot_response)