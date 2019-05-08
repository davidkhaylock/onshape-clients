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


class BTAppElementUpdateParams(object):
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
        'changes': 'list[BTAppElementChangeParams]',
        'transaction_id': 'str',
        'parent_change_id': 'str',
        'return_error': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'changes': 'changes',
        'transaction_id': 'transactionId',
        'parent_change_id': 'parentChangeId',
        'return_error': 'returnError'
    }

    def __init__(self, description=None, changes=None, transaction_id=None, parent_change_id=None, return_error=None):  # noqa: E501
        """BTAppElementUpdateParams - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._changes = None
        self._transaction_id = None
        self._parent_change_id = None
        self._return_error = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if changes is not None:
            self.changes = changes
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if parent_change_id is not None:
            self.parent_change_id = parent_change_id
        if return_error is not None:
            self.return_error = return_error

    @property
    def description(self):
        """Gets the description of this BTAppElementUpdateParams.  # noqa: E501


        :return: The description of this BTAppElementUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTAppElementUpdateParams.


        :param description: The description of this BTAppElementUpdateParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def changes(self):
        """Gets the changes of this BTAppElementUpdateParams.  # noqa: E501


        :return: The changes of this BTAppElementUpdateParams.  # noqa: E501
        :rtype: list[BTAppElementChangeParams]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this BTAppElementUpdateParams.


        :param changes: The changes of this BTAppElementUpdateParams.  # noqa: E501
        :type: list[BTAppElementChangeParams]
        """

        self._changes = changes

    @property
    def transaction_id(self):
        """Gets the transaction_id of this BTAppElementUpdateParams.  # noqa: E501


        :return: The transaction_id of this BTAppElementUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this BTAppElementUpdateParams.


        :param transaction_id: The transaction_id of this BTAppElementUpdateParams.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def parent_change_id(self):
        """Gets the parent_change_id of this BTAppElementUpdateParams.  # noqa: E501


        :return: The parent_change_id of this BTAppElementUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._parent_change_id

    @parent_change_id.setter
    def parent_change_id(self, parent_change_id):
        """Sets the parent_change_id of this BTAppElementUpdateParams.


        :param parent_change_id: The parent_change_id of this BTAppElementUpdateParams.  # noqa: E501
        :type: str
        """

        self._parent_change_id = parent_change_id

    @property
    def return_error(self):
        """Gets the return_error of this BTAppElementUpdateParams.  # noqa: E501


        :return: The return_error of this BTAppElementUpdateParams.  # noqa: E501
        :rtype: bool
        """
        return self._return_error

    @return_error.setter
    def return_error(self, return_error):
        """Sets the return_error of this BTAppElementUpdateParams.


        :param return_error: The return_error of this BTAppElementUpdateParams.  # noqa: E501
        :type: bool
        """

        self._return_error = return_error

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
        if not isinstance(other, BTAppElementUpdateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
