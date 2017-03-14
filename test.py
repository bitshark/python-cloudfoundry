#!/usr/bin/env python
"""HSDP CF API Interface
Quick test example from Alex

Usage:
  test.py [options] <cf_api_endpoint> <cf_username> <cf_password>
  test.py (-h | --help)
  test.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  <cf_api_endpoint>  The CF API endpoint to use
  <cf_username>      The CF CLI username
  <cf_password>      The CF CLI password
"""
from cloudfoundry import CloudFoundryInterface
from docopt import docopt


def test(endpoint, username, password):
    cfi = CloudFoundryInterface("http://" + endpoint, username, password, True)
    cfi.login()
    a = cfi
    b = cfi.apps
    #c = cfi.apps()
    r = cfi._get_or_exception('/v2/stacks/39a6edda-ab09-41dd-8bb5-eb8ca5f7f8d4', True)

    print(dir(cfi.apps[cfi.apps.keys()[0]]))

if __name__ == '__main__':
    args = docopt(__doc__, version='1.0.0')
    test(endpoint=args['<cf_api_endpoint>'], username=args['<cf_username>'], password=args['<cf_password>'])
