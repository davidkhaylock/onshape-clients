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


class BTFriendInfo(object):
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
        'token': 'str',
        'email': 'str',
        'image_url': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'name': 'str',
        'id': 'str',
        'href': 'str',
        'view_ref': 'str'
    }

    attribute_map = {
        'token': 'token',
        'email': 'email',
        'image_url': 'imageUrl',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'name': 'name',
        'id': 'id',
        'href': 'href',
        'view_ref': 'viewRef'
    }

    def __init__(self, token=None, email=None, image_url=None, first_name=None, last_name=None, name=None, id=None, href=None, view_ref=None):  # noqa: E501
        """BTFriendInfo - a model defined in OpenAPI"""  # noqa: E501

        self._token = None
        self._email = None
        self._image_url = None
        self._first_name = None
        self._last_name = None
        self._name = None
        self._id = None
        self._href = None
        self._view_ref = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if email is not None:
            self.email = email
        if image_url is not None:
            self.image_url = image_url
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref

    @property
    def token(self):
        """Gets the token of this BTFriendInfo.  # noqa: E501


        :return: The token of this BTFriendInfo.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this BTFriendInfo.


        :param token: The token of this BTFriendInfo.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def email(self):
        """Gets the email of this BTFriendInfo.  # noqa: E501


        :return: The email of this BTFriendInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BTFriendInfo.


        :param email: The email of this BTFriendInfo.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def image_url(self):
        """Gets the image_url of this BTFriendInfo.  # noqa: E501


        :return: The image_url of this BTFriendInfo.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this BTFriendInfo.


        :param image_url: The image_url of this BTFriendInfo.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def first_name(self):
        """Gets the first_name of this BTFriendInfo.  # noqa: E501


        :return: The first_name of this BTFriendInfo.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this BTFriendInfo.


        :param first_name: The first_name of this BTFriendInfo.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this BTFriendInfo.  # noqa: E501


        :return: The last_name of this BTFriendInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this BTFriendInfo.


        :param last_name: The last_name of this BTFriendInfo.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def name(self):
        """Gets the name of this BTFriendInfo.  # noqa: E501


        :return: The name of this BTFriendInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTFriendInfo.


        :param name: The name of this BTFriendInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTFriendInfo.  # noqa: E501


        :return: The id of this BTFriendInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTFriendInfo.


        :param id: The id of this BTFriendInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BTFriendInfo.  # noqa: E501


        :return: The href of this BTFriendInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTFriendInfo.


        :param href: The href of this BTFriendInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTFriendInfo.  # noqa: E501


        :return: The view_ref of this BTFriendInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTFriendInfo.


        :param view_ref: The view_ref of this BTFriendInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

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
        if not isinstance(other, BTFriendInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
