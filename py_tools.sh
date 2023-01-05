#!/bin/bash

# The following script runs development tools such as code formatters, docstring
# coverage, linting, and type checking on python files (.py) only.

# Get the name of the current directory
current_dir=$(basename "$(pwd)")
# Assign the names of the project and app directories
project_dir="dash-test-app"
app_dir="src"

# Colors for printing
cyan='\033[0;36m'
bcyan='\033[1;36m'
color_off='\033[0m'

echo -e "${cyan}========== ${bcyan}DEV TOOLS for Python Files (.py)${cyan} ==========${color_off}"
echo

# Code formatter: black
echo -e "${cyan}Running ${bcyan}black${cyan} (code formatter):${color_off}"

black .

# Import formatter: isort
echo
echo -e "${cyan}Running ${bcyan}isort${cyan} (import formatter):${color_off}"

isort .

# Docstring Coverage: interrogate
echo
echo -e "${cyan}Running ${bcyan}interrogate${cyan} (docstring coverage):${color_off}"

interrogate .

# Code linter: flake 8
echo
echo -e "${cyan}Running ${bcyan}flake8${cyan} (code linter):${color_off}"

flake8 .

# Type checker: mypy
echo
echo -e "${cyan}Running ${bcyan}mypy${cyan} (type checker):${color_off}"

if [ $current_dir = $project_dir ]; then
    mypy ./src --config-file="./pyproject.toml"
elif [ $current_dir = $app_dir ]; then
    mypy . --config-file="../pyproject.toml"
fi

echo
echo -e "${cyan}=============== ${bcyan}DEV TOOLS NOW COMPLETE${cyan} ===============${color_off}"
