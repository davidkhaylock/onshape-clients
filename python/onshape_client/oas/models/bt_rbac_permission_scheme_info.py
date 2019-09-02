# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.103
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTRbacPermissionSchemeInfo(object):
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
        'description': 'str',
        'active': 'bool',
        'entries': 'list[Entry]',
        'predefined_permission_scheme': 'int',
        'href': 'str',
        'view_ref': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'active': 'active',
        'entries': 'entries',
        'predefined_permission_scheme': 'predefinedPermissionScheme',
        'href': 'href',
        'view_ref': 'viewRef',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, description=None, active=None, entries=None, predefined_permission_scheme=None, href=None, view_ref=None, id=None, name=None):  # noqa: E501
        """BTRbacPermissionSchemeInfo - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._active = None
        self._entries = None
        self._predefined_permission_scheme = None
        self._href = None
        self._view_ref = None
        self._id = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if active is not None:
            self.active = active
        if entries is not None:
            self.entries = entries
        if predefined_permission_scheme is not None:
            self.predefined_permission_scheme = predefined_permission_scheme
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this BTRbacPermissionSchemeInfo.  # noqa: E501


        :return: The description of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTRbacPermissionSchemeInfo.


        :param description: The description of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def active(self):
        """Gets the active of this BTRbacPermissionSchemeInfo.  # noqa: E501


        :return: The active of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this BTRbacPermissionSchemeInfo.


        :param active: The active of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def entries(self):
        """Gets the entries of this BTRbacPermissionSchemeInfo.  # noqa: E501


        :return: The entries of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :rtype: list[Entry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this BTRbacPermissionSchemeInfo.


        :param entries: The entries of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :type: list[Entry]
        """

        self._entries = entries

    @property
    def predefined_permission_scheme(self):
        """Gets the predefined_permission_scheme of this BTRbacPermissionSchemeInfo.  # noqa: E501


        :return: The predefined_permission_scheme of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :rtype: int
        """
        return self._predefined_permission_scheme

    @predefined_permission_scheme.setter
    def predefined_permission_scheme(self, predefined_permission_scheme):
        """Sets the predefined_permission_scheme of this BTRbacPermissionSchemeInfo.


        :param predefined_permission_scheme: The predefined_permission_scheme of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :type: int
        """

        self._predefined_permission_scheme = predefined_permission_scheme

    @property
    def href(self):
        """Gets the href of this BTRbacPermissionSchemeInfo.  # noqa: E501


        :return: The href of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTRbacPermissionSchemeInfo.


        :param href: The href of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTRbacPermissionSchemeInfo.  # noqa: E501


        :return: The view_ref of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTRbacPermissionSchemeInfo.


        :param view_ref: The view_ref of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

    @property
    def id(self):
        """Gets the id of this BTRbacPermissionSchemeInfo.  # noqa: E501


        :return: The id of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTRbacPermissionSchemeInfo.


        :param id: The id of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this BTRbacPermissionSchemeInfo.  # noqa: E501


        :return: The name of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTRbacPermissionSchemeInfo.


        :param name: The name of this BTRbacPermissionSchemeInfo.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, BTRbacPermissionSchemeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other