import os
import click

from yans.utils import get_crawler


SHORT_HELP = "Display useful information"
version = "1.0"


@click.command(short_help=SHORT_HELP)
def yans_command():
    crawler = get_crawler()
    spiders = crawler.spider_loader.list()
    click.secho("Version: ", bold=True, nl=False)
    click.echo(version)
    click.secho("Spiders:", bold=True)
    for s in spiders:
        click.echo(f"- {s}")

    env_list = ["YANS_SPIDER", "YANS_SINCE", "YANS_TO"]
    click.secho("Environment: ", bold=True)
    for e in env_list:
        click.secho(f"  {e}: ", nl=False)
        click.echo(os.getenv(e, ""))

    kws = os.getenv("YANS_KEYWORDS", "")
    click.secho(f"  YANS_KEYWORDS:")
    for k in kws.split():
        click.echo(f"  - {k}")
