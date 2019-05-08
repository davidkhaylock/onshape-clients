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


class BTCloudStorageAccountParams(object):
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
        'import_folder_id': 'str',
        'export_folder_id': 'str'
    }

    attribute_map = {
        'import_folder_id': 'importFolderId',
        'export_folder_id': 'exportFolderId'
    }

    def __init__(self, import_folder_id=None, export_folder_id=None):  # noqa: E501
        """BTCloudStorageAccountParams - a model defined in OpenAPI"""  # noqa: E501

        self._import_folder_id = None
        self._export_folder_id = None
        self.discriminator = None

        if import_folder_id is not None:
            self.import_folder_id = import_folder_id
        if export_folder_id is not None:
            self.export_folder_id = export_folder_id

    @property
    def import_folder_id(self):
        """Gets the import_folder_id of this BTCloudStorageAccountParams.  # noqa: E501


        :return: The import_folder_id of this BTCloudStorageAccountParams.  # noqa: E501
        :rtype: str
        """
        return self._import_folder_id

    @import_folder_id.setter
    def import_folder_id(self, import_folder_id):
        """Sets the import_folder_id of this BTCloudStorageAccountParams.


        :param import_folder_id: The import_folder_id of this BTCloudStorageAccountParams.  # noqa: E501
        :type: str
        """

        self._import_folder_id = import_folder_id

    @property
    def export_folder_id(self):
        """Gets the export_folder_id of this BTCloudStorageAccountParams.  # noqa: E501


        :return: The export_folder_id of this BTCloudStorageAccountParams.  # noqa: E501
        :rtype: str
        """
        return self._export_folder_id

    @export_folder_id.setter
    def export_folder_id(self, export_folder_id):
        """Sets the export_folder_id of this BTCloudStorageAccountParams.


        :param export_folder_id: The export_folder_id of this BTCloudStorageAccountParams.  # noqa: E501
        :type: str
        """

        self._export_folder_id = export_folder_id

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
        if not isinstance(other, BTCloudStorageAccountParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
