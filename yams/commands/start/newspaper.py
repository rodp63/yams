import os

import click
from alive_progress import alive_bar

import yams.info as info
from yams.utils import date_to_str, days_ago, get_crawler, init_bar, remove_bar, today

SHORT_HELP = "Start a newspaper crawling process"


def print_arguments(source, keywords, output, since, to, flags):
    click.secho("Parameters:", bold=True)
    click.secho("  Kind: ", nl=False, bold=True)
    click.echo("Newspaper")
    click.secho("  Source: ", nl=False, bold=True)
    click.echo(source)
    click.secho("  Output: ", nl=False, bold=True)
    click.echo(output)
    click.secho("  Keywords:", bold=True)
    for k in keywords:
        click.echo(f"    - {k}")
    click.secho("  Since: ", nl=False, bold=True)
    click.echo(since)
    click.secho("  To: ", nl=False, bold=True)
    click.echo(to)
    click.secho("  Flags:", bold=True)
    for f in flags:
        click.echo(f"    - --{f}")
    click.echo("\n")


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
    "--output",
    "-o",
    envvar=info.news["env"]["output"]["value"],
    type=click.Path(file_okay=True, dir_okay=False),
    help="Save output to json FILE instead of stdout",
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
@click.option(
    "--exact-match",
    is_flag=True,
    default=False,
    show_default=True,
    help="Look for the exact match of the keywords",
)
def yams_command(source, keyword, output, since, to, exact_match):
    crawler = get_crawler()
    since, to = date_to_str(since), date_to_str(to)
    flags = []
    if exact_match:
        flags.append("exact-match")
    if not output:
        output = "stdout"
    else:
        if not output.endswith(".json"):
            output += ".json"
        os.environ.update({info.news["env"]["output"]["value"]: output})

    print_arguments(source, keyword, output, since, to, flags)

    with alive_bar(
        spinner=None,
        unknown="waves",
        length=10,
        monitor="{count} items",
        title="Crawling in progress",
        enrich_print=False,
    ) as bar:
        init_bar(bar)
        crawler.crawl(
            source,
            since=since,
            to=to,
            keywords=",".join(keyword),
            flags=",".join(flags),
        )
        crawler.start()
        remove_bar()

    click.echo("Crawling finished")
