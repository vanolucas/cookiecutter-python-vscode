import unittest
from os import environ
from urllib.parse import urljoin

import requests


class TestEcho(unittest.TestCase):
    def setUp(self) -> None:
        ENDPOINT = "echo"
        self.url = urljoin(environ["API_BASE"], ENDPOINT)
        self.msg = "Hi!"

    def test_echo(self) -> None:
        params = {"msg": self.msg}
        response = requests.get(self.url, params)
        response.raise_for_status()
        echo = response.json()
        self.assertEqual(echo, self.msg, "incorrect echo message")
