import click
from pathlib import Path
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
@click.option(
    "--path",
    type=click.Path(exists=False),
    default=None,
    help="Directory to save diary entries (default: ~/diary)",
)
def dictate(duration, enhance, path):
    """Record and transcribe your diary entry."""
    click.echo("Starting diary dictation...")
    click.echo("=" * 50)

    path = Path(path) if path else None
    output_path = process_diary(enhance=enhance, diary_path=path)
    click.echo(f"\nSuccess! Diary saved to: {output_path}")


if __name__ == "__main__":
    cli()
