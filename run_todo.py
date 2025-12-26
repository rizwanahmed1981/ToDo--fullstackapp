#!/usr/bin/env python3
"""
Simple launcher for Evolution of Todo application
"""
import sys
import os

# Ensure we're in the project root
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Now import and run the application
try:
    from src.main import main
    main()
except Exception as e:
    print(f"Error running application: {e}")
    sys.exit(1)