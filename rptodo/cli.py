""" This module provides the RP To-Do CLI."""
# rptodo/cli.py

from pathlib import Path
from typing import Optional

import typer

from rptodo import __version__, __app_name__, ERRORS, config, database

app = typer.Typer()

@app.command()
def init(
    db_path: str = typer.Option(
        str(database.DEFAULT_DB_FILE_PATH), # Default database path
        '--db-path',
        '-db',
        prompt = 'to-do database location?'
    )
) -> None:
    """Initialie the to-do database."""
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
            f'Creating database failed with "{ERRORS[app_init_error]}"',
            fg = typer.colors.RED
        )
        raise typer.Exit(1)
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
            f'Creating database failed with "{ERRORS[db_init_error]}"',
            fg = typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(
            f'The to-do database is {db_path}',
            fg = typer.colors.GREEN
        )

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
    """Method that executes version callback to print app version."""
    return
