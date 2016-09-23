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

from pprint import pformat
from six import iteritems
import re


class Output(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, type=None, title=None, configuration=None, creator_user_id=None, created_at=None, content_pack=None):
        """
        Output - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'title': 'str',
            'configuration': 'object',
            'creator_user_id': 'str',
            'created_at': 'datetime',
            'content_pack': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'title': 'title',
            'configuration': 'configuration',
            'creator_user_id': 'creator_user_id',
            'created_at': 'created_at',
            'content_pack': 'content_pack'
        }

        self._id = id
        self._type = type
        self._title = title
        self._configuration = configuration
        self._creator_user_id = creator_user_id
        self._created_at = created_at
        self._content_pack = content_pack

    @property
    def id(self):
        """
        Gets the id of this Output.


        :return: The id of this Output.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Output.


        :param id: The id of this Output.
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """
        Gets the type of this Output.


        :return: The type of this Output.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Output.


        :param type: The type of this Output.
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """
        Gets the title of this Output.


        :return: The title of this Output.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Output.


        :param title: The title of this Output.
        :type: str
        """

        self._title = title

    @property
    def configuration(self):
        """
        Gets the configuration of this Output.


        :return: The configuration of this Output.
        :rtype: object
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this Output.


        :param configuration: The configuration of this Output.
        :type: object
        """

        self._configuration = configuration

    @property
    def creator_user_id(self):
        """
        Gets the creator_user_id of this Output.


        :return: The creator_user_id of this Output.
        :rtype: str
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """
        Sets the creator_user_id of this Output.


        :param creator_user_id: The creator_user_id of this Output.
        :type: str
        """

        self._creator_user_id = creator_user_id

    @property
    def created_at(self):
        """
        Gets the created_at of this Output.


        :return: The created_at of this Output.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Output.


        :param created_at: The created_at of this Output.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def content_pack(self):
        """
        Gets the content_pack of this Output.


        :return: The content_pack of this Output.
        :rtype: str
        """
        return self._content_pack

    @content_pack.setter
    def content_pack(self, content_pack):
        """
        Sets the content_pack of this Output.


        :param content_pack: The content_pack of this Output.
        :type: str
        """

        self._content_pack = content_pack

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other