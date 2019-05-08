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


class BTUpdateVersionThumbnailParams(object):
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
        'version_ids': 'list[BTIdAndConfiguration]',
        'force_update': 'bool'
    }

    attribute_map = {
        'version_ids': 'versionIds',
        'force_update': 'forceUpdate'
    }

    def __init__(self, version_ids=None, force_update=None):  # noqa: E501
        """BTUpdateVersionThumbnailParams - a model defined in OpenAPI"""  # noqa: E501

        self._version_ids = None
        self._force_update = None
        self.discriminator = None

        if version_ids is not None:
            self.version_ids = version_ids
        if force_update is not None:
            self.force_update = force_update

    @property
    def version_ids(self):
        """Gets the version_ids of this BTUpdateVersionThumbnailParams.  # noqa: E501


        :return: The version_ids of this BTUpdateVersionThumbnailParams.  # noqa: E501
        :rtype: list[BTIdAndConfiguration]
        """
        return self._version_ids

    @version_ids.setter
    def version_ids(self, version_ids):
        """Sets the version_ids of this BTUpdateVersionThumbnailParams.


        :param version_ids: The version_ids of this BTUpdateVersionThumbnailParams.  # noqa: E501
        :type: list[BTIdAndConfiguration]
        """

        self._version_ids = version_ids

    @property
    def force_update(self):
        """Gets the force_update of this BTUpdateVersionThumbnailParams.  # noqa: E501


        :return: The force_update of this BTUpdateVersionThumbnailParams.  # noqa: E501
        :rtype: bool
        """
        return self._force_update

    @force_update.setter
    def force_update(self, force_update):
        """Sets the force_update of this BTUpdateVersionThumbnailParams.


        :param force_update: The force_update of this BTUpdateVersionThumbnailParams.  # noqa: E501
        :type: bool
        """

        self._force_update = force_update

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
        if not isinstance(other, BTUpdateVersionThumbnailParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
