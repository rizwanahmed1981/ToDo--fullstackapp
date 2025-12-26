#!/usr/bin/env python3
"""
Debug script to test the TaskManager functionality directly
"""
import sys
import os

# Add project root to path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from src.core.models import Task
from src.core.manager import TaskManager

def test_basic_functionality():
    """Test that basic functionality works"""
    print("Testing TaskManager functionality...")

    # Create manager
    manager = TaskManager()

    # Add a task
    task_id = manager.add_task("Test Task", "Test Description")
    print(f"Added task with ID: {task_id}")

    # Get tasks
    tasks = manager.get_tasks()
    print(f"Retrieved {len(tasks)} tasks")

    if tasks:
        task = tasks[0]
        print(f"Task ID: {task.id}, Title: {task.title}, Status: {task.status}")

    # Test listing functionality
    print("\n--- Listing tasks directly ---")
    if not tasks:
        print("No tasks found.")
    else:
        print(f"{'ID':<5} {'Status':<12} {'Title':<30}")
        print("-" * 50)
        for task in tasks:
            print(f"{task.id:<5} {task.status:<12} {task.title:<30}")

    return True

if __name__ == "__main__":
    test_basic_functionality()