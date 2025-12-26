"""
Evolution of Todo - Task Manager
Handles all task-related operations with in-memory storage
"""
from typing import List, Optional
from .models import Task


class TaskManager:
    """
    Manages all task operations with in-memory storage.
    Provides methods for CRUD operations on tasks.
    """

    def __init__(self):
        """
        Initialize the TaskManager with empty task list and ID counter.
        """
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: str) -> int:
        """
        Creates a new task with auto-incremented ID and default status 'Pending'.

        Args:
            title: Title of the task
            description: Description of the task

        Returns:
            The ID of the newly created task
        """
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            status="Pending"
        )
        self._tasks.append(task)
        task_id = self._next_id
        self._next_id += 1
        return task_id

    def remove_task(self, task_id: int) -> bool:
        """
        Removes a task by ID.

        Args:
            task_id: ID of the task to remove

        Returns:
            True if the task was found and removed, False otherwise
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                self._tasks.pop(i)
                return True
        return False

    def get_tasks(self) -> List[Task]:
        """
        Returns all tasks.

        Returns:
            List of all tasks
        """
        return self._tasks.copy()

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Updates a task's title or description.

        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            True if the task was found and updated, False otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                return True
        return False

    def complete_task(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id: ID of the task to mark as completed

        Returns:
            True if the task was found and marked as completed, False otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                task.status = "Completed"
                return True
        return False