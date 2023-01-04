#!/bin/bash

# Get the name of the current directory
current_dir=$(basename "$(pwd)")
# Assign the names of the project and app directories
project_dir="dash-test-app"
app_dir="notebooks"

# Colors for printing
cyan='\033[0;36m'
bcyan='\033[1;36m'
color_off='\033[0m'

echo -e "${cyan}====== ${bcyan}DEV TOOLS for Jupyter Notebooks (.ipynb)${cyan} ======${color_off}"
echo

# Code formatter: black
echo -e "${cyan}Running ${bcyan}black${cyan} (code formatter):${color_off}"

nbqa black .

# Markdown code block formatter: blacken-docs
echo
echo -e "${cyan}Running ${bcyan}blacken-docs${cyan} (markdown code block formatter):${color_off}"

nbqa blacken-docs .

# Import formatter: isort
echo
echo -e "${cyan}Running ${bcyan}isort${cyan} (import formatter):${color_off}"

nbqa isort .

# Docstring Existence Checker: interrogate
# Use `--ignore-module` to avoid checking for docstrings at the module level.
echo
echo -e "${cyan}Running ${bcyan}interrogate${cyan} (check docstrings exist):${color_off}"

nbqa interrogate .

# Code linter: flake8
# Ignore code `D100` which checks for docstrings at the module level.
echo
echo -e "${cyan}Running ${bcyan}flake8${cyan} (code linter):${color_off}"

nbqa flake8 .

# Type checker: mypy
echo
echo -e "${cyan}Running ${bcyan}mypy${cyan} (type checker):${color_off}"

if [ $current_dir = $project_dir ]; then
    nbqa mypy ./notebooks --config-file="./pyproject.toml"
elif [ $current_dir = $app_dir ]; then
    nbqa mypy . --config-file="../pyproject.toml"
fi

echo
echo -e "${cyan}=============== ${bcyan}DEV TOOLS NOW COMPLETE${cyan} ===============${color_off}"
