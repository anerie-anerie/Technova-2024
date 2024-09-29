try:
    import streamlit as st
    import pandas as pd
    import os
    import sys
    from io import BytesIO, StringIO

except Exception as e:
    print("Some Modules are Missing: {}".format(e))

def main():
    st.info(__doc__)
    st.markdown(STYLE, unsafe_allow_html = True)
    file = st.file_uploader(label = "Uplooad your file here: ", type = ["png","jpg"])
    show_file = st.empty()

    if not file:
        show_file.info("Please upload a file: {}".format("".join(["png","jpg"])))
        return

    content = file.getvalue()

    if isistance(file, BytesIO):
        show_file.image(file)
    file.close()


main()
