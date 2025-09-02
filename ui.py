import streamlit as st

def show_header():
    st.title("✅ To-Do List")
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg");
            background-attachment: fixed;
            background-size: cover;
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_tasks(task_list):
    if task_list:
        st.subheader("Your Tasks")
        done_tasks = []
        for task in task_list:
            if st.checkbox(task, key=task):
                done_tasks.append(task)
        return done_tasks
    else:
        st.write("📭 No tasks yet.")
        return []

