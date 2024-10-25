import os
import json
import logging
import hashlib

def load_baseline():
    """Load baseline data from baseline.json for integrity checks."""
    baseline_file_path = os.path.join(os.path.dirname(__file__), "..", "baseline.json")
    try:
        with open(baseline_file_path, 'r') as baseline_file:
            return json.load(baseline_file)
    except FileNotFoundError:
        logging.error("Baseline file not found. Please generate a new baseline.")
        return {}
    except json.JSONDecodeError:
        logging.error("Error reading baseline JSON file.")
        return {}

def load_monitoring_list():
    """Load list of files to monitor from monitoring_list.txt."""
    filepath = os.path.join(os.path.dirname(__file__), "..", "config", "monitoring_list.txt")
    if not os.path.exists(filepath):
        logging.error("Monitoring list file not found.")
        return []
    with open(filepath, "r") as file:
        return [line.strip() for line in file if line.strip()]

def generate_hash(filepath):
    """Generate SHA-256 hash for a given file."""
    try:
        with open(filepath, 'rb') as file:
            return hashlib.sha256(file.read()).hexdigest()
    except Exception as e:
        logging.error(f"Could not hash {filepath}: {e}")
        return None

def create_baseline():
    """Create a baseline of file hashes for integrity monitoring."""
    baseline_data = {}
    files_to_monitor = load_monitoring_list()
    for filepath in files_to_monitor:
        if os.path.exists(filepath):
            file_hash = generate_hash(filepath)
            if file_hash:
                baseline_data[filepath] = file_hash
                
        else:
            logging.warning(f"{filepath} does not exist and will be skipped.")
    baseline_file_path = os.path.join(os.path.dirname(__file__), "..", "baseline.json")
    with open(baseline_file_path, 'w') as baseline_file:
        json.dump(baseline_data, baseline_file, indent=4)
