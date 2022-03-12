""" testing history class """
import pytest
from calculator.history import History
from calculator.calculation import Addition

def test_history_instance():
    """ testing the history instance """
    history = History()
    assert isinstance(history, History)

def test_history_add_item():
