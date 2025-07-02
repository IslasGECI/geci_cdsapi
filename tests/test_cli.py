from geci_cdsapi.cli import cli

from typer.testing import CliRunner

import geci_test_tools as gtt

runner = CliRunner()


def test_version():
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert " version " in gtt.strip_ansi_sequences(result.stdout)
