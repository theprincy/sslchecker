import unittest


from sslchecker.lib import get_sslcert


class TestGetSslCert(unittest.TestCase):
    def setUp(self):
        pass

    def test_google_passed(self, domain='google.com'):
        sslcert = get_sslcert(domain)
        assert sslcert.is_secured

    def test_naver_not_ssl(self, domain='naver.com'):
        sslcert = get_sslcert(domain)
        assert False is sslcert
