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


class BTPublishWorkflowParams(object):
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
        'name': 'str',
        'description': 'str',
        'workspace_id': 'str',
        'element_id': 'str',
        'is_obsoletion': 'bool',
        'document_id': 'str',
        'workflow_type': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'workspace_id': 'workspaceId',
        'element_id': 'elementId',
        'is_obsoletion': 'isObsoletion',
        'document_id': 'documentId',
        'workflow_type': 'workflowType'
    }

    def __init__(self, name=None, description=None, workspace_id=None, element_id=None, is_obsoletion=None, document_id=None, workflow_type=None):  # noqa: E501
        """BTPublishWorkflowParams - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._description = None
        self._workspace_id = None
        self._element_id = None
        self._is_obsoletion = None
        self._document_id = None
        self._workflow_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if element_id is not None:
            self.element_id = element_id
        if is_obsoletion is not None:
            self.is_obsoletion = is_obsoletion
        if document_id is not None:
            self.document_id = document_id
        if workflow_type is not None:
            self.workflow_type = workflow_type

    @property
    def name(self):
        """Gets the name of this BTPublishWorkflowParams.  # noqa: E501


        :return: The name of this BTPublishWorkflowParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTPublishWorkflowParams.


        :param name: The name of this BTPublishWorkflowParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this BTPublishWorkflowParams.  # noqa: E501


        :return: The description of this BTPublishWorkflowParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTPublishWorkflowParams.


        :param description: The description of this BTPublishWorkflowParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTPublishWorkflowParams.  # noqa: E501


        :return: The workspace_id of this BTPublishWorkflowParams.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTPublishWorkflowParams.


        :param workspace_id: The workspace_id of this BTPublishWorkflowParams.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def element_id(self):
        """Gets the element_id of this BTPublishWorkflowParams.  # noqa: E501


        :return: The element_id of this BTPublishWorkflowParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTPublishWorkflowParams.


        :param element_id: The element_id of this BTPublishWorkflowParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def is_obsoletion(self):
        """Gets the is_obsoletion of this BTPublishWorkflowParams.  # noqa: E501


        :return: The is_obsoletion of this BTPublishWorkflowParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_obsoletion

    @is_obsoletion.setter
    def is_obsoletion(self, is_obsoletion):
        """Sets the is_obsoletion of this BTPublishWorkflowParams.


        :param is_obsoletion: The is_obsoletion of this BTPublishWorkflowParams.  # noqa: E501
        :type: bool
        """

        self._is_obsoletion = is_obsoletion

    @property
    def document_id(self):
        """Gets the document_id of this BTPublishWorkflowParams.  # noqa: E501


        :return: The document_id of this BTPublishWorkflowParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTPublishWorkflowParams.


        :param document_id: The document_id of this BTPublishWorkflowParams.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def workflow_type(self):
        """Gets the workflow_type of this BTPublishWorkflowParams.  # noqa: E501


        :return: The workflow_type of this BTPublishWorkflowParams.  # noqa: E501
        :rtype: int
        """
        return self._workflow_type

    @workflow_type.setter
    def workflow_type(self, workflow_type):
        """Sets the workflow_type of this BTPublishWorkflowParams.


        :param workflow_type: The workflow_type of this BTPublishWorkflowParams.  # noqa: E501
        :type: int
        """

        self._workflow_type = workflow_type

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
        if not isinstance(other, BTPublishWorkflowParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
