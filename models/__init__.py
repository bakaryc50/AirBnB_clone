#!/usr/bin/python3
""" creates a unique FileStorage instance for the application """
import models
from . engine.file_storage import FileStorage


storage = FileStorage()

storage.reload()
