import openai
import streamlit as st

st.title("Chatbot")

openai.api_key = st.secrets["OPENAI_API_KEY"]

# set up columns
left_col, right_col = st.columns([2, 1]) # adjust

# use right column for chatbot
with right_col:

    # set a default model
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    # initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # accept user input
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # display assistant message in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # call openai api with the new interface
            response = openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
            )
            
            # get the response content
            full_response = response['choices'][0]['message']['content']
            message_placeholder.markdown(full_response)

        # add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})