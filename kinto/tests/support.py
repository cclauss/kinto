try:
    import unittest2 as unittest
except ImportError:
    import unittest  # NOQA

from cliquet.tests import support as cliquet_support
import webtest
import kinto


class BaseWebTest(cliquet_support.BaseWebTest):

    api_prefix = kinto.API_VERSION

    def get_test_app(self):
        return webtest.TestApp(kinto.main({}, **self.get_app_settings()))

    def get_app_settings(self):
        return {
            'cliquet.project_name': 'cloud storage',
            'cliquet.project_docs': 'https://kinto.rtfd.org/',
            'cliquet.basic_auth_enabled': 'true',
            'cliquet.storage_backend': 'cliquet.storage.redis',
            'cliquet.session_backend': 'cliquet.session.redis',
            'fxa-oauth.client_id': '89513028159972bc',
            'fxa-oauth.client_secret': '9aced230585cc0aa2932e2eb871c9a3a7d6458'
                                       'e59ccf57eb610ea0a3467dd800',
            'fxa-oauth.oauth_uri': 'https://oauth-stable.dev.lcip.org',
            'fxa-oauth.scope': 'profile'
        }