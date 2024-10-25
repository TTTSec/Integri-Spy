import os
import logging
from is_functionality import load_baseline, load_monitoring_list, generate_hash, create_baseline

# Logging configuration at the start of the script
log_file_path = os.path.join(os.path.dirname(__file__), "..", "logs", "monitor_log.txt")
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def monitor_changes():
    """Monitors file changes against the baseline and logs detected issues."""

    logging.info("Starting file integrity monitoring...")

    baseline_data = load_baseline()
    if baseline_data == {}:
        exit()


    monitoring_list = load_monitoring_list()
    if monitoring_list == []:
        exit()


    for filepath in monitoring_list:
        if filepath in baseline_data:
            if os.path.exists(filepath):
                try:
                    current_hash = generate_hash(filepath)
                    if current_hash != baseline_data[filepath]:
                        logging.warning(f"Change detected in {filepath}: hash mismatch.")
                except Exception as e:
                    logging.error(f"Error accessing {filepath}: {e}")
            else:
                logging.warning(f"File missing: {filepath}.")
        else:
            logging.info(f"New file detected: {filepath}, please, make sure it is supposed to be there and re-run the baseline_generator.py")


    logging.info("File integrity monitoring completed.")


if __name__ == '__main__':
    monitor_changes()
