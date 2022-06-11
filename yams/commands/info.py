import os

import click

import yams.info as info
from yams.utils import get_crawler

SHORT_HELP = "Display useful information"
version = "1.0"


def display_info(info, spiders):
    click.secho(info["name"] + ":", bold=True)

    click.secho("  Sources:", bold=True)
    for s in spiders:
        if s in info["spiders"]:
            click.echo(f"    - {s}")

    click.secho("  Environment:", bold=True)
    for e in info["env"].values():
        if e["list"]:
            values = os.getenv(e["value"], "")
            click.echo(f"    {e['value']}:")
            for v in values.split():
                click.echo(f"      - {v}")
        else:
            click.secho(f"    {e['value']}: ", nl=False)
            click.echo(os.getenv(e["value"], ""))


@click.command(short_help=SHORT_HELP)
def yams_command():
    crawler = get_crawler()
    spiders = crawler.spider_loader.list()

    click.secho("Version: ", bold=True, nl=False)
    click.echo(version)

    display_info(info.news, spiders)
