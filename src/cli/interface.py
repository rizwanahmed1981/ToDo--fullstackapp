"""
Evolution of Todo - CLI Interface
Handles user interaction through command line interface
"""
from typing import Optional
from src.core.manager import TaskManager


class CLIRunner:
    """
    Handles user interaction through the command line interface.
    Contains the main menu loop and processes user commands.
    """

    def __init__(self):
        """
        Initialize the CLI runner with a TaskManager instance.
        """
        self.task_manager = TaskManager()

    def run(self):
        """
        Run the main menu loop until user selects Exit.
        """
        while True:
            self._display_menu()
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self._add_task()
            elif choice == "2":
                self._view_tasks()
            elif choice == "3":
                self._update_task()
            elif choice == "4":
                self._delete_task()
            elif choice == "5":
                self._complete_task()
            elif choice == "6":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.\n")

    def _display_menu(self):
        """
        Display the main menu options to the user.
        """
        print("\n--- Evolution of Todo ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Complete")
        print("6. Exit")
        print("-------------------------")

    def _add_task(self):
        """
        Handle adding a new task.
        """
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()
        if not title:
            print("Title cannot be empty.\n")
            return

        description = input("Enter task description: ").strip()

        task_id = self.task_manager.add_task(title, description)
        print(f"Task added successfully with ID: {task_id}\n")

    def _view_tasks(self):
        """
        Handle viewing all tasks in a table-like format.
        """
        print("\n--- All Tasks ---")
        tasks = self.task_manager.get_tasks()

        if not tasks:
            print("No tasks found.\n")
            return

        # Print table header
        print(f"{'ID':<5} {'Status':<12} {'Title':<30}")
        print("-" * 50)

        # Print each task
        for task in tasks:
            print(f"{task.id:<5} {task.status:<12} {task.title:<30}")
        print()

    def _update_task(self):
        """
        Handle updating an existing task.
        """
        print("\n--- Update Task ---")
        try:
            task_id = int(input("Enter task ID to update: ").strip())
        except ValueError:
            print("Invalid task ID. Please enter a number.\n")
            return

        # Check if task exists
        tasks = self.task_manager.get_tasks()
        task_exists = any(task.id == task_id for task in tasks)
        if not task_exists:
            print(f"Task with ID {task_id} not found.\n")
            return

        print("Leave blank to keep current value.")
        new_title = input(f"Enter new title (current: {self._get_task_title(task_id)}): ").strip()
        new_description = input(f"Enter new description (current: {self._get_task_description(task_id)}): ").strip()

        # Prepare update parameters
        title_update = new_title if new_title else None
        description_update = new_description if new_description else None

        # Perform update if there's something to update
        if title_update or description_update:
            success = self.task_manager.update_task(
                task_id,
                title=title_update if title_update else None,
                description=description_update if description_update else None
            )
            if success:
                print("Task updated successfully.\n")
            else:
                print("Failed to update task.\n")
        else:
            print("No changes made.\n")

    def _delete_task(self):
        """
        Handle deleting a task.
        """
        print("\n--- Delete Task ---")
        try:
            task_id = int(input("Enter task ID to delete: ").strip())
        except ValueError:
            print("Invalid task ID. Please enter a number.\n")
            return

        success = self.task_manager.remove_task(task_id)
        if success:
            print("Task deleted successfully.\n")
        else:
            print(f"Task with ID {task_id} not found.\n")

    def _complete_task(self):
        """
        Handle marking a task as complete.
        """
        print("\n--- Mark Task Complete ---")
        try:
            task_id = int(input("Enter task ID to mark complete: ").strip())
        except ValueError:
            print("Invalid task ID. Please enter a number.\n")
            return

        success = self.task_manager.complete_task(task_id)
        if success:
            print("Task marked as complete.\n")
        else:
            print(f"Task with ID {task_id} not found.\n")

    def _get_task_title(self, task_id: int) -> str:
        """
        Get the title of a task by ID.

        Args:
            task_id: ID of the task

        Returns:
            Title of the task or empty string if not found
        """
        tasks = self.task_manager.get_tasks()
        for task in tasks:
            if task.id == task_id:
                return task.title
        return ""

    def _get_task_description(self, task_id: int) -> str:
        """
        Get the description of a task by ID.

        Args:
            task_id: ID of the task

        Returns:
            Description of the task or empty string if not found
        """
        tasks = self.task_manager.get_tasks()
        for task in tasks:
            if task.id == task_id:
                return task.description
        return ""