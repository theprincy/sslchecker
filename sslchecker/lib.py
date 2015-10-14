# -*- coding: utf-8 -*-
from __future__ import (unicode_literals)
from .sslcert import SSLCert
from socket import error as socket_error
import errno
import socket
import ssl
import OpenSSL
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


def get_sslcert(domain):
    if ('http' in domain) or ('/' in domain):
        parse_object = urlparse(domain)
        domain = parse_object.netloc

    try:
        cert = ssl.get_server_certificate((domain, 443))
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    except socket.gaierror:
        print("Nodename nor servname provided, or not known")
        return False
    except socket_error as serr:
        if serr.errno != errno.ECONNREFUSED:
            raise serr
        return False
    except:
        return False

    return SSLCert(x509)
