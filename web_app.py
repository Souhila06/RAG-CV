import streamlit as st


def page2():
    st.title("Second page")


pg = st.navigation(
    [
        st.Page("./pages/prompt.py", title="Prompt", icon="🔥"),
        st.Page("./pages/upload.py", title="Uploads", icon=":material/favorite:"),
    ]
)
pg.run()
