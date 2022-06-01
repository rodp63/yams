import click
import signal
import yams.info as info

from yams.utils import get_crawler, today, days_ago, date_to_str
from alive_progress import alive_bar


SHORT_HELP = "Start a newspaper crawling process"


def print_arguments(source, keywords, since, to):
    click.secho("Parameters:", bold=True)
    click.secho("  Kind: ", nl=False, bold=True)
    click.echo("Newspaper")
    click.secho("  Source: ", nl=False, bold=True)
    click.echo(source)
    click.secho("  Keywords:", bold=True)
    for k in keywords:
        click.echo(f"  - {k}")
    click.secho("  Since: ", nl=False, bold=True)
    click.echo(since)
    click.secho("  To: ", nl=False, bold=True)
    click.echo(to)


@click.command(short_help=SHORT_HELP)
@click.argument("source", required=True, envvar=info.news["env"]["source"]["value"])
@click.option(
    "--keyword",
    "-k",
    multiple=True,
    required=True,
    envvar=info.news["env"]["keywords"]["value"],
    help="Set one keyword for post retrieval",
)
@click.option(
    "--since",
    "-s",
    default=days_ago(30, to_str=True),
    type=click.DateTime(formats=["%Y-%m-%d"]),
    envvar=info.news["env"]["since"]["value"],
    help="Set the lower date of the posts to retrieve",
)
@click.option(
    "--to",
    "-t",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    default=today(to_str=True),
    envvar=info.news["env"]["to"]["value"],
    help="Set the upper date of the posts to retrieve",
)
def yams_command(source, keyword, since, to):
    crawler = get_crawler()
    since, to = date_to_str(since), date_to_str(to)
    print_arguments(source, keyword, since, to)
    crawler.crawl(source, since=since, to=to, keywords=",".join(keyword))

    with alive_bar(
        spinner=None,
        unknown="waves",
        length=10,
        monitor="{count} items",
        title="Crawling in progress",
    ) as bar:

        def sig_handler(sig, frame):
            bar()

        signal.signal(signal.SIGUSR1, sig_handler)
        crawler.start()

    click.echo("Crawling finished")
