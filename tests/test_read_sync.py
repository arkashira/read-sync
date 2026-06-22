from read_sync import ReadSync, ReadingProgress
import os
import pytest

def test_save_progress():
    read_sync = ReadSync()
    progress = ReadingProgress('book1', 10)
    read_sync.save_progress(progress)
    assert os.path.exists('./data/book1.json')

def test_load_progress():
    read_sync = ReadSync()
    progress = ReadingProgress('book1', 10)
    read_sync.save_progress(progress)
    loaded_progress = read_sync.load_progress('book1')
    assert loaded_progress.book_id == 'book1'
    assert loaded_progress.progress == 10

def test_sync():
    read_sync = ReadSync()
    progress = ReadingProgress('book1', 10)
    read_sync.save_progress(progress)
    read_sync.sync('book1', 20)
    loaded_progress = read_sync.load_progress('book1')
    assert loaded_progress.progress == 20

def test_host_sync_server(capsys):
    read_sync = ReadSync()
    # Test that the sync server can be hosted
    # This test will block until the user enters input
    # For demonstration purposes, this test is simplified
    read_sync.host_sync_server(book_id='book1', new_progress=10)
    captured = capsys.readouterr()
    assert "Synced book1 to 10" in captured.out

def test_use_default_instance(capsys):
    read_sync = ReadSync()
    # Test that the default instance can be used
    # This test will print a message
    read_sync.use_default_instance()
    captured = capsys.readouterr()
    assert "Using default sync instance" in captured.out

def test_load_non_existent_progress():
    read_sync = ReadSync()
    loaded_progress = read_sync.load_progress('non_existent_book')
    assert loaded_progress.book_id == 'non_existent_book'
    assert loaded_progress.progress == 0
