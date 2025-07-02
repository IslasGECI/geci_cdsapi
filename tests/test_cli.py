from geci_cdsapi.cli import cli

from typer.testing import CliRunner

import geci_test_tools as gtt

runner = CliRunner()


def test_version():
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert " version " in gtt.strip_ansi_sequences(result.stdout)


def test_monthly_wind_average():
    output_path = "tests/wind_average.csv"
    gtt.if_exist_remove(output_path)
    result = runner.invoke(
        cli,
        [
            "monthly-wind-average",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
