# -*- coding: utf-8 -*-
from urlparse import urlparse
from sslcert import SSLCert
import ssl


def get_sslcert(domain):
    if ('http' in domain) or ('/' in domain):
        try:
            parse_object = urlparse(domain)
        except:
            print "Specified domain is wrong"
            return False
        domain = parse_object.netloc

    try:
        cert = ssl.get_server_certificate((domain, 443))
    except:
        return False

    return SSLCert(cert)
