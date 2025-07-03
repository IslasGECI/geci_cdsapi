from geci_cdsapi.cli import cli

from typer.testing import CliRunner
import pytest
import os

import geci_test_tools as gtt

runner = CliRunner()


def test_version():
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert " version " in gtt.strip_ansi_sequences(result.stdout)
    result = runner.invoke(cli, ["version"])
    assert "0.1.0\n" in gtt.strip_ansi_sequences(result.stdout)


@pytest.mark.skipif(os.getenv("GITHUB_ACTIONS") is None, reason="Solo se ejecuta en GitHub Actions")
def test_monthly_wind_average():
    output_path = "tests/wind_average.csv"
    gtt.if_exist_remove(output_path)
    result = runner.invoke(
        cli,
        [
            "monthly-wind-average",
            "--start-year",
            2012,
            "--end-year",
            2013,
            "--island",
            "San Benito",
            "--output-path",
            output_path,
        ],
    )
    gtt.assert_exist(output_path)
    nc_files = ["San Benito_wind_2012.nc", "San Benito_wind_2013.nc"]
    for nc_file in nc_files:
        gtt.assert_exist(f"tests/{nc_file}")
    assert result.exit_code == 0
