#!/usr/bin/env python3
"""
Direct launcher for Evolution of Todo application that avoids import issues
"""
import sys
import os

# Ensure we're in the correct directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Add current directory to Python path
sys.path.insert(0, '.')

try:
    from src.main import main
    main()
except ImportError as e:
    print(f"Import error: {e}")
    print("Trying alternative import...")

    # Alternative approach - directly import and run
    try:
        import src.main
        src.main.main()
    except Exception as e2:
        print(f"Alternative import also failed: {e2}")
        sys.exit(1)
except Exception as e:
    print(f"Runtime error: {e}")
    sys.exit(1)