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

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SourcesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def list(self, range, **kwargs):
        """
        Get a list of all sources (not more than 5000) that have messages in the current indices. The result is cached for 10 seconds.
        Range: The parameter is in seconds relative to the current time. 86400 means 'in the last day',0 is special and means 'across all indices'

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list(range, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Object range: Relative timeframe to search in. See method description. (required)
        :param Object size: Maximum size of the result set.
        :return: SourcesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(range, **kwargs)
        else:
            (data) = self.list_with_http_info(range, **kwargs)
            return data

    def list_with_http_info(self, range, **kwargs):
        """
        Get a list of all sources (not more than 5000) that have messages in the current indices. The result is cached for 10 seconds.
        Range: The parameter is in seconds relative to the current time. 86400 means 'in the last day',0 is special and means 'across all indices'

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_with_http_info(range, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Object range: Relative timeframe to search in. See method description. (required)
        :param Object size: Maximum size of the result set.
        :return: SourcesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['range', 'size']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'range' is set
        if ('range' not in params) or (params['range'] is None):
            raise ValueError("Missing the required parameter `range` when calling `list`")

        resource_path = '/sources'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'range' in params:
            query_params['range'] = params['range']
        if 'size' in params:
            query_params['size'] = params['size']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SourcesList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
