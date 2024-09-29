import streamlit as st
import os
import sys
import shutil

sys.path.append('/Users/anerie/technova-24')
from anemicScore import aScoring

# Function to save uploaded files
def save_uploaded_file(uploaded_file, label):
    savedir = "/users/anerie/technova-24/InputImg"
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    # Save the file with the label as the filename
    file_path = os.path.join(savedir, f"{label}.png")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path

# Function to create the upload interface for images
def image_dropboxes():
    labels = ["nail image", "palm image", "eye image"]
    image_files = {}

    for label in labels:
        file = st.file_uploader(label=f"Upload your {label} here:", type=["png", "jpg"])

        if file:
            # Display the uploaded image
            st.image(file, caption=label)

            # Save the file immediately with the appropriate label
            file_path = save_uploaded_file(file, label.split()[0])  # Save as nail.png, palm.png, eye.png
            image_files[label] = file_path

    return image_files

# Function to clear all images in InputImg folder
def clear_input_folder():
    folder_path = "/users/anerie/technova-24/InputImg"
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

# Main function
def main():
    # Collect uploaded images
    st.title("Anemia Score Calculator")
    image_files = image_dropboxes()

    # Only show the button if all 3 images are uploaded
    if len(image_files) == 3:
        if st.button("Calculate Anemia Score"):
            # Call anemicScore with predefined image paths
            nail_img = "/users/anerie/technova-24/InputImg/nail.png"
            palm_img = "/users/anerie/technova-24/InputImg/palm.png"
            eye_img = "/users/anerie/technova-24/InputImg/eye.png"

            # Call the anemicScore function with these paths
            score = aScoring(nail_img, palm_img, eye_img)

            # Display the calculated score
            st.success(f"Anemia Score: {score}")

            # Clear the InputImg folder after the calculation
            clear_input_folder()
            st.info("Input images have been cleared.")

if __name__ == "__main__":
    main()
