# Read Sync

A simple systemd service file generator for read-sync.

## Usage

1. Install the package using pip: `pip install .`
2. Run the script using: `python -m systemd_service --name read-sync --description "Read sync service" --executable /usr/bin/read-sync --log_file /var/log/read-sync/daemon.log`
