""" This module provides the RP To-Do CLI."""
# rptodo/cli.py

from typing import Optional

import typer

from rptodo import __version__, __app_name__

app = typer.Typer()


def version__callback(value: bool) -> None:
    """Method that prints version when --version or -v option are requested."""
    if value:
        typer.echo(f'{__app_name__} v{__version__}')
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        '--version',
        '-v',
        help="Show the application's version and exit.",
        callback=version__callback,
        is_eager=True
    )
) -> None:
    return
