# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.97
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTApiKeyUpdateParams(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'state': 'int',
        'access_key': 'str'
    }

    attribute_map = {
        'state': 'state',
        'access_key': 'accessKey'
    }

    def __init__(self, state=None, access_key=None):  # noqa: E501
        """BTApiKeyUpdateParams - a model defined in OpenAPI"""  # noqa: E501

        self._state = None
        self._access_key = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if access_key is not None:
            self.access_key = access_key

    @property
    def state(self):
        """Gets the state of this BTApiKeyUpdateParams.  # noqa: E501


        :return: The state of this BTApiKeyUpdateParams.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BTApiKeyUpdateParams.


        :param state: The state of this BTApiKeyUpdateParams.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def access_key(self):
        """Gets the access_key of this BTApiKeyUpdateParams.  # noqa: E501


        :return: The access_key of this BTApiKeyUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this BTApiKeyUpdateParams.


        :param access_key: The access_key of this BTApiKeyUpdateParams.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BTApiKeyUpdateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
