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


class BTMetadataSchemaParams(object):
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
        'owner_id': 'str',
        'object_type': 'int',
        'owner_type': 'int'
    }

    attribute_map = {
        'owner_id': 'ownerId',
        'object_type': 'objectType',
        'owner_type': 'ownerType'
    }

    def __init__(self, owner_id=None, object_type=None, owner_type=None):  # noqa: E501
        """BTMetadataSchemaParams - a model defined in OpenAPI"""  # noqa: E501

        self._owner_id = None
        self._object_type = None
        self._owner_type = None
        self.discriminator = None

        if owner_id is not None:
            self.owner_id = owner_id
        if object_type is not None:
            self.object_type = object_type
        if owner_type is not None:
            self.owner_type = owner_type

    @property
    def owner_id(self):
        """Gets the owner_id of this BTMetadataSchemaParams.  # noqa: E501


        :return: The owner_id of this BTMetadataSchemaParams.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this BTMetadataSchemaParams.


        :param owner_id: The owner_id of this BTMetadataSchemaParams.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def object_type(self):
        """Gets the object_type of this BTMetadataSchemaParams.  # noqa: E501


        :return: The object_type of this BTMetadataSchemaParams.  # noqa: E501
        :rtype: int
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this BTMetadataSchemaParams.


        :param object_type: The object_type of this BTMetadataSchemaParams.  # noqa: E501
        :type: int
        """

        self._object_type = object_type

    @property
    def owner_type(self):
        """Gets the owner_type of this BTMetadataSchemaParams.  # noqa: E501


        :return: The owner_type of this BTMetadataSchemaParams.  # noqa: E501
        :rtype: int
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this BTMetadataSchemaParams.


        :param owner_type: The owner_type of this BTMetadataSchemaParams.  # noqa: E501
        :type: int
        """

        self._owner_type = owner_type

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
        if not isinstance(other, BTMetadataSchemaParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other