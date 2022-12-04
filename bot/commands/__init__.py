"""export commands"""
# iterate over all files in the current directory
# and import all modules expect this one
# and add them to the command_handlers dict

from pathlib import Path
from importlib import import_module

command_handlers = {}

for file in Path(__file__).parent.glob("*.py"):
    if file.name == "__init__.py":
        continue

    module = import_module(f"bot.commands.{file.stem}")
    command_handlers[file.stem] = getattr(module, file.stem)
