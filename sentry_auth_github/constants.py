from __future__ import absolute_import, print_function

from django.conf import settings


AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'

ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'

CLIENT_ID = getattr(settings, 'GITHUB_APP_ID', None)

CLIENT_SECRET = getattr(settings, 'GITHUB_API_SECRET', None)

ERR_NO_ORG_ACCESS = 'You do not have access to the required GitHub organization.'

# we request repo as we share scopes with the other GitHub integration
SCOPE = 'user:email,read:org,repo'

DOMAIN = getattr(settings, 'GITHUB_DOMAIN', 'api.github.com')
