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


class BTShareParams(object):
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
        'message': 'str',
        'entries': 'list[BTShareEntryParams]',
        'permission': 'int',
        'document_id': 'str',
        'workspace_id': 'str',
        'element_id': 'str',
        'folder_id': 'str',
        'permission_set': 'BTPermissionSet',
        'update': 'bool',
        'encoded_configuration': 'str'
    }

    attribute_map = {
        'message': 'message',
        'entries': 'entries',
        'permission': 'permission',
        'document_id': 'documentId',
        'workspace_id': 'workspaceId',
        'element_id': 'elementId',
        'folder_id': 'folderId',
        'permission_set': 'permissionSet',
        'update': 'update',
        'encoded_configuration': 'encodedConfiguration'
    }

    def __init__(self, message=None, entries=None, permission=None, document_id=None, workspace_id=None, element_id=None, folder_id=None, permission_set=None, update=None, encoded_configuration=None):  # noqa: E501
        """BTShareParams - a model defined in OpenAPI"""  # noqa: E501

        self._message = None
        self._entries = None
        self._permission = None
        self._document_id = None
        self._workspace_id = None
        self._element_id = None
        self._folder_id = None
        self._permission_set = None
        self._update = None
        self._encoded_configuration = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if entries is not None:
            self.entries = entries
        if permission is not None:
            self.permission = permission
        if document_id is not None:
            self.document_id = document_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if element_id is not None:
            self.element_id = element_id
        if folder_id is not None:
            self.folder_id = folder_id
        if permission_set is not None:
            self.permission_set = permission_set
        if update is not None:
            self.update = update
        if encoded_configuration is not None:
            self.encoded_configuration = encoded_configuration

    @property
    def message(self):
        """Gets the message of this BTShareParams.  # noqa: E501


        :return: The message of this BTShareParams.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BTShareParams.


        :param message: The message of this BTShareParams.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def entries(self):
        """Gets the entries of this BTShareParams.  # noqa: E501


        :return: The entries of this BTShareParams.  # noqa: E501
        :rtype: list[BTShareEntryParams]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this BTShareParams.


        :param entries: The entries of this BTShareParams.  # noqa: E501
        :type: list[BTShareEntryParams]
        """

        self._entries = entries

    @property
    def permission(self):
        """Gets the permission of this BTShareParams.  # noqa: E501


        :return: The permission of this BTShareParams.  # noqa: E501
        :rtype: int
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this BTShareParams.


        :param permission: The permission of this BTShareParams.  # noqa: E501
        :type: int
        """

        self._permission = permission

    @property
    def document_id(self):
        """Gets the document_id of this BTShareParams.  # noqa: E501


        :return: The document_id of this BTShareParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTShareParams.


        :param document_id: The document_id of this BTShareParams.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTShareParams.  # noqa: E501


        :return: The workspace_id of this BTShareParams.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTShareParams.


        :param workspace_id: The workspace_id of this BTShareParams.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def element_id(self):
        """Gets the element_id of this BTShareParams.  # noqa: E501


        :return: The element_id of this BTShareParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTShareParams.


        :param element_id: The element_id of this BTShareParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def folder_id(self):
        """Gets the folder_id of this BTShareParams.  # noqa: E501


        :return: The folder_id of this BTShareParams.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this BTShareParams.


        :param folder_id: The folder_id of this BTShareParams.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def permission_set(self):
        """Gets the permission_set of this BTShareParams.  # noqa: E501


        :return: The permission_set of this BTShareParams.  # noqa: E501
        :rtype: BTPermissionSet
        """
        return self._permission_set

    @permission_set.setter
    def permission_set(self, permission_set):
        """Sets the permission_set of this BTShareParams.


        :param permission_set: The permission_set of this BTShareParams.  # noqa: E501
        :type: BTPermissionSet
        """

        self._permission_set = permission_set

    @property
    def update(self):
        """Gets the update of this BTShareParams.  # noqa: E501


        :return: The update of this BTShareParams.  # noqa: E501
        :rtype: bool
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this BTShareParams.


        :param update: The update of this BTShareParams.  # noqa: E501
        :type: bool
        """

        self._update = update

    @property
    def encoded_configuration(self):
        """Gets the encoded_configuration of this BTShareParams.  # noqa: E501


        :return: The encoded_configuration of this BTShareParams.  # noqa: E501
        :rtype: str
        """
        return self._encoded_configuration

    @encoded_configuration.setter
    def encoded_configuration(self, encoded_configuration):
        """Sets the encoded_configuration of this BTShareParams.


        :param encoded_configuration: The encoded_configuration of this BTShareParams.  # noqa: E501
        :type: str
        """

        self._encoded_configuration = encoded_configuration

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
        if not isinstance(other, BTShareParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
