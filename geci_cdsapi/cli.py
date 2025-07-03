from geci_cdsapi.calculate_wind_speed import (
    read_and_calculate_wind_speed,
    write_windspeed_dataset_to_csv,
)
import typer


cli = typer.Typer()


@cli.command()
def monthly_wind_average(
    start_year: int = typer.Option(),
    end_year: int = typer.Option(),
    island: str = typer.Option(),
    output_path: str = typer.Option(),
):
    wind_speed_dataset = read_and_calculate_wind_speed([end_year], island, "tests/data")
    write_windspeed_dataset_to_csv(wind_speed_dataset, output_path)


@cli.command()
def version():
    return "0.1.0"
