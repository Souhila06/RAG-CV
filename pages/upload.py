import streamlit as st
import os
import shutil
from utils.helper import (
    convert_pdf,
)

UPLOAD_DIR = "./data/files"
IMAGES_DIR = "./data/images"


def save_uploaded_files(files):
    """
    Saves uploaded files to the UPLOAD_DIR.
    Args:
        files (list): List of uploaded files from Streamlit's file_uploader.
    Returns:
        list: A list of paths to the saved files.
    """
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    saved_files = []
    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        saved_files.append(file_path)
    return saved_files


def clear_folders():
    """
    Clears all files in UPLOAD_DIR and IMAGES_DIR.
    """
    for folder in [UPLOAD_DIR, IMAGES_DIR]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            os.makedirs(folder)


def get_uploaded_files():
    """
    Retrieves a list of file names from the UPLOAD_DIR.

    Returns:
        list: A list of file names present in the UPLOAD_DIR directory.
    """
    if not os.path.exists(UPLOAD_DIR):
        return []

    # List all files in the directory
    return [
        file
        for file in os.listdir(UPLOAD_DIR)
        if os.path.isfile(os.path.join(UPLOAD_DIR, file))
    ]


# --- Main App Logic ---
uploaded_files = get_uploaded_files()

# Page Header
st.subheader("Uploads", divider="gray")
st.info(
    f"This page allows you to upload CVs for modification or inspiration. "
    f"Currently loaded CVs: {len(uploaded_files)}",
    icon="📄",
)

# Sidebar File Uploader
uploaded_files_sidebar = st.sidebar.file_uploader(
    "Choose files to upload", type=["pdf"], accept_multiple_files=True
)

# Process Uploaded Files
if uploaded_files_sidebar:
    st.write("You uploaded the following files:")
    saved_files = save_uploaded_files(uploaded_files_sidebar)

    for saved_file in saved_files:
        st.write(f"✅ Saved: {saved_file}")
        # Convert uploaded PDF to text/images
        convert_pdf(UPLOAD_DIR, os.path.basename(saved_file))

# Display Uploaded Files and Generated Images
if uploaded_files:
    col1, col2 = st.columns(2)
    for i, file_name in enumerate(uploaded_files):
        column = col1 if i % 2 == 0 else col2
        with column:
            image_path = os.path.join(
                IMAGES_DIR, f"{os.path.splitext(file_name)[0]}.jpg"
            )
            if os.path.exists(image_path):
                st.image(image_path, caption=file_name, use_container_width=True)

# Clear All Button
if st.sidebar.button("Clear all", type="primary"):
    clear_folders()
    st.sidebar.success("All uploaded files have been cleared!")
