import pytest
from src.systemd_service import SystemdService
import tempfile
import os

def test_generate_unit_file():
    service = SystemdService("read-sync", "Read sync service", "/usr/bin/read-sync", "/var/log/read-sync/daemon.log")
    unit_file = service.generate_unit_file()
    assert "[Unit]" in unit_file
    assert "[Service]" in unit_file
    assert "[Install]" in unit_file

def test_write_unit_file():
    service = SystemdService("read-sync", "Read sync service", "/usr/bin/read-sync", "/var/log/read-sync/daemon.log")
    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = os.path.join(tmp_dir, "read-sync.service")
        service.write_unit_file(file_path)
        assert os.path.exists(file_path)

def test_start_service():
    service = SystemdService("read-sync", "Read sync service", "/usr/bin/read-sync", "/var/log/read-sync/daemon.log")
    # Mock the os.system call
    import unittest.mock as mock
    with mock.patch('os.system') as mock_system:
        service.start_service()
        mock_system.assert_called_once()

def test_enable_service():
    service = SystemdService("read-sync", "Read sync service", "/usr/bin/read-sync", "/var/log/read-sync/daemon.log")
    # Mock the os.system call
    import unittest.mock as mock
    with mock.patch('os.system') as mock_system:
        service.enable_service()
        mock_system.assert_called_once()
