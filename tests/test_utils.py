import pytest
from io import StringIO
import sys
from stc_ml_test.utils import hello_world


def test_hello_world(capsys):
    """Test that hello_world function prints the expected message."""
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"


def test_hello_world_returns_none():
    """Test that hello_world function returns None."""
    result = hello_world()
    assert result is None
