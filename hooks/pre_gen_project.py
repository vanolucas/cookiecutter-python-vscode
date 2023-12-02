import logging
import re
import sys


MODULE_NAME_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = "{{ cookiecutter.project_slug }}"

if not re.match(MODULE_NAME_REGEX, module_name):
    logging.error(f"The project slug `{module_name}` is not a valid Python module name.")
    sys.exit(1)
