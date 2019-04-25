# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.96
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTPartMaterialPropertyInfo(object):
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
        'name': 'str',
        'value': 'str',
        'type': 'str',
        'description': 'str',
        'category': 'str',
        'display_name': 'str',
        'units': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'type': 'type',
        'description': 'description',
        'category': 'category',
        'display_name': 'displayName',
        'units': 'units'
    }

    def __init__(self, name=None, value=None, type=None, description=None, category=None, display_name=None, units=None):  # noqa: E501
        """BTPartMaterialPropertyInfo - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._value = None
        self._type = None
        self._description = None
        self._category = None
        self._display_name = None
        self._units = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        if display_name is not None:
            self.display_name = display_name
        if units is not None:
            self.units = units

    @property
    def name(self):
        """Gets the name of this BTPartMaterialPropertyInfo.  # noqa: E501


        :return: The name of this BTPartMaterialPropertyInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTPartMaterialPropertyInfo.


        :param name: The name of this BTPartMaterialPropertyInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this BTPartMaterialPropertyInfo.  # noqa: E501


        :return: The value of this BTPartMaterialPropertyInfo.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BTPartMaterialPropertyInfo.


        :param value: The value of this BTPartMaterialPropertyInfo.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def type(self):
        """Gets the type of this BTPartMaterialPropertyInfo.  # noqa: E501


        :return: The type of this BTPartMaterialPropertyInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTPartMaterialPropertyInfo.


        :param type: The type of this BTPartMaterialPropertyInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this BTPartMaterialPropertyInfo.  # noqa: E501


        :return: The description of this BTPartMaterialPropertyInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTPartMaterialPropertyInfo.


        :param description: The description of this BTPartMaterialPropertyInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def category(self):
        """Gets the category of this BTPartMaterialPropertyInfo.  # noqa: E501


        :return: The category of this BTPartMaterialPropertyInfo.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this BTPartMaterialPropertyInfo.


        :param category: The category of this BTPartMaterialPropertyInfo.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def display_name(self):
        """Gets the display_name of this BTPartMaterialPropertyInfo.  # noqa: E501


        :return: The display_name of this BTPartMaterialPropertyInfo.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this BTPartMaterialPropertyInfo.


        :param display_name: The display_name of this BTPartMaterialPropertyInfo.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def units(self):
        """Gets the units of this BTPartMaterialPropertyInfo.  # noqa: E501


        :return: The units of this BTPartMaterialPropertyInfo.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this BTPartMaterialPropertyInfo.


        :param units: The units of this BTPartMaterialPropertyInfo.  # noqa: E501
        :type: str
        """

        self._units = units

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
        if not isinstance(other, BTPartMaterialPropertyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
