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

def test_complete_list_one_item():
    todo = "seperate audio tracks"
    task = Todo(todo)
    task.mark_complete()
    lst = TodoList()
    lst.add(task)
    result = lst.complete()
    assert result == [task]

def test_complete_list_multiple_items_two_completed():
    todo = "process audio voice track"
    task = Todo(todo)
    task.mark_complete()
    todo2 = "find levels"
    task2 = Todo(todo2)
    task2.mark_complete()
    todo3 = "remove silences"
    task3 = Todo(todo3)
    lst = TodoList()
    lst.add(task)
    lst.add(task2)
    lst.add(task3)
    result = lst.complete()
    assert result == [task, task2]

def test_empty_todo_incomplete():
    todo = ""
    task = Todo(todo)
    lst = TodoList()
    lst.add(task)
    result = lst.incomplete()
    assert result == [task]

def test_alternate_data_type_complete():
    todo = True
    task = Todo(todo)
    task.mark_complete()
    lst = TodoList()
    lst.add(task)
    result = lst.complete()
    assert result == [task]
    
def test_give_up_one_item():
    todo = "insert end screen and blend out"
    task = Todo(todo)
    lst = TodoList()
    lst.add(task)
    lst.give_up()
    result = lst.complete()
    assert result == [task]

def test_give_up_multiple_tasks():
    todo = "add music track"
    task = Todo(todo)
    todo2 = "adjust audio levels"
    task2 = Todo(todo2)
    todo3 = "encode video"
    task3 = Todo(todo3)
    lst = TodoList()
    lst.add(task)
    lst.add(task2)
    lst.add(task3)
    lst.give_up()
    result = lst.complete()
    assert result == [task, task2, task3]
