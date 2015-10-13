# -*- coding: utf-8 -*-
from urlparse import urlparse
from netlib.certutils import SSLCert
import click
import ssl


def get_sslcert(domain):
    if ('http' in domain) or ('/' in domain):
        try:
            parse_object = urlparse(domain)
        except:
            click.echo("Specified domain is wrong")
            return False
        domain = parse_object.netloc

    try:
        cert = ssl.get_server_certificate((domain, 443))
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    except:
        return False

    return SSLCert(x509)
