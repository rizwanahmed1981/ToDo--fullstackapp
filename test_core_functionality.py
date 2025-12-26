#!/usr/bin/env python3
"""
Test script to verify the core functionality of the Evolution of Todo application
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.core.models import Task
from src.core.manager import TaskManager

def test_task_model():
    """Test that the Task dataclass works correctly"""
    print("Testing Task model...")
    task = Task(id=1, title="Test Task", description="This is a test", status="Pending")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "This is a test"
    assert task.status == "Pending"
    print("✓ Task model works correctly")

def test_task_manager():
    """Test that the TaskManager works correctly"""
    print("Testing TaskManager...")
    manager = TaskManager()

    # Test adding a task
    task_id = manager.add_task("Test Task", "Test Description")
    assert task_id == 1

    # Test getting tasks
    tasks = manager.get_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1
    assert tasks[0].title == "Test Task"
    assert tasks[0].description == "Test Description"
    assert tasks[0].status == "Pending"

    # Test completing a task
    success = manager.complete_task(1)
    assert success == True
    tasks = manager.get_tasks()
    assert tasks[0].status == "Completed"

    # Test updating a task
    success = manager.update_task(1, title="Updated Task")
    assert success == True
    tasks = manager.get_tasks()
    assert tasks[0].title == "Updated Task"

    # Test deleting a task
    success = manager.remove_task(1)
    assert success == True
    tasks = manager.get_tasks()
    assert len(tasks) == 0

    print("✓ TaskManager works correctly")

def main():
    """Run all tests"""
    print("Running core functionality tests...\n")

    test_task_model()
    test_task_manager()

    print("\n✓ All tests passed! Core functionality is working correctly.")

if __name__ == "__main__":
    main()