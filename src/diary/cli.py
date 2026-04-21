import click
from .transcriber import process_diary


@click.group()
def cli():
    """Voice-dictated diary stored locally."""
    pass


@cli.command()
@click.option(
    "--duration", default=300, help="Max recording duration in seconds (default: 300)"
)
@click.option(
    "--enhance/--no-enhance",
    default=False,
    help="Enhance with Ollama for better grammar and tone (default: off)",
)
def dictate(duration, enhance):
    """Record and transcribe your diary entry."""
    click.echo("Starting diary dictation...")
    click.echo("=" * 50)

    path = process_diary(enhance=enhance)
    click.echo(f"\nSuccess! Diary saved to: {path}")


if __name__ == "__main__":
    cli()
