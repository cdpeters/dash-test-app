#!/bin/bash

# The following script runs development tools such as code formatters, docstring
# coverage, linting, and type checking on project files such as jupyter
# notebooks (.ipynb), python files (.py) and markdown files (.md). The default
# behavior is to run all of the tools jupyter notebooks (except for the markdown
# code block formatting tool blacken-docs when it is used on markdown files).

# Main variables ---------------------------------------------------------------
# Get the name of the current directory
current_dir=$(basename "$(pwd)")

# Assign the names of the project and app directories
project_dir="dash-test-app"

nb_app_dir="notebooks"
py_app_dir="src"

# Colors for printing
cyan='\033[0;36m'
purple='\033[0;35m'
blue='\033[0;34m'
yellow='\033[0;33m'
bcyan='\033[1;36m'
color_off='\033[0m'

# Array of current tools that can be applied to jupyter notebooks and python
# (.ipynb and .py) files. Note that the markdown code block formatter
# blacken-docs is not included because it is handled separately using the
# -md|--markdown option.
current_tools=("black" "isort" "interrogate" "flake8" "mypy")

# Array of tools that will be run, subject to any tool that is skipped or
# any markdown file that needs formatting.
tools_to_run=()

# Markdown option variables ----------------------------------------------------
# Booleans to indicate if markdown or markdown-only formatting has been
# requested.
markdown=false
markdown_only=false

# Array that holds all the arguments to the -md|--markdown|-mdo|--markdown-only
# option. This array will only consist of valid files using the "-f" command
# which checks if a file exists and is not a directory.
md_files=()

# Array that collects the options what were passed in.
options_called=()

# The set of options that conflict with the -mdo|--markdown-only option.
mdo_conflict_options=("-s" "--skip" "-t" "--type")

# The set of options gathered from options_called that are in the set of
# conflict options (mdo_conflict_options) and thus will be ignored due to
# -mdo|--markdown-only being passed in.
options_for_warning=()

# Skip option variables --------------------------------------------------------
# Array that holds all the arguments to the -s|--skip option.
skip_args=()

# Type option variables --------------------------------------------------------
# File type to run tools on where "nb" stands for notebook (.ipynb). The default
# behavior is to run the tools only on jupyter notebooks unless the -t|--type
# option is specified.
file_type="nb"

# Array that holds all the arguments to the -t|--type option.
type_args=()

# End of variables -------------------------------------------------------------


# $# is number of arguments at run time.
# While there are still args left to be processed.
while [ $# -gt 0 ]; do
  option="$1"
  options_called+=("$1")
  # Throw out the value thereby reducing number of args left to be processed.
  shift
  case "$option" in
    -md|--markdown|-mdo|--markdown-only)
      # Error checking ---------------------------------------------------------
      # Check if a markdown file(s) was provided.
      if [[ $# -eq 0 || "$1" =~ ^(-|--) ]]; then
        echo
        echo "Error: No markdown file(s) provided to \"${option}\". Please provide a"
        echo "markdown file(s) as an argument."
        echo
        exit 1
      fi

      # Check if two markdown options were passed in.
      if [[ "$markdown" = true || "$markdown_only" = true ]]; then
        echo
        echo "Error: Two markdown options were used at the same time. Only pass in one"
        echo "markdown option at a time."
        echo
        exit 1
      fi

      # Markdown Option Processing ---------------------------------------------
      # Determine which markdown option was passed in and update its boolean.
      if [[ " $option " =~ ( -md | --markdown ) ]]; then
        markdown=true
      else
        markdown_only=true
      fi

      # Add the markdown files to the md_files array up until there are no more
      # args or you reach the next cli option.
      for i in "$@"; do
        # Break if you reach a cli option.
        if [[ "$i" =~ ^(-|--) ]]; then
          break
        fi
        # Check if the file passed in is a valid file (exists and is not a
        # directory).
        if [[ -f "$i" ]]; then
          md_files+=("$i")
          shift
        else
          echo
          echo "Error: The following argument is not a valid file (it is either a directory or"
          echo "it doesn't exist):"
          echo "  ${i}"
          echo
          exit 1
        fi
      done
      ;;

    -s|--skip)
      # Error Checking ---------------------------------------------------------
      # Check if a tool name(s) was provided.
      if [[ $# -eq 0 || "$1" =~ ^(-|--) ]]; then
        echo
        echo "Error: No tool name(s) provided to \"${option}\". Please provide a tool name(s) as"
        echo "an argument."
        echo
        exit 1
      fi

      # Skip Option Processing -------------------------------------------------
      # Add the tool names to the skip_args array up until there are no more
      # args or you reach the next cli option.
      for i in "$@"; do
        # Break if you reach a cli option.
        if [[ "$i" =~ ^(-|--) ]]; then
          break
        fi
        skip_args+=("$i")
        shift
      done

      # Add a tool from the array of current tools to the array of tools_to_run
      # if it is not a tool name found in the skip_args array.
      for tool in "${current_tools[@]}"; do
        [[ ! " ${skip_args[*]} " =~ " $tool " ]] && tools_to_run+=("$tool")
      done
      ;;

    -t|--type)
      # Error Checking ---------------------------------------------------------
      # Check if a type was provided.
      if [[ $# -eq 0 || "$1" =~ ^(-|--) ]]; then
        echo
        echo "Error: No type provided to \"${option}\". Please provide py|all as an argument."
        echo
        exit 1
      fi

      # Type Option Processing -------------------------------------------------
      # Add the type to the type_args array up until there are no more args or
      # you reach the next cli option. Since only 1 type should be passed in
      # (and it must be py|all), error checking must handle the case of too many
      # args passed to -t|--type.
      for i in "$@"; do
        # Break if you reach a cli option.
        if [[ "$i" =~ ^(-|--) ]]; then
          break
        fi
        type_args+=("$i")
        shift
        if [[ ${#type_args[@]} -gt 1 ]]; then
          echo
          echo "Error: Too many arguments supplied to \"${option}\". Please provide only py|all as"
          echo "an argument."
          echo
          exit 1
        fi
      done

      # Update the type variable with arg passed in.
      if [[ " ${type_args[0]} " =~ " py " ]]; then
        file_type="py"
      elif [[ " ${type_args[0]} " =~ " all " ]]; then
        file_type="all"
      else
        echo
        echo "Error: Argument to -t|--type must be either py|all."
        echo
        exit 1
      fi
      ;;

    -h|--help)
      echo
      echo "-------------------------------  tools.sh Help  -------------------------------"
      echo
      echo "tools.sh runs development tools on jupyter notebooks (.ipynb) only by default."
      echo "CLI options allow for running these tools on python and markdown files as well"
      echo "as skipping any of the tools if needed."
      echo
      echo
      echo "Current Tools In Use:"
      echo
      echo "         black: code formatter"
      echo "  blacken-docs: code formatter for markdown code blocks. Not run by default,"
      echo "                see the -md|--markdown or -mdo|--markdown-only cli options."
      echo "         isort: import formatter"
      echo "   interrogate: docstring coverage"
      echo "        flake8: linter"
      echo "          mypy: type checker"
      echo
      echo
      echo "Available CLI Options:"
      echo
      echo "  -h|--help"
      echo "      Provides a list of cli options."
      echo
      echo "  -md|--markdown <markdown_file>"
      echo "      Runs blacken-docs on <markdown_file> to format code blocks within."
      echo
      echo "  -mdo|--markdown-only <markdown_file>"
      echo "      ONLY runs blacken-docs on <markdown_file> to format code blocks within."
      echo "      No other tools are run."
      echo
      echo "  -s|--skip <tool_name>"
      echo "      Skips application of the <tool_name>'s provided."
      echo
      echo "  -t|--type (all|py)"
      echo "      all"
      echo "          Runs tools on both jupyter notebooks and python files (.ipynb and"
      echo "          .py)."
      echo "      py"
      echo "          Runs tools on python files (.py) only."
      echo
      exit 0
      ;;

    *)
      echo
      echo "Error: The following argument is not a valid cli option:"
      echo "  ${option}"
      echo
      echo "Use -h|--help to see a list of valid options."
      echo
      exit 1
      ;;

  esac
done

# If -mdo|--markdown-only was passed in, gather any conflicting options that
# were also passed in.
for conflict_option in "${mdo_conflict_options[@]}"; do
  if [[ "$markdown_only" = true && " ${options_called[*]} " =~ " $conflict_option " ]]; then
    options_for_warning+=("$conflict_option")
  fi
done

# If the previous code block produced a non-empty options_for_warning array,
# warn the user that options that conflict with markdown-only will be ignored.
if [[ ${#options_for_warning[@]} -gt 0 ]]; then
  echo
  echo "Warning: The markdown-only option was passed in. The following option(s) will"
  echo "be ignored:"
  for i in "${options_for_warning[@]}"; do
    echo "  $i"
  done
  echo
fi

# Update tools_to_run based on either no arguments passed in when the script is
# run or any markdown options that were passed in.
if [[ "$markdown_only" = true ]]; then
  file_type="mdo"
  # The entire array becomes only the blacken-docs tool.
  tools_to_run=("blacken-docs")
elif [[ ${#tools_to_run[@]} -eq 0 ]]; then
  # If tools_to_run was empty then no tools are skipped.
  tools_to_run=("${current_tools[@]}")
  if [[ "$markdown" = true ]]; then
    tools_to_run+=("blacken-docs")
  fi
else
  # tools_to_run is non-empty meaning a tool(s) is skipped.
  if [[ "$markdown" = true ]]; then
    tools_to_run+=("blacken-docs")
  fi
fi

# Print out the dev tools header based on the file_type value.
case "$file_type" in
  all)
    echo -e "${cyan}==== ${bcyan}DEV TOOLS for Both Jupyter Notebooks (.ipynb) and Python Files (.py)${cyan} ====${color_off}"
    ;;

  mdo)
    echo -e "${cyan}====================== ${bcyan}DEV TOOL for Markdown-Only (.md)${cyan} ======================${color_off}"
    ;;

  nb)
    echo -e "${cyan}================== ${bcyan}DEV TOOLS for Jupyter Notebooks (.ipynb)${cyan} ==================${color_off}"
    ;;

  py)
    echo -e "${cyan}====================== ${bcyan}DEV TOOLS for Python Files (.py)${cyan} ======================${color_off}"
    ;;

esac

# Run the tools based on the tools_to_run array and the file_type value.
for i in ${tools_to_run[@]}; do
  case "$i" in
    black)
      if [[ $file_type == "all" ]]; then
        echo
        echo -e "${purple}(on python files)${cyan} Running ${bcyan}black${cyan} (code formatter):${color_off}"
        black .

        echo
        echo -e "${yellow}(on jupyter files)${cyan} Running ${bcyan}black${cyan} (code formatter):${color_off}"
        nbqa black .

        echo
        echo -e "${yellow}(on jupyter files)${cyan} Running ${bcyan}blacken-docs${cyan} (markdown code block formatter):${color_off}"
        nbqa blacken-docs .

      elif [[ $file_type == "nb" ]]; then
        echo
        echo -e "${yellow}(on jupyter files)${cyan} Running ${bcyan}black${cyan} (code formatter):${color_off}"
        nbqa black .

        echo
        echo -e "${yellow}(on jupyter files)${cyan} Running ${bcyan}blacken-docs${cyan} (markdown code block formatter):${color_off}"
        nbqa blacken-docs .

      elif [[ $file_type == "py" ]]; then
        echo
        echo -e "${purple}(on python files)${cyan} Running ${bcyan}black${cyan} (code formatter):${color_off}"
        black .

      fi
      ;;

    isort)
      if [[ $file_type == "all" ]]; then
        echo
        echo -e "${purple}(on python files)${cyan} Running ${bcyan}isort${cyan} (import formatter):${color_off}"
        isort .

        echo
        echo -e "${yellow}(on jupyter files)${cyan} Running ${bcyan}isort${cyan} (import formatter):${color_off}"
        nbqa isort .

      elif [[ $file_type == "nb" ]]; then
        echo
        echo -e "${yellow}(on jupyter files)${cyan} Running ${bcyan}isort${cyan} (import formatter):${color_off}"
        nbqa isort .

      elif [[ $file_type == "py" ]]; then
        echo
        echo -e "${purple}(on python files)${cyan} Running ${bcyan}isort${cyan} (import formatter):${color_off}"
        isort .

      fi
      ;;

    interrogate)
      if [[ $file_type == "all" ]]; then
        echo
        echo -e "${purple}(on python files)${cyan} Running ${bcyan}interrogate${cyan} (docstring coverage):${color_off}"
        interrogate .

        echo
        echo -e "${yellow}(on jupyter files)${cyan} Running ${bcyan}interrogate${cyan} (docstring coverage):${color_off}"
        nbqa interrogate .

      elif [[ $file_type == "nb" ]]; then
        echo
        echo -e "${yellow}(on jupyter files)${cyan} Running ${bcyan}interrogate${cyan} (docstring coverage):${color_off}"
        nbqa interrogate .
      elif [[ $file_type == "py" ]]; then
        echo
        echo -e "${purple}(on python files)${cyan} Running ${bcyan}interrogate${cyan} (docstring coverage):${color_off}"
        interrogate .

      fi
      ;;

    flake8)
      if [[ $file_type == "all" ]]; then
        echo
        echo -e "${purple}(on python files)${cyan} Running ${bcyan}flake8${cyan} (code linter):${color_off}"
        flake8 .

        echo
        echo -e "${yellow}(on jupyter files)${cyan} Running ${bcyan}flake8${cyan} (code linter):${color_off}"
        nbqa flake8 .

      elif [[ $file_type == "nb" ]]; then
        echo
        echo -e "${yellow}(on jupyter files)${cyan} Running ${bcyan}flake8${cyan} (code linter):${color_off}"
        nbqa flake8 .

      elif [[ $file_type == "py" ]]; then
        echo
        echo -e "${purple}(on python files)${cyan} Running ${bcyan}flake8${cyan} (code linter):${color_off}"
        flake8 .

      fi
      ;;

    mypy)
      if [[ $file_type == "all" ]]; then
        echo
        echo -e "${purple}(on python files)${cyan} Running ${bcyan}mypy${cyan} (type checker):${color_off}"
        # Adjust the target and pass in the config file path based on the
        # directory this script is run in.
        if [ $current_dir = $project_dir ]; then
            mypy ./src --config-file="./pyproject.toml"
        elif [ $current_dir = $py_app_dir ]; then
            mypy . --config-file="../pyproject.toml"
        fi

        echo
        echo -e "${yellow}(on jupyter files)${cyan} Running ${bcyan}mypy${cyan} (type checker):${color_off}"
        if [ $current_dir = $project_dir ]; then
            nbqa mypy ./notebooks --config-file="./pyproject.toml"
        elif [ $current_dir = $nb_app_dir ]; then
            nbqa mypy . --config-file="../pyproject.toml"
        fi

      elif [[ $file_type == "nb" ]]; then
        echo
        echo -e "${yellow}(on jupyter files)${cyan} Running ${bcyan}mypy${cyan} (type checker):${color_off}"
        if [ $current_dir = $project_dir ]; then
            nbqa mypy ./notebooks --config-file="./pyproject.toml"
        elif [ $current_dir = $nb_app_dir ]; then
            nbqa mypy . --config-file="../pyproject.toml"
        fi

      elif [[ $file_type == "py" ]]; then
        echo
        echo -e "${purple}(on python files)${cyan} Running ${bcyan}mypy${cyan} (type checker):${color_off}"
        if [ $current_dir = $project_dir ]; then
            mypy ./src --config-file="./pyproject.toml"
        elif [ $current_dir = $py_app_dir ]; then
            mypy . --config-file="../pyproject.toml"
        fi

      fi
      ;;

    blacken-docs)
      echo
      echo -e "${blue}(on markdown files)${cyan} Running ${bcyan}blacken-docs${cyan} (markdown code block formatter):${color_off}"
      blacken-docs ${md_files[*]}
      ;;

  esac
done

echo
echo -e "${cyan}=========================== ${bcyan}DEV TOOLS NOW COMPLETE${cyan} ===========================${color_off}"
