import typer


cli = typer.Typer()


@cli.command()
def version():
    return "0.1.0"
