import unittest
from click.testing import CliRunner

from sslchecker.cli import cli


class TestCliCommand(unittest.TestCase):
    def setUp(self):
        pass

    def test_success_google_domain(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['google.com'])
        assert result.exit_code == 0
        assert 'SSL secured' in result.output

    def test_failed_naver_domain(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['naver.com'])
        assert result.exit_code == -1
        assert result.exception

    def test_warning_pinkfong_domain(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['pinkfong.com'])
        assert result.exit_code == 0
        assert 'SSL unsecured' in result.output
