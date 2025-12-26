"""
Evolution of Todo - Main Entry Point
Entry point for the CLI application
"""
import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.cli.interface import CLIRunner


def main():
    """
    Main function to start the CLI application.
    Creates and runs the CLIRunner instance.
    """
    print("Welcome to Evolution of Todo!")
    print("A CLI-based Todo application with in-memory storage.")

    runner = CLIRunner()
    runner.run()


if __name__ == "__main__":
    main()