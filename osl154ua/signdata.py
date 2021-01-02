import os
import pathlib
from . import utils

def list_signs():
    root = pathlib.Path(".", "signs")
    print("Available signs:")
    for d in root.iterdir():
        print(f" * {d.name}")

def add_sign_data(name, server, tag, width, height):
    utils.create_sign_data(name, server, tag, width, height, {})
