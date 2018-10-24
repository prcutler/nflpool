import unittest
import pyramid.testing

from tests.web_settings import settings


class HomeControllerTests(unittest.TestCase):
    def setUp(self):
        from nflpool import main

        app = main({}, **settings, logging="OFF")
        # noinspection PyPackageRequirements
        from webtest import TestApp

        self.app = TestApp(app)

    def test_home_page(self):
        # noinspection PyPackageRequirements
        import webtest.response

        response: webtest.response.TestResponse = self.app.get("/", status=200)

        self.assertTrue(b"nflpool" in response.body)
