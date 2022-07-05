"""This module provides the RP To-Do model-controller."""
# rptodo/rptodo.py

from pathlib import Path
from typing import Any, Dict, NamedTuple

from rptodo.database import DatabaseHandler

class CurrentTodo(NamedTuple):
    """This class define the current to-do object."""
    todo: Dict[str, Any]
    error: int
    
    
class Todoer:
    """Controller that connects application logic with database."""
    def __init__(self, db_path: Path) -> None:
        self.db_handler = DatabaseHandler(db_path)