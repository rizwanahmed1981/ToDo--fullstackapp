"""
Evolution of Todo - Data models
Defines the Task dataclass for the application
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single task in the todo application.

    Attributes:
        id: Unique identifier for the task
        title: Title of the task
        description: Detailed description of the task
        status: Status of the task ('Pending' or 'Completed')
    """
    id: int
    title: str
    description: str
    status: str = "Pending"