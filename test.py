from cloudfoundry import CloudFoundryInterface

def test():
    cfi = CloudFoundryInterface("http://api.cloud.url.com", "MY_EMAIL@whatever", "MYPASSWORD", True)
    cfi.login()
    a = cfi
    b = cfi.apps
    #c = cfi.apps()
    cfi.
    r = cfi._get_or_exception('/v2/stacks/39a6edda-ab09-41dd-8bb5-eb8ca5f7f8d4', True)


    print dir(cfi.apps[cfi.apps.keys()[0]])

if __name__ == '__main__':
    test()
