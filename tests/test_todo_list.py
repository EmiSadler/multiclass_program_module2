from lib.todo_list import *
import pytest

def test_add_one_todo():
    todo = "Record a video"
    task = Todo(todo)
    lst = TodoList()
    lst.add(task)
    assert lst.list_of_todos == [task]

def test_incomplete_list_one_item():
    todo = "Make a thumbnail"
    task = Todo(todo)
    lst = TodoList()
    lst.add(task)
    result = lst.incomplete()
    assert result == [task]
    
def test_incomplete_multiple_items():
    todo = "Remux the mkv file"
    task = Todo(todo)
    todo2 = "Copy the template over"
    task2 = Todo(todo2)
    todo3 = "Rename the files"
    task3 = Todo(todo3)
    lst = TodoList()
    lst.add(task)
    lst.add(task2)
    lst.add(task3)
    result = lst.incomplete()
    assert result == [task, task2, task3]

def test_mark_as_complete():
    todo = "Choose music file"
    task = Todo(todo)
    task.mark_complete()
    assert task.complete == True

