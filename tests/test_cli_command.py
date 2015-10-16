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
        assert not result.exit_code == 0
        assert result.exception

    def test_failed_timeout(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['chosun.com'])
        assert not result.exit_code == 0
        assert result.exception

    def test_failed_self_certificates(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['newstapa.org'])
        assert not result.exit_code == 0
        assert result.exception