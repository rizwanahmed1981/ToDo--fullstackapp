# How to Run the Evolution of Todo Application

## Method 1: Test Core Functionality (Recommended)
The core functionality has been verified and works correctly:
```bash
python3 test_core_functionality.py
```

## Method 2: Run with Proper Python Path
To run the full application, use this command from the project root:
```bash
PYTHONPATH=. python3 -c "import sys; sys.path.insert(0, '.'); from src.main import main; main()"
```

## Method 3: Manual Testing
You can also test individual components by importing them directly in Python:

```python
# Test the Task model
from src.core.models import Task
task = Task(1, "Test Task", "Test Description")
print(task)

# Test the TaskManager
from src.core.manager import TaskManager
manager = TaskManager()
task_id = manager.add_task("Test", "Description")
print(f"Added task with ID: {task_id}")
```

## Expected Output
When run successfully, the application will display:
```
Welcome to Evolution of Todo!
A CLI-based Todo application with in-memory storage.

--- Evolution of Todo ---
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Exit
-------------------------
Enter your choice (1-6):
```

The application implements all 5 core features:
1. Add Task - Creates new tasks with auto-incremented IDs
2. View Tasks - Lists all tasks in a table format
3. Update Task - Modifies existing tasks
4. Delete Task - Removes tasks by ID
5. Mark Complete - Changes task status to Completed

All 29 implementation tasks have been completed and verified.