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


class BTReleasePackageItemParams(object):
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
        'properties': 'list[BTPropertyValueParam]',
        'id': 'str',
        'version_id': 'str',
        'document_id': 'str',
        'workspace_id': 'str',
        'element_id': 'str',
        'part_id': 'str',
        'href': 'str',
        'configuration': 'str',
        'part_number': 'str',
        'is_included': 'bool'
    }

    attribute_map = {
        'properties': 'properties',
        'id': 'id',
        'version_id': 'versionId',
        'document_id': 'documentId',
        'workspace_id': 'workspaceId',
        'element_id': 'elementId',
        'part_id': 'partId',
        'href': 'href',
        'configuration': 'configuration',
        'part_number': 'partNumber',
        'is_included': 'isIncluded'
    }

    def __init__(self, properties=None, id=None, version_id=None, document_id=None, workspace_id=None, element_id=None, part_id=None, href=None, configuration=None, part_number=None, is_included=None):  # noqa: E501
        """BTReleasePackageItemParams - a model defined in OpenAPI"""  # noqa: E501

        self._properties = None
        self._id = None
        self._version_id = None
        self._document_id = None
        self._workspace_id = None
        self._element_id = None
        self._part_id = None
        self._href = None
        self._configuration = None
        self._part_number = None
        self._is_included = None
        self.discriminator = None

        if properties is not None:
            self.properties = properties
        if id is not None:
            self.id = id
        if version_id is not None:
            self.version_id = version_id
        if document_id is not None:
            self.document_id = document_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if element_id is not None:
            self.element_id = element_id
        if part_id is not None:
            self.part_id = part_id
        if href is not None:
            self.href = href
        if configuration is not None:
            self.configuration = configuration
        if part_number is not None:
            self.part_number = part_number
        if is_included is not None:
            self.is_included = is_included

    @property
    def properties(self):
        """Gets the properties of this BTReleasePackageItemParams.  # noqa: E501


        :return: The properties of this BTReleasePackageItemParams.  # noqa: E501
        :rtype: list[BTPropertyValueParam]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this BTReleasePackageItemParams.


        :param properties: The properties of this BTReleasePackageItemParams.  # noqa: E501
        :type: list[BTPropertyValueParam]
        """

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this BTReleasePackageItemParams.  # noqa: E501


        :return: The id of this BTReleasePackageItemParams.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTReleasePackageItemParams.


        :param id: The id of this BTReleasePackageItemParams.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def version_id(self):
        """Gets the version_id of this BTReleasePackageItemParams.  # noqa: E501


        :return: The version_id of this BTReleasePackageItemParams.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTReleasePackageItemParams.


        :param version_id: The version_id of this BTReleasePackageItemParams.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def document_id(self):
        """Gets the document_id of this BTReleasePackageItemParams.  # noqa: E501


        :return: The document_id of this BTReleasePackageItemParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTReleasePackageItemParams.


        :param document_id: The document_id of this BTReleasePackageItemParams.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTReleasePackageItemParams.  # noqa: E501


        :return: The workspace_id of this BTReleasePackageItemParams.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTReleasePackageItemParams.


        :param workspace_id: The workspace_id of this BTReleasePackageItemParams.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def element_id(self):
        """Gets the element_id of this BTReleasePackageItemParams.  # noqa: E501


        :return: The element_id of this BTReleasePackageItemParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTReleasePackageItemParams.


        :param element_id: The element_id of this BTReleasePackageItemParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def part_id(self):
        """Gets the part_id of this BTReleasePackageItemParams.  # noqa: E501


        :return: The part_id of this BTReleasePackageItemParams.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this BTReleasePackageItemParams.


        :param part_id: The part_id of this BTReleasePackageItemParams.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

    @property
    def href(self):
        """Gets the href of this BTReleasePackageItemParams.  # noqa: E501


        :return: The href of this BTReleasePackageItemParams.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTReleasePackageItemParams.


        :param href: The href of this BTReleasePackageItemParams.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def configuration(self):
        """Gets the configuration of this BTReleasePackageItemParams.  # noqa: E501


        :return: The configuration of this BTReleasePackageItemParams.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this BTReleasePackageItemParams.


        :param configuration: The configuration of this BTReleasePackageItemParams.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def part_number(self):
        """Gets the part_number of this BTReleasePackageItemParams.  # noqa: E501


        :return: The part_number of this BTReleasePackageItemParams.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this BTReleasePackageItemParams.


        :param part_number: The part_number of this BTReleasePackageItemParams.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def is_included(self):
        """Gets the is_included of this BTReleasePackageItemParams.  # noqa: E501


        :return: The is_included of this BTReleasePackageItemParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_included

    @is_included.setter
    def is_included(self, is_included):
        """Sets the is_included of this BTReleasePackageItemParams.


        :param is_included: The is_included of this BTReleasePackageItemParams.  # noqa: E501
        :type: bool
        """

        self._is_included = is_included

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
        if not isinstance(other, BTReleasePackageItemParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
