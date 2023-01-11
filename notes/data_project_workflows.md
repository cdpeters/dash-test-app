---
title: Data Project Workflows
created: 2022-11-30T01:30:55.417Z
modified: 2022-11-30T02:53:04.577Z
---

# Data Project Workflows

- The following commands can be executed multiple times as needed for a given project

### Common Workflows
- Adding/removing packages
- Updating environment when `environment.yml` changes
- Updating environment when `pyproject.toml` changes
- Update `environment.yml` when `conda` packages are added
- Running the code formatter/linter/docstring script

### Adding/Removing Packages
- `pip` packages are preferred over `conda` packages. Only install `conda` packages if there is no `pip` equivalent
- Add packages:
	```shell
	poetry add <package_name>=<version_constraint>
	```
	- the `version_constraint` is optional
	- use this command in place of `pip install <package_name>=<version_constraint>`

- Add packages to a group (for an explanation of groups and to create a group, see the section below called "Dependency Groups Within `pyproject.toml`"):
	```shell
	poetry add <package_name>=<version_constraint> --group <group_name>
	```
	> For how to specify version constraints, see the "Version constraints" section of Poetry's [dependency specification](https://python-poetry.org/docs/dependency-specification/)
- Remove packages:
	```shell
	poetry remove <package_name>
	```

### Updating environment when `environment.yml` changes
**This creates a new environment, update this with proper way to update the environment**
```shell
conda env create -f environment.yml
```

### Updating environment when `pyproject.toml` changes
- To install dependencies when there has been a change to the `poetry.lock` file (i.e. when we add a new package(s) to the `pyproject.toml` file):
	```shell
	poetry install
	```

### Update `environment.yml` when `conda` packages are added
```shell
conda env export --from-history | grep -v "^prefix: " > environment.yml
```

### Running the code formatter/linter/docstring script `dev_tools.sh`
- this script will act on files in the directory it is being run in **and** all files in sub-directories recursively:
```shell
bash <relative_path_to_script>/dev_tools.sh
```





### Dependency Groups Within `pyproject.toml`
- Think of dependency groups as labels associated with your dependencies, they are simply a way to organize the dependencies logically
- The main dependency group is the section with the heading `[tool.poetry.dependencies]`, all dependencies that are needed to **run** the project must be here
- Other dependency groups (ones that you add yourself) must only contain dependencies you need for development of the project (things like formatters, linters, unit testing libraries, etc.)
- Add a dependency group by editing the `pyproject.toml` file directly, follow the following format which adds a heading:
	```toml
	[tool.poetry.group.<group_name>.dependencies]
	```
- If the plan is to leave the development dependencies in one all encompassing group, a common group name would be `dev`, see the example `pyproject.toml` code block below. Otherwise, you could separate the development dependencies into however many groups that you want. Poetry even allows for installing or synchronizing by groups, so multiple groups for different purposes could be useful


### Example `pyproject.toml`
- The required fields below get set when `poetry init` is called during project setup but can also be modified afterwards by editing `pyproject.toml` directly
- If there is a `packages` attribute in the `[tool.poetry]` section, remove it. These projects will not be packages

```toml
[tool.poetry]
name = "dash-test" # Required (non-null)
version = "0.1.0" # Required (non-null)
description = "" # Required (non-null)
authors = ["Chris Peterson <cdpeters1@gmail.com>"] # Required
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.9"
dash = "^2.7.0"
ibis-framework = { version = "^3.2.0", python = ">=3.9,<3.11" }

[tool.poetry.group.dev.dependencies]
pytest = "^6.0.0"
pytest-mock = "*"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```


### Overall Steps

#### Once
1. Install Anaconda
1. Install python from [www.python.org](https://www.python.org/)
1. Install poetry globally via script

#### Once Per project
1. Set up Repo
1. Create conda environment and activate it
1. Initialize poetry
1. Remove packages field from the `[tool.poetry]` section of `pyproject.toml`

#### Multiple Times Per Project
1. Activate the conda environment
1. Add/Update/Remove packages
1. Create/Update conda-packages specific `environments.yml`
1. Run `poetry check` to check `pyprojects.toml` and some version of `poetry lock` to lock `poetry.lock`
1. If the any of the 3 dependency/environment files change, run `conda env create...` and `poetry install`


### Reasons for a Conda + Poetry Setup
- "freeze" type approaches require more manual upkeep of the dependencies file. 2 dependency files (non lock files) need to be maintained, one for "production" and one for development
- if a project uses conda and you plan to host it online as a website there are fewer hosting services with conda buildpacks (the software that sets up the environment to run your website on a cloud server)
- pypi packages (installed via poetry) are often more up-to-date, usually by a couple months
- in the end, having both allows for packages from either conda, conda-forge, or pypi
- conda can be slow
- poetry's dependency resolver is more advanced than pip's
