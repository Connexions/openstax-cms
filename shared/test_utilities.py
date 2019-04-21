from django.urls import resolve, Resolver404

def assertPathDoesNotRedirectToTrailingSlash(test, path):
    try:
        resolve(path)
    except Resolver404:
        test.fail(f'The path {path} cannot be found')

    response = test.client.get(path)

    if (type(response).__name__ == 'HttpResponsePermanentRedirect' or
       type(response).__name__ == 'HttpResponsePermanentRedirect'):
       test.assertNotEqual(response.url, path + "/")
