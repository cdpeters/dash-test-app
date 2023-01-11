---
title: Data Project Install Instructions
created: 2022-11-29T17:47:19.640Z
modified: 2022-11-30T02:31:35.538Z
---

# Data Project Install Instructions

## High Level Steps
### Done Once Overall (Before Starting Any Projects)
1. Install Anaconda (most recent is fine)
1. Install python from [www.python.org](https://www.python.org/) (most recent is fine)
1. Install `poetry` globally via script

### Done Once Per Project
1. Set up GitHub repo and clone to local machine
1. Create `conda` environment and activate it
1. Create `environment.yml` file representing the `conda` environment (if no `environment.yml` file exists)
1. Initialize `poetry` (creates `pyproject.toml` and `poetry.lock`, see detailed instructions below if you already have one or both of these files)
1. Remove `packages` field from the `[tool.poetry]` section of `pyproject.toml`
1. Install dependencies (only if you have a `pyproject.toml` file that is already populated)
1. Add the following development tools configuration files/script from the Dash Test App repo:
	- `.flake8`
	- `.pre-commit-config.yaml`
	- `dev_tools.sh`

## Detailed Instructions with Code
### Done Once Overall (Before Starting Any Projects)
1. Install Anaconda from [www.anaconda.com](https://www.anaconda.com/products/distribution)
	- `conda` will be used to manage virtual environments
	- most recent version is fine
1. Install python separately (it is useful to have a system python) from [www.python.org](https://www.python.org/)
	- python will be used to install `poetry` globally
	- most recent version is fine
1. Install `poetry`:
	- `poetry` will be used for dependency management within a project
	- preferred way to install is via terminal script (this will give most recent version):
		- Windows (powershell):
			```powershell
			# This is the only place powershell is needed, the rest of
			# this document uses git-bash
			(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
			```
		- Mac:
			```shell
			curl -sSL https://install.python-poetry.org | python3 -
			```


### Done Once Per project
1. Create a repository:
	1. On Github:
		- Click on the "Create a new repository" or "New" button (depending on the page you're viewing)
		- Include:
			- `README.md`
			- `.gitignore` (for example "python" if a python project)
			- `LICENSE` (a good default choice is Apache License 2.0)
	1. Clone repo locally (requires SSH credentials):
		```shell
		git clone <remote_repo_ssh_url>
		```

1. Create `conda` environment and activate it:
	1. Create environment `<env_name>`:
		- From scratch:
			- Specify python version (to get the `pip` version associated with that python version):
			```shell
			conda create --name <env_name> python=<version>
			```

		- From `environment.yml` file:
			- `-f` tells `conda` to create the environment from a file
			- The `environment.yml` file should have a `name` field. This is why a name is not specified in the command below
			```shell
			conda env create -f environment.yml
			```
	1. Activate `<env_name>`:
		```shell
		conda activate <env_name>
		```

1. Create `environment.yml` file representing the `conda` environment:
	```shell
	conda env export --from-history | grep -v "^prefix: " > environment.yml
	```
	- `--from-history` is important, this creates an environment file from the direct dependencies when the `conda` environment was created and from any packages added using `conda` during the project.
	- `grep -v "^prefix: "` takes the output from export and only writes the lines that don't start with `"prefix: "` to `environment.yml`. The prefix is just the path to the virtual environment folder and does include our computer's username. We leave it out here so that's not on github and because `conda` doesn't need it when creating the virtual environment

1. Initialize `poetry`:
	- Explanation of `poetry` files:
		- `pyproject.toml`:
			- the file that holds your project and development dependencies as well as some configuration for development tools
		- `poetry.lock`:
			- Generated from `pyproject.toml` via the `poetry lock` command (or auto-generated at initialization). Contains all the project and development dependencies **and** their sub-dependencies with their versions "locked". Environments will be reproduced via this file in combination with an `environment.yml` file (which captures the `conda` specific packages)
			- **DON'T MODIFY `poetry.lock` DIRECTLY!** This file should always be generated from the `pyproject.toml` file
	- Initialization:
		- From scratch (no `pyproject.toml` or `poetry.lock` files exist):
			```shell
			poetry init
			```
			- As you run through the initialization it is fine to accept the defaults for the `version` or `description` fields. These would be used if the project was a package and was meant to be published on PyPi
			- This process creates `pyproject.toml` and an associated `poetry.lock` file
		- From `pyproject.toml` file (no `poetry.lock` file):
			1. Place `pyproject.toml` in the root directory of your project
			1. Then run the following `poetry` commands:
				```shell
				poetry check
				poetry lock
				```
				- `poetry check` checks to ensure that the `pyproject.toml` file is valid
				- `poetry lock` generates the `poetry.lock` file based on the current `pyproject.toml` file
		- Both `pyproject.toml` and an associated `poetry.lock` file exist and are synced:
			- Initialization not needed, skip to step 5

1. Check the `[tool.poetry]` section of the `pyproject.toml` file. If there is a `packages` field, delete that line since these projects won't be packages

1. Install dependencies via `poetry`:
	- This step is only necessary if you have an already populated `pyproject.toml` file. If you created a new `pyproject.toml` file in step 4 via `poetry init` then you can skip this step as there will not be any dependencies to install.
	- Install:
		```shell
		poetry install
		```
