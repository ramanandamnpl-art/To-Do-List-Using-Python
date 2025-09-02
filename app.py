import streamlit as st
from tasks import load_tasks, save_tasks
from ui import show_header, show_tasks

def main():
    show_header()
    task_list = load_tasks()

    # Add new task
    task_input = st.text_input("Add a new task:")
    if st.button("➕ Add Task"):
        if task_input.strip() != "":
            if task_input not in task_list:
                task_list.append(task_input.strip())
                save_tasks(task_list)
                st.rerun()   # ✅ updated
            else:
                st.warning("⚠️ Task already exists!")

    # Show tasks
    done_tasks = show_tasks(task_list)

    # Remove completed tasks
    if done_tasks:
        if st.button("✅ Remove Completed"):
            task_list = [t for t in task_list if t not in done_tasks]
            save_tasks(task_list)
            st.rerun()   # ✅ updated

    # Clear all
    if st.button("🗑️ Clear All Tasks"):
        task_list.clear()
        save_tasks(task_list)
        st.rerun()   # ✅ updated

if __name__ == "__main__":
    main()

