import unittest


from sslchecker.lib import get_sslcert


class TestGetSslCert(unittest.TestCase):
    def test_failed_wrong_domain_name(self, domain='google.com/asdf/'):
        assert not get_sslcert(domain)

    def test_success_full_url(self, domain='http://google.asdf'):
        assert not get_sslcert(domain)

    def test_success_google_domain(self, domain='google.com'):
        assert not get_sslcert(domain).has_expired

    def test_failed_naver_domain(self, domain='naver.com'):
        assert not get_sslcert(domain)

    def test_failed_expired_domain(self, domain='pinkfong.com'):
        assert get_sslcert(domain).has_expired
