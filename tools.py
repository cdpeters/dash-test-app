"""A CLI for running development tools on jupyter notebooks and python files."""

import subprocess
from pathlib import Path

import click

# Help messages and meta variables for the CLI options and arguments.
help_msg = {
    "markdown_help": """Runs blacken-docs on FILENAME to format code blocks within.
    FILENAME must be either a jupyter notebook (.ipynb) or a markdown file (.md) and
    must be found within the current working directory.""",
    "skip_help": """Skips running of the tool names provided. The value is a
    string containing space separated tool names.""",
    "skip_metavar": "STRING",
    "file_type_help": """'nb' - Runs tools on jupyter notebooks (.ipynb) only.
    'all' - Runs tools on both jupyter notebooks and python files (.ipynb and .py).
    'py' - Runs tools on python files (.py) only.""",
    "filenames_metavar": "[FILENAME]...",
}


@click.command()
@click.option("-md", "--markdown", is_flag=True, help=help_msg["markdown_help"])
@click.option(
    "-s",
    "--skip",
    help=help_msg["skip_help"],
    metavar=help_msg["skip_metavar"],
)
@click.option(
    "-t",
    "--type",
    "file_type",
    type=click.Choice(["nb", "py", "all"]),
    show_default=True,
    default="nb",
    help=help_msg["file_type_help"],
)
@click.argument(
    "filenames",
    nargs=-1,
    type=click.Path(exists=True, dir_okay=False),
    metavar=help_msg["filenames_metavar"],
)
def tools(
    markdown: bool,
    skip: str | None,
    file_type: str,
    filenames: tuple[str, ...],
) -> None:
    """tools.py runs development tools on project files.

    tools.py runs the development tools on the current working directory (note that some
    of the tools have the ability to recursively apply themselves down the directory
    tree). The default behavior is to run these tools on jupyter notebooks (.ipynb)
    only. CLI options allow for modifying this behavior to be able to run these tools on
    python (.py) and markdown (.md) files as well. Additionally, there is an option to
    allow for skipping tools during the run process if needed.

    Current Tools In Use:

    \b
           black: code formatter
    blacken-docs: code formatter for markdown code blocks in jupyter notebooks
                  (.ipynb) and markdown files (.md). Runs on jupyter notebooks by
                  default. Not run on markdown files by default, see the -md|--markdown
                  cli option.
           isort: import formatter
     interrogate: docstring coverage
          flake8: linter
            mypy: type checker
    """
    # Constants and Variables ----------------------------------------------------------
    run_tools = ["black", "blacken-docs", "isort", "interrogate", "flake8", "mypy"]
    header_banner_len = 80
    tool_banner_len = 74
    type_messages = {
        "nb": "notebooks (.ipynb)",
        "py": "python files (.py)",
        "md": "markdown files (.md)",
    }
    type_prepend = {}

    # Helper Functions -----------------------------------------------------------------
    def double_echo(func):
        """Decorate banners with two blank lines on each side."""

        def wrapper_double_echo(*args, **kwargs):
            """Add a blank line before and after the func call."""
            click.echo("")
            func(*args, **kwargs)
            click.echo("")

        return wrapper_double_echo

    @double_echo
    def create_banner(
        message: str,
        *,
        banner_length: int,
        fg_color: str,
        bg_color: str,
        prepend: dict[str, str] | None = None,
        file_type: str | None = None,
    ) -> None:
        """Create a banner with a message and coloring for clarity.

        If `file_type` is not specified, the banner is a header banner and no file type
        is prepended to the banner. If `file_type` is specified, the banner is a tool
        banner thus the file type that the tool is running on will be prepended to the
        banner.

        Parameters
        ----------
        message : str
            Banner message.
        banner_length : int
            Length of banner in number of characters.
        fg_color : str
            Foreground color (text color).
        bg_color : str
            Background color.
        prepend : dict[str, str] | None, optional
            Mapping from `file_type` string to the prepend string, by default None.
        file_type : str | None, optional
            Type of file that the tool is being run on, by default None.
        """
        # Calculate whitespace in order to center the banner message.
        total_ws = banner_length - len(message)
        left_ws = total_ws // 2
        right_ws = total_ws - left_ws

        if file_type:
            # Calculate new left whitespace to allow room for prepended file type.
            left_ws = left_ws - len(prepend[file_type]) - 1
            banner_message = (
                f" {prepend[file_type]}{' '*left_ws}{message}{' '*right_ws}"
            )
        else:
            banner_message = f"{' '*left_ws}{message}{' '*right_ws}"
        click.echo(click.style(banner_message, fg=fg_color, bg=bg_color))

    def generate_run_summary(
        tools: list[str], prepend: dict[str, str], file_type: str
    ) -> None:
        """Generate a summary of the run including the tools and file type being run on.

        Parameters
        ----------
        tools : list[str]
            List of development tools selected for the current run.
        prepend : dict[str, str]
            Mapping from `file_type` string to the prepend string.
        file_type : str
            Type of file that the tool is being run on.
        """
        # Copy so that the object passed to `tools` is not modified.
        tools_display = list(tools)

        # blacken-docs is not run on python files, remove it from the list of tools
        # shown for python files.
        if file_type == "py":
            tools_display.remove("blacken-docs")

        click.echo("Run Summary:")
        click.echo(f"Tool(s): {', '.join(tools_display)}")
        click.echo(f"File Type(s): {', '.join(prepend.values())}")

    # Path processing ------------------------------------------------------------------
    # `tools_path` will be static (always the directory where this file is located).
    tools_path = Path(__file__).parent
    # `cwd` will be dynamic based on where the script is run from.
    cwd = Path.cwd()

    # Input Validation -----------------------------------------------------------------
    if markdown and not filenames:
        raise click.UsageError(
            "No FILENAME provided for markdown option. Provide one or more FILENAME as "
            + "an argument."
        )

    if (skip or (file_type != "nb")) and markdown:
        raise click.UsageError(
            "The markdown option can only be run without any other options."
        )

    # Create `Path` objects for `filenames` for easier access to the path parts in the
    # logic below.
    filenames_list = [cwd.joinpath(filename) for filename in filenames]
    for path in filenames_list:
        if path.suffix not in (".md", ".ipynb"):
            raise click.BadArgumentUsage(
                f"'{path.name}' is not a markdown or jupyter notebook file."
            )
        if path.parent != cwd:
            raise click.BadArgumentUsage(
                f"'{path.name}' is not found in the current working directory."
            )

    # Input Processing -----------------------------------------------------------------
    # Set up `type_prepend` based on the `markdown` and `file_type` inputs
    if markdown:
        run_tools = ["blacken-docs"]
        type_prepend["md"] = type_messages["md"]
        file_type = "md"
    elif file_type == "all":
        type_prepend["nb"] = type_messages["nb"]
        type_prepend["py"] = type_messages["py"]
    else:
        type_prepend[file_type] = type_messages[file_type]

    # Remove tools if the `skip` option was used.
    if skip:
        skip_tools = set(skip.split(" "))
        for tool in skip_tools:
            if tool not in run_tools:
                raise click.BadParameter(f"'{tool}' is not a current dev tool.")
            else:
                run_tools.remove(tool)

    # Run Dev Tools --------------------------------------------------------------------
    create_banner(
        "RUNNING DEV TOOLS",
        banner_length=header_banner_len,
        fg_color="black",
        bg_color="bright_cyan",
    )

    generate_run_summary(tools=run_tools, prepend=type_prepend, file_type=file_type)

    for ft in type_prepend:
        for tool in run_tools:
            if ft == "nb":
                create_banner(
                    f"Running {tool}",
                    banner_length=tool_banner_len,
                    fg_color="black",
                    bg_color="bright_yellow",
                    prepend=type_prepend,
                    file_type=ft,
                )
                # `mypy` addressed separately in order to ensure the config file is
                # added to the command.
                if tool == "mypy":
                    subprocess.run(
                        [
                            "nbqa",
                            tool,
                            cwd,
                            "--config-file",
                            tools_path.joinpath("pyproject.toml"),
                        ]
                    )
                else:
                    subprocess.run(["nbqa", tool, cwd])
            elif ft == "py":
                # `blacken-docs` is not run on python files.
                if tool != "blacken-docs":
                    create_banner(
                        f"Running {tool}",
                        banner_length=tool_banner_len,
                        fg_color="black",
                        bg_color="bright_green",
                        prepend=type_prepend,
                        file_type=ft,
                    )
                    # `mypy` addressed separately in order to ensure the config file is
                    # added to the command.
                    if tool == "mypy":
                        subprocess.run(
                            [
                                tool,
                                cwd,
                                "--config-file",
                                tools_path.joinpath("pyproject.toml"),
                            ]
                        )
                    else:
                        subprocess.run([tool, cwd])
            elif ft == "md":
                create_banner(
                    f"Running {tool}",
                    banner_length=tool_banner_len,
                    fg_color="black",
                    bg_color="bright_blue",
                    prepend=type_prepend,
                    file_type=ft,
                )
                subprocess.run([tool, *filenames])

    create_banner(
        "DEV TOOLS COMPLETE",
        banner_length=header_banner_len,
        fg_color="black",
        bg_color="bright_cyan",
    )


if __name__ == "__main__":
    tools()
