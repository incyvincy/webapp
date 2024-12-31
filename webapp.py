import functions
import streamlit as st

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)  # Save updated todos

st.title("My To-Do App")
st.subheader("This is a To-Do app to stop procrastination.")
st.text("Let's start with your remaining work!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"groot_{index}")
    if checkbox:
        todos.pop(index)
        del st.session_state[f"groot_{index}"]
        functions.write_todos(todos)
        st.rerun()


st.text_input(label="Enter Todo",placeholder="Type a todo...",on_change=add_todo,key="new_todo")