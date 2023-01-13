---
title: Data Project Creation/Installation Instructions
created: 2022-11-29T17:47:19.640Z
modified: 2023-01-13T09:16:27.332Z
---

# Data Project Creation/Installation Instructions

> This guide is not intended to be read in its entirety. Ready only the sections corresponding to your role in the project as defined in the first section below, or just use the guide as a reference when needed.

## Development Roles
- There are two distinct sets of installation instructions in this guide. One for each of the following development roles:
	1. Creator - sets up the project and works on it
	1. Collaborator - only works on the project

## High Level Steps
> For details and code for completing any of the *High Level Steps*, see the *[Detailed Steps](#detailed-steps)* section.

#### *Development Role: Both (Creator and Collaborator)*
### Done Once Overall (before creating or collaborating on any projects)
1. Install Anaconda from [www.anaconda.com](https://www.anaconda.com/products/distribution)
1. Install python from [www.python.org](https://www.python.org/)
1. Install `poetry` globally via script

> **Global set up is complete. You're ready to create projects or collaborate on them!**

<hr>

#### *Development Role: Creator*
### Done Once Per Project
1. Set up GitHub repo and clone to local machine
1. Create python environment or use an existing one (complete one of the following):
	- **Create environment from scratch**
		> Your intention is not to use an existing `environment.yml` and `pyproject.toml` to create the environment.
		1. Create `conda` environment **and activate it**
		1. Create `environment.yml` file from `conda` environment
		1. Initialize `poetry` to create `pyproject.toml` and `poetry.lock`
		1. Remove `packages` field from the `[tool.poetry]` section of `pyproject.toml`
		1. Add dev tools and their configs to `pyproject.toml`
		1. Add any separate dev tool config files and the dev tool cli script to the current project's root directory
		1. Install dev tool dependencies with `poetry install`
		1. Install `pre-commit` hooks
		> **Result**: A new python environment with dev tools ready to use. Project dependencies will have to be added to it.
	- **Create environment from existing environment files**
		> An `environment.yml` and `pyproject.toml` exist but the environment has not yet been created on your computer.
		1. Copy `environment.yml` and `pyproject.toml` into the current project's root directory
		1. Create `conda` environment from `environment.yml` file **and activate it**
		1. Add any separate dev tool config files and the dev tool cli script to the current project's root directory
		1. Install dependencies via `poetry install`
		1. Install `pre-commit` hooks
		> **Result**: A new python environment with dev tools **and** project dependencies ready to use.
	- **Use an existing python environment**
		> An environment that already exists on your computer.
		1. Activate the environment
		1. Copy this environment's `environment.yml` and `pyproject.toml` files into the current project's root directory
		1. Add any separate dev tool config files and the dev tool cli script to the current project's root directory
		1. Install `pre-commit` hooks
		> **Result**: An existing python environment with its dev tools **and** its project dependencies ready to use.

1. Create the project directory structure
1. Create a `secrets.toml` file
1. Add `secrets.toml` to `.gitignore` ==**WARNING: Do not skip this step!**==

> **Project creation is complete. Project is ready to be worked on and shared with collaborators!**

<hr>

#### *Development Role: Collaborator*
### Done Once Per Project
1. Clone the GitHub repo to local machine
1. Create `conda` environment from `environment.yml`
1. Install dependencies via `poetry install`
1. Install `pre-commit` hooks
1. Create a `secrets.toml` file

> **Existing project set up is complete. Project is ready to be worked on and shared with collaborators!**

<hr>

## Detailed Steps

#### *Development Role: Both (Creator and Collaborator)*
### Done Once Overall (Before Creating or Collaborating on Any Projects)
1. Install Anaconda from [www.anaconda.com](https://www.anaconda.com/products/distribution)
	- `conda` will be used to manage python virtual environments
	- most recent version is fine
1. Install python separately from [www.python.org](https://www.python.org/)
	- python will be used to install `poetry` globally
	- most recent version is fine
1. Install `poetry`:
	- `poetry` will be used for dependency management within a project
	1. Install is via terminal script (this will give most recent version and is the preferred way to install):
		- Windows (powershell):
			```powershell
			(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
			```
			> This is the only place powershell is needed, the rest of this document uses git-bash.
		- Mac:
			```shell
			curl -sSL https://install.python-poetry.org | python3 -
			```
	2. Try the command `poetry --version`. If the command is not recognized, add the following to your path environment variable:
		- Windows:
			- `%APPDATA%\Python\Scripts` or `%APPDATA%\pypoetry\venv\Scripts\poetry`
		- Unix:
			- `$HOME/.local/bin` or:
				- Linux/Unix:
					- `~/.local/share/pypoetry/venv/bin/poetry`
				- Mac:
					- `~/Library/Application Support/pypoetry/venv/bin/poetry`
	3. Check installation:
		```shell
		poetry --version
		```

> **Global set up is complete. You're ready to create projects or collaborate on them!**

<hr>

#### *Development Role: Creator*
### Done Once Per Project
1. Set up GitHub repo and clone to local machine
	1. On GitHub:
		- Create the new repository
		- Include:
			- `README.md`
			- `.gitignore` (choose "python" as the template if a python project)
			- `LICENSE` (a good default choice is Apache License 2.0)
	1. Clone repo locally:
		```shell
		git clone <remote_repo_ssh_url>
		```

1. Create python environment or use an existing one (complete one of the following):
	- **Create environment from scratch**
		> Your intention is not to use an existing `environment.yml` and `pyproject.toml` to create the environment.

		1. Create `conda` environment **and activate it**
			```shell
			conda create --name <env_name> python=<version>
			```
			- Specify python version so that the appropriate `pip` for that version is included
			- Activate `<env_name>`:
			```shell
			conda activate <env_name>
			```

		1. Create `environment.yml` file from `conda` environment
			```shell
			conda env export --from-history | grep -v "^prefix: " > environment.yml
			```
			- `--from-history` is important, this creates an environment file from the direct dependencies when the `conda` environment was created and from any packages added using `conda` during the project.
			- `grep -v "^prefix: "` takes the output from export and only writes the lines that don't start with `"prefix: "` to `environment.yml`. The prefix is just the path to the virtual environment folder and does include our computer's username. We leave it out here so that's not on github and because `conda` doesn't need it when creating the virtual environment

		1. Initialize `poetry` to create `pyproject.toml` and `poetry.lock`
			- Explanation of `poetry` files:
				- `pyproject.toml`:
					- the file that holds your project and dev dependencies as well as some configuration for dev tools
				- `poetry.lock`:
					- Generated from `pyproject.toml` via the `poetry lock` command (or auto-generated at initialization). Contains all the project and dev dependencies **and** their sub-dependencies with their versions "locked". Environments will be reproduced via this file in combination with an `environment.yml` file (which captures the `conda` specific packages)
					- ==**DON'T MODIFY `poetry.lock` DIRECTLY!**== This file should always be generated from the `pyproject.toml` file
			- Initialization:
				```shell
				poetry init
				```
				- As you run through the initialization it is fine to accept the defaults for the `version` or `description` fields. These would be used if the project was a package and was meant to be published on PyPi
				- This process creates `pyproject.toml` and an associated `poetry.lock` file

		1. Remove `packages` field from the `[tool.poetry]` section of `pyproject.toml`
			- Check the `[tool.poetry]` section of the `pyproject.toml` file. If there is a `packages` field, delete that line since these projects won't be packages

		1. Add dev tools and their configs to `pyproject.toml`
			1. Copy `[tool.poetry.group.dev.dependencies]` section of `pyproject.toml` from a previous project's repo into the current project's `pyproject.toml`
			1. Copy any section with the heading pattern `[tool.<dev_tool_name>*]` or `[[tool.<dev_tool_name>*]]` into the current project's `pyproject.toml`

		1. Add any separate dev tool config files and the dev tool cli script to the current project's root directory
			- `.flake8` - flake8 config
			- `.pre-commit-config.yaml` - pre-commit config
			- `tools.sh` - cli tool for running the dev tools

		1. Install dev tool dependencies with `poetry install`
			```shell
			poetry install
			```
			- This step is necessary so that the dev tools that were added can be installed and ready to use

		1. Install `pre-commit` hooks
			```shell
			pre-commit install
			```
			- This will install the pre-commit hooks found in the `.pre-commit-config.yaml` file into the git hooks folder
			- Once this is complete, the hooks will run on each `git commit`
			- Optionally, you can run the hooks against all current files in the project with the following command (this is useful when the hooks are first installed since they normally only run on files that have changed):
			```shell
			pre-commit run --all-files
			```

		> **Result**: A new python environment with dev tools ready to use. Project dependencies will have to be added to it.

	- **Create environment from existing environment files**
		> An `environment.yml` and `pyproject.toml` exist but the environment has not yet been created on your computer.

		1. Copy `environment.yml` and `pyproject.toml` into the current project's root directory

		1. Create `conda` environment from `environment.yml` file **and activate it**
			```shell
			conda env create -f environment.yml
			```
			- `-f` tells `conda` to create the environment from a file
			- The environment's name is drawn from the `name` field in the `environment.yml` file. This is why a name is not specified in the command above
				- Activate `<env_name>` (the name should have been printed in the terminal from the previous command, you can also open the `environment.yml` file and look for the `name` field):
			```shell
			conda activate <env_name>
			```

		1. Add any separate dev tool config files and the dev tool cli script to the current project's root directory
			- `.flake8` - flake8 config
			- `.pre-commit-config.yaml` - pre-commit config
			- `tools.sh` - cli tool for running the dev tools

		1. Install dependencies via `poetry install`
			```shell
			poetry install
			```
			- This step is necessary so that the project dependencies and dev tools that were in `pyproject.toml` can be installed and ready to use

		1. Install `pre-commit` hooks
			```shell
			pre-commit install
			```
			- This will install the pre-commit hooks found in the `.pre-commit-config.yaml` file into the git hooks folder
			- Once this is complete, the hooks will run on each `git commit`
			- Optionally, you can run the hooks against all current files in the project with the following command (this is useful when the hooks are first installed since they normally only run on files that have changed):
			```shell
			pre-commit run --all-files
			```

		> **Result**: A new python environment with dev tools **and** project dependencies ready to use.

	- **Use an existing python environment**
		> An environment that already exists on your computer.

		1. Activate the environment

		1. Copy this environment's `environment.yml` and `pyproject.toml` files into the current project's root directory

		1. Add the following config files/dev tool script to the current project's root directory:
			- `.flake8` - flake8 config
			- `.pre-commit-config.yaml` - pre-commit config
			- `tools.sh` - cli tool for running the dev tools

		1. Install `pre-commit` hooks
			```shell
			pre-commit install
			```
			- This will install the pre-commit hooks found in the `.pre-commit-config.yaml` file into the git hooks folder
			- Once this is complete, the hooks will run on each `git commit`
			- Optionally, you can run the hooks against all current files in the project with the following command (this is useful when the hooks are first installed since they normally only run on files that have changed):
			```shell
			pre-commit run --all-files
			```

		> **Result**: An existing python environment with its dev tools **and** its project dependencies ready to use.

1. Create the project directory structure
	> The `src` directory can be left out if there is no intention to build a website (this can easily be added later if things change). The other folders can be left out as well if they're not needed.
	- The directories:
		- `data`: any data files (for example *csv* or *sqlite*)
		- `notebooks`: jupyter notebooks
		- `notes`: markdown and other notes files
		- `src`: website files
		- `tests`: unit tests and other test files
	<div align="center">
		<img src="images/top_level_project_directory_tree_scaled.svg" />
	</div>

1. Create a `secrets.toml` file
	```toml
	[google_drive]
	path = 'path/to/google/drive/collaboration/folder'
	```
	- Add the `path` variable to a `google_drive` heading at the top of the file.
	- This file will contain any secrets the project requires, examples:
		- Database username and password
		- Database URL
		- API keys
		- Local machine specific paths such as the path to the Google Drive collaboration folder
1. Add `secrets.toml` to `.gitignore` ==**WARNING: Do not skip this step!**==
	- Ensure that this file does not get committed to the remote repo (i.e. the online GitHub repo)

> **Project creation is complete. Ready to use and share with collaborators!**

<hr>

#### *Development Role: Collaborator*
### Done Once Per Project
1. Clone the GitHub repo to local machine
	```shell
	git clone <remote_repo_ssh_url>
	```

1. Create `conda` environment from `environment.yml` **and activate it**
	```shell
	conda env create -f environment.yml
	```
	- `-f` tells `conda` to create the environment from a file
	- The environment's name is drawn from the `name` field in the `environment.yml` file. This is why a name is not specified in the command above
	- Activate `<env_name>` (the name should have been printed in the terminal from the previous command, you can also open the `environment.yml` file and look for the `name` field):
	```shell
	conda activate <env_name>
	```

1. Install dependencies via `poetry install`
	```shell
	poetry install
	```
	- This step is necessary so that the project dependencies and dev tools that were in `pyproject.toml` can be installed and ready to use

1. Install `pre-commit` hooks
	```shell
	pre-commit install
	```
	- This will install the pre-commit hooks found in the `.pre-commit-config.yaml` file into the git hooks folder
	- Once this is complete, the hooks will run on each `git commit`
	- Optionally, you can run the hooks against all current files in the project with the following command (this is useful when the hooks are first installed since they normally only run on files that have changed):
	```shell
	pre-commit run --all-files
	```

1. Create a `secrets.toml` file
	```toml
	[google_drive]
	path = 'path/to/google/drive/collaboration/folder'
	```
	- Add the `path` variable to a `google_drive` heading at the top of the file.
	- This file will contain any secrets the project requires, examples:
		- Database username and password
		- Database URL
		- API keys
		- Local machine specific paths such as the path to the Google Drive collaboration folder

> **Existing project set up is complete. Project is ready to be worked on and shared with collaborators!**

<hr>
