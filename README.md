# Integri-Spy

**Integri-Spy** is a Python-based File Integrity Monitoring (FIM) tool designed to track changes to critical files. By generating a baseline of file hashes, Integri-Spy can detect unauthorized modifications, deletions, and additions to monitored files. All changes are logged, providing an audit trail for security monitoring.

## Features

- Generates a baseline of SHA-256 hashes for critical files.
- Detects file changes, deletions, and additions by comparing against the baseline.
- Logs all changes, including mismatches, missing files, and new files detected in the monitored list.
- Configurable to monitor custom lists of files.

## Project Structure

```plaintext
.
├── src
│   ├── Integri-Spy.py            # Main script to monitor changes in files
│   ├── baseline_generator.py      # Script to create the initial baseline of file hashes
│   └── is_functionality.py        # Core functions for hash generation, loading baseline, and monitoring list
├── config
│   └── monitoring_list.txt        # List of file paths to be monitored
├── baseline.json                  # Baseline file containing original file hashes (generated)
└── logs
    └── monitor_log.txt            # Log file where detected changes are recorded
```

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TheMuslimHacker/Integri-Spy.git
   cd Integri-Spy
   ```

2. Install required packages (if any additional dependencies are added).

3. Set up the monitoring list:

   - Add paths to the files you want to monitor in `config/monitoring_list.txt`, with one file path per line. Example:
     ```
     /etc/passwd
     /etc/hosts
     /path/to/other/important/file
     ```

## Usage

### Step 1: Generate the Initial Baseline

To create the baseline file (`baseline.json`), which stores the initial hash values of each file, run:

```bash
python3 src/baseline_generator.py
```

This script will read each file listed in `monitoring_list.txt`, generate SHA-256 hashes, and save these hashes in `baseline.json`.

### Step 2: Monitor Changes

Once the baseline is created, run the monitoring script to check for file changes:

```bash
python3 src/Integri-Spy.py
```

The script will:
- Load the baseline and monitoring list.
- Check each file in the monitoring list:
  - Log a warning if the hash does not match the baseline (indicating a change).
  - Log if a file is missing or if a new file is detected.
- Re-run the baseline generator automatically if a new file is detected.

### Logs

All detected changes are recorded in `logs/monitor_log.txt`, including:
- Timestamps
- File paths
- Type of change (e.g., hash mismatch, missing file, or new file detected).

Example log entry:

```
2024-10-24 14:55:30,120 - WARNING - Change detected in /etc/passwd: hash mismatch.
2024-10-24 14:55:31,110 - INFO - New file detected: /path/to/new/file
```

## Code Overview

### `Integri-Spy.py`

This is the main script for monitoring file changes. It:
- Loads the baseline and monitoring list.
- Compares each file’s hash to its baseline hash.
- Logs any mismatches, missing files, or new files.

### `baseline_generator.py`

This script generates the baseline of file hashes and stores them in `baseline.json`. Run this script initially and any time the monitored files change significantly.

### `is_functionality.py`

Contains helper functions:
- `load_baseline()`: Loads baseline hashes from `baseline.json`.
- `load_monitoring_list()`: Loads the file paths to be monitored from `monitoring_list.txt`.
- `generate_hash(filepath)`: Generates a SHA-256 hash of a file’s contents.
- `create_baseline()`: Creates the baseline file with initial hashes for all monitored files.

## Troubleshooting

- **Baseline file not found**: Ensure `baseline_generator.py` has been run at least once to create `baseline.json`.
- **Missing monitoring list**: Ensure `monitoring_list.txt` exists in the `config` directory with paths of files to monitor.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License.
