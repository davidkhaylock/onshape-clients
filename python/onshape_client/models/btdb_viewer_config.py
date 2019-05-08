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


class BTDBViewerConfig(object):
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
        'id': 'str',
        'query_field_labels': 'dict(str, str)',
        'collection_configs': 'list[BTDBViewerCollectionConfig]',
        'created_by': 'str',
        'created_at': 'datetime',
        'modified_by': 'str',
        'modified_at': 'datetime',
        'new': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'query_field_labels': 'queryFieldLabels',
        'collection_configs': 'collectionConfigs',
        'created_by': 'createdBy',
        'created_at': 'createdAt',
        'modified_by': 'modifiedBy',
        'modified_at': 'modifiedAt',
        'new': 'new'
    }

    def __init__(self, id=None, query_field_labels=None, collection_configs=None, created_by=None, created_at=None, modified_by=None, modified_at=None, new=None):  # noqa: E501
        """BTDBViewerConfig - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._query_field_labels = None
        self._collection_configs = None
        self._created_by = None
        self._created_at = None
        self._modified_by = None
        self._modified_at = None
        self._new = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if query_field_labels is not None:
            self.query_field_labels = query_field_labels
        if collection_configs is not None:
            self.collection_configs = collection_configs
        if created_by is not None:
            self.created_by = created_by
        if created_at is not None:
            self.created_at = created_at
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_at is not None:
            self.modified_at = modified_at
        if new is not None:
            self.new = new

    @property
    def id(self):
        """Gets the id of this BTDBViewerConfig.  # noqa: E501


        :return: The id of this BTDBViewerConfig.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTDBViewerConfig.


        :param id: The id of this BTDBViewerConfig.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def query_field_labels(self):
        """Gets the query_field_labels of this BTDBViewerConfig.  # noqa: E501


        :return: The query_field_labels of this BTDBViewerConfig.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._query_field_labels

    @query_field_labels.setter
    def query_field_labels(self, query_field_labels):
        """Sets the query_field_labels of this BTDBViewerConfig.


        :param query_field_labels: The query_field_labels of this BTDBViewerConfig.  # noqa: E501
        :type: dict(str, str)
        """

        self._query_field_labels = query_field_labels

    @property
    def collection_configs(self):
        """Gets the collection_configs of this BTDBViewerConfig.  # noqa: E501


        :return: The collection_configs of this BTDBViewerConfig.  # noqa: E501
        :rtype: list[BTDBViewerCollectionConfig]
        """
        return self._collection_configs

    @collection_configs.setter
    def collection_configs(self, collection_configs):
        """Sets the collection_configs of this BTDBViewerConfig.


        :param collection_configs: The collection_configs of this BTDBViewerConfig.  # noqa: E501
        :type: list[BTDBViewerCollectionConfig]
        """

        self._collection_configs = collection_configs

    @property
    def created_by(self):
        """Gets the created_by of this BTDBViewerConfig.  # noqa: E501


        :return: The created_by of this BTDBViewerConfig.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this BTDBViewerConfig.


        :param created_by: The created_by of this BTDBViewerConfig.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this BTDBViewerConfig.  # noqa: E501


        :return: The created_at of this BTDBViewerConfig.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BTDBViewerConfig.


        :param created_at: The created_at of this BTDBViewerConfig.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def modified_by(self):
        """Gets the modified_by of this BTDBViewerConfig.  # noqa: E501


        :return: The modified_by of this BTDBViewerConfig.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this BTDBViewerConfig.


        :param modified_by: The modified_by of this BTDBViewerConfig.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def modified_at(self):
        """Gets the modified_at of this BTDBViewerConfig.  # noqa: E501


        :return: The modified_at of this BTDBViewerConfig.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this BTDBViewerConfig.


        :param modified_at: The modified_at of this BTDBViewerConfig.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def new(self):
        """Gets the new of this BTDBViewerConfig.  # noqa: E501


        :return: The new of this BTDBViewerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._new

    @new.setter
    def new(self, new):
        """Sets the new of this BTDBViewerConfig.


        :param new: The new of this BTDBViewerConfig.  # noqa: E501
        :type: bool
        """

        self._new = new

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
        if not isinstance(other, BTDBViewerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
