import streamlit as st
import os
import shutil

def save_uploaded_file(uploaded_file):
    savedir = "/users/anerie/technova-24/InputImg"
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    file_path = os.path.join(savedir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path

def image_dropboxes():
    labels = ["nail image", "palm image", "eye image"]
    image_files = {}

    for label in labels:
        file = st.file_uploader(label=f"Upload your {label} here:", type=["png", "jpg"])

        if file:
            # Display the uploaded file
            st.image(file, caption=label)

            # Add a submit button for each file
            if st.button(f"Submit {label}"):
                # Save the uploaded file
                file_path = save_uploaded_file(file)
                image_files[label] = file_path
                st.success(f"{label} has been saved to {file_path}.")
        else:
            st.warning(f"Please upload a(n) {label} (png or jpg).")

image_dropboxes()
