# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.list_of_todos = []

    def add(self, todo):
        self.list_of_todos.append(todo)
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        

    def incomplete(self):
        return [task for task in self.list_of_todos if task.complete == False]

        # Returns:
        #   A list of Todo instances representing the todos that are not complete


    def complete(self):
        return [task for task in self.list_of_todos if task.complete]
        # Returns:
        #   A list of Todo instances representing the todos that are complete

    def give_up(self):
        for item in self.list_of_todos:
            item.mark_complete()
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        


# File: lib/todo.py
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        self.task = task
        self.complete = False
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False


    def mark_complete(self):
        self.complete = True
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
    
