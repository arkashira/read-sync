import argparse
import json
import os
from dataclasses import dataclass

@dataclass
class SystemdService:
    name: str
    description: str
    executable: str
    log_file: str

    def generate_unit_file(self):
        unit_file = f"""
        [Unit]
        Description={self.description}
        After=network.target

        [Service]
        User=root
        ExecStart={self.executable}
        Restart=always
        StandardOutput=syslog
        StandardError=syslog
        SyslogIdentifier={self.name}

        [Install]
        WantedBy=multi-user.target
        """
        return unit_file

    def write_unit_file(self, file_path):
        with open(file_path, 'w') as f:
            f.write(self.generate_unit_file())

    def start_service(self):
        os.system(f"systemctl start {self.name}")

    def enable_service(self):
        os.system(f"systemctl enable {self.name}")

def main():
    parser = argparse.ArgumentParser(description='Generate and start systemd service')
    parser.add_argument('--name', help='Service name')
    parser.add_argument('--description', help='Service description')
    parser.add_argument('--executable', help='Path to executable')
    parser.add_argument('--log_file', help='Path to log file')
    args = parser.parse_args()

    service = SystemdService(args.name, args.description, args.executable, args.log_file)
    service.write_unit_file(f"/etc/systemd/system/{args.name}.service")
    service.start_service()
    service.enable_service()

if __name__ == "__main__":
    main()
