import typer


cli = typer.Typer()


@cli.command()
def monthly_wind_average(
    start_year: int = typer.Option(),
    end_year: int = typer.Option(),
    island: str = typer.Option(),
    output_path: str = typer.Option(),
):
    pass


@cli.command()
def version():
    return "0.1.0"
