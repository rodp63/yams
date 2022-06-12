import importlib

import click


@click.group(short_help="Start a crawling process")
def yams_command():
    pass


commands = ["newspaper"]

for command in commands:
    module = importlib.import_module("yams.commands.start.{}".format(command))
    yams_command.add_command(module.yams_command, command)
