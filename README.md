# SSL checker

A simple SSL certificates validator on your command line.

[![Build Status](https://travis-ci.org/raccoonyy/sslchecker.svg?branch=master)](https://travis-ci.org/raccoonyy/sslchecker)

[![Coverage Status](https://coveralls.io/repos/raccoonyy/sslchecker/badge.svg?branch=master&service=github)](https://coveralls.io/github/raccoonyy/sslchecker?branch=master)

## Requirements
`Python` >= 2.7

## Installation

```shell
pip install sslchecker
```

## Sample result

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

## Author

Seungho Kim(@raccoonyy)

## Thanks to
[@limeburst](https://github.com/limeburst)

## License

sslchecker is distributed under MIT license.