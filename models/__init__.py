#!/usr/bin/python3
"""__init__ method for models package, or
Module for FileStorage initialization."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
