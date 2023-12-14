import logging
import re
import sys


def validate_module_name(cookiecutter_var_name: str, value: str) -> None:
    MODULE_NAME_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
    if not re.match(MODULE_NAME_REGEX, value):
        logging.error(
            f"`{value}` is not a valid Python module name for "
            f"cookiecutter variable `{cookiecutter_var_name}`."
        )
        sys.exit(1)
