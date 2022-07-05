"""This module provides the RP To-Do model-controller."""
# rptodo/rptodo.py

from typing import Any, Dict, NamedTuple

class CurrentTodo(NamedTuple):
    """This class define the current to-do object."""
    todo: Dict[str, Any]
    error: int