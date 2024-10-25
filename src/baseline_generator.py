from is_functionality import create_baseline  # Import the create_baseline function from is_functionality.py

try:
    print("Starting baseline creation...")
    create_baseline()
    print("Baseline created successfully.")
except Exception as e:
    print(f"An error occurred during baseline creation: {e}")