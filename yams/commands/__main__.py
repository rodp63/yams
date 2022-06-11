import importlib

import click

__version__ = "0.1"
CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__)
def cli():
    pass


commands = ["info", "start"]

for command in commands:
    module = importlib.import_module("yams.commands.{}".format(command))
    cli.add_command(module.yams_command, command)
