# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.1.1+01d50e5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import graylog
from graylog.rest import ApiException
from graylog.apis.systemdebugevents_api import SystemdebugeventsApi


class TestSystemdebugeventsApi(unittest.TestCase):
    """ SystemdebugeventsApi unit test stubs """

    def setUp(self):
        self.api = graylog.apis.systemdebugevents_api.SystemdebugeventsApi()

    def tearDown(self):
        pass

    def test_generate_cluster_debug_event(self):
        """
        Test case for generate_cluster_debug_event

        Create and send a cluster debug event.
        """
        pass

    def test_generate_debug_event(self):
        """
        Test case for generate_debug_event

        Create and send a local debug event.
        """
        pass

    def test_show_last_cluster_debug_event(self):
        """
        Test case for show_last_cluster_debug_event

        Show last received cluster debug event.
        """
        pass

    def test_show_last_debug_event(self):
        """
        Test case for show_last_debug_event

        Show last received local debug event.
        """
        pass


if __name__ == '__main__':
    unittest.main()
