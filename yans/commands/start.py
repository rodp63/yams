import click
import signal

from yans.utils import get_crawler, today, days_ago, date_to_str
from alive_progress import alive_bar


SHORT_HELP = "Start the crawling process"


def print_arguments(keywords, since, to):
    click.echo("Crawling parameters:")
    click.secho("  Keywords:", bold=True)
    for k in keywords:
        click.echo(f"  - {k}")
    click.secho("  Since: ", nl=False, bold=True)
    click.echo(since)
    click.secho("  To: ", nl=False, bold=True)
    click.echo(to)


@click.command(short_help=SHORT_HELP)
@click.argument("spider", required=True, envvar="YANS_SPIDER")
@click.option(
    "--keyword",
    "-k",
    multiple=True,
    required=True,
    envvar="YANS_KEYWORDS",
    help="Set one keyword for post retrieval",
)
@click.option(
    "--since",
    "-s",
    default=days_ago(30, to_str=True),
    type=click.DateTime(formats=["%Y-%m-%d"]),
    envvar="YANS_SINCE",
    help="Set the lower date of the posts to retrieve",
)
@click.option(
    "--to",
    "-t",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    default=today(to_str=True),
    envvar="YANS_TO",
    help="Set the upper date of the posts to retrieve",
)
def yans_command(spider, keyword, since, to):
    crawler = get_crawler()
    since, to = date_to_str(since), date_to_str(to)
    print_arguments(keyword, since, to)
    crawler.crawl(spider, since=since, to=to, keywords=",".join(keyword))

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
