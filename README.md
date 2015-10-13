# ssl checker

A simple SSL certificates validator on your command line.

## pip install

```shell
pip install sslchecker
```

## example

```shell
$ sslchecker google.com
###############
# SSL secured #
###############

Common name: google.com
Valid from: 2015-09-29 19:04:14
Expiration date: 2015-12-28 00:00:00
    Expire in 75 days.

Signature Algorithm: RSA
Key length: 2048
Issued by:
    Country: United States
    Organization: Google Inc
    Common name: Google Internet Authority G2
```
