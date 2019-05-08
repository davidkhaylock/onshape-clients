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


class ParameterizedHeader(object):
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
        'value': 'str',
        'parameters': 'dict(str, str)'
    }

    attribute_map = {
        'value': 'value',
        'parameters': 'parameters'
    }

    def __init__(self, value=None, parameters=None):  # noqa: E501
        """ParameterizedHeader - a model defined in OpenAPI"""  # noqa: E501

        self._value = None
        self._parameters = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if parameters is not None:
            self.parameters = parameters

    @property
    def value(self):
        """Gets the value of this ParameterizedHeader.  # noqa: E501


        :return: The value of this ParameterizedHeader.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ParameterizedHeader.


        :param value: The value of this ParameterizedHeader.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def parameters(self):
        """Gets the parameters of this ParameterizedHeader.  # noqa: E501


        :return: The parameters of this ParameterizedHeader.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ParameterizedHeader.


        :param parameters: The parameters of this ParameterizedHeader.  # noqa: E501
        :type: dict(str, str)
        """

        self._parameters = parameters

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
        if not isinstance(other, ParameterizedHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
