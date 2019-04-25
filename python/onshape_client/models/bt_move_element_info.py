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


class BTMoveElementInfo(object):
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
        'new_document_version_id': 'str',
        'element_original_to_new_map': 'dict(str, str)',
        'is_new_document': 'bool',
        'error_message': 'str',
        'new_document_id': 'str',
        'new_document_name': 'str',
        'new_workspace_id': 'str'
    }

    attribute_map = {
        'new_document_version_id': 'newDocumentVersionId',
        'element_original_to_new_map': 'elementOriginalToNewMap',
        'is_new_document': 'isNewDocument',
        'error_message': 'errorMessage',
        'new_document_id': 'newDocumentId',
        'new_document_name': 'newDocumentName',
        'new_workspace_id': 'newWorkspaceId'
    }

    def __init__(self, new_document_version_id=None, element_original_to_new_map=None, is_new_document=None, error_message=None, new_document_id=None, new_document_name=None, new_workspace_id=None):  # noqa: E501
        """BTMoveElementInfo - a model defined in OpenAPI"""  # noqa: E501

        self._new_document_version_id = None
        self._element_original_to_new_map = None
        self._is_new_document = None
        self._error_message = None
        self._new_document_id = None
        self._new_document_name = None
        self._new_workspace_id = None
        self.discriminator = None

        if new_document_version_id is not None:
            self.new_document_version_id = new_document_version_id
        if element_original_to_new_map is not None:
            self.element_original_to_new_map = element_original_to_new_map
        if is_new_document is not None:
            self.is_new_document = is_new_document
        if error_message is not None:
            self.error_message = error_message
        if new_document_id is not None:
            self.new_document_id = new_document_id
        if new_document_name is not None:
            self.new_document_name = new_document_name
        if new_workspace_id is not None:
            self.new_workspace_id = new_workspace_id

    @property
    def new_document_version_id(self):
        """Gets the new_document_version_id of this BTMoveElementInfo.  # noqa: E501


        :return: The new_document_version_id of this BTMoveElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._new_document_version_id

    @new_document_version_id.setter
    def new_document_version_id(self, new_document_version_id):
        """Sets the new_document_version_id of this BTMoveElementInfo.


        :param new_document_version_id: The new_document_version_id of this BTMoveElementInfo.  # noqa: E501
        :type: str
        """

        self._new_document_version_id = new_document_version_id

    @property
    def element_original_to_new_map(self):
        """Gets the element_original_to_new_map of this BTMoveElementInfo.  # noqa: E501


        :return: The element_original_to_new_map of this BTMoveElementInfo.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._element_original_to_new_map

    @element_original_to_new_map.setter
    def element_original_to_new_map(self, element_original_to_new_map):
        """Sets the element_original_to_new_map of this BTMoveElementInfo.


        :param element_original_to_new_map: The element_original_to_new_map of this BTMoveElementInfo.  # noqa: E501
        :type: dict(str, str)
        """

        self._element_original_to_new_map = element_original_to_new_map

    @property
    def is_new_document(self):
        """Gets the is_new_document of this BTMoveElementInfo.  # noqa: E501


        :return: The is_new_document of this BTMoveElementInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_new_document

    @is_new_document.setter
    def is_new_document(self, is_new_document):
        """Sets the is_new_document of this BTMoveElementInfo.


        :param is_new_document: The is_new_document of this BTMoveElementInfo.  # noqa: E501
        :type: bool
        """

        self._is_new_document = is_new_document

    @property
    def error_message(self):
        """Gets the error_message of this BTMoveElementInfo.  # noqa: E501


        :return: The error_message of this BTMoveElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this BTMoveElementInfo.


        :param error_message: The error_message of this BTMoveElementInfo.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def new_document_id(self):
        """Gets the new_document_id of this BTMoveElementInfo.  # noqa: E501


        :return: The new_document_id of this BTMoveElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._new_document_id

    @new_document_id.setter
    def new_document_id(self, new_document_id):
        """Sets the new_document_id of this BTMoveElementInfo.


        :param new_document_id: The new_document_id of this BTMoveElementInfo.  # noqa: E501
        :type: str
        """

        self._new_document_id = new_document_id

    @property
    def new_document_name(self):
        """Gets the new_document_name of this BTMoveElementInfo.  # noqa: E501


        :return: The new_document_name of this BTMoveElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._new_document_name

    @new_document_name.setter
    def new_document_name(self, new_document_name):
        """Sets the new_document_name of this BTMoveElementInfo.


        :param new_document_name: The new_document_name of this BTMoveElementInfo.  # noqa: E501
        :type: str
        """

        self._new_document_name = new_document_name

    @property
    def new_workspace_id(self):
        """Gets the new_workspace_id of this BTMoveElementInfo.  # noqa: E501


        :return: The new_workspace_id of this BTMoveElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._new_workspace_id

    @new_workspace_id.setter
    def new_workspace_id(self, new_workspace_id):
        """Sets the new_workspace_id of this BTMoveElementInfo.


        :param new_workspace_id: The new_workspace_id of this BTMoveElementInfo.  # noqa: E501
        :type: str
        """

        self._new_workspace_id = new_workspace_id

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
        if not isinstance(other, BTMoveElementInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
