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


class BTReleasePackageInfo(object):
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
        'package_thumbnail': 'str',
        'items': 'list[BTReleasePackageItemInfo]',
        'detailed': 'bool',
        'column_names': 'dict(str, str)',
        'comments': 'list[BTCommentInfo]',
        'workspace_id': 'str',
        'version_id': 'str',
        'revision_rule_id': 'str',
        'linked_version_ids': 'list[str]',
        'properties': 'list[BTWorkflowPropertyInfo]',
        'description': 'str',
        'workflow': 'BTWorkflowSnapshotInfo',
        'company_id': 'str',
        'is_obsoletion': 'bool',
        'document_id': 'str',
        'workflow_id': 'BTPublishedWorkflowId',
        'name_as_property': 'str',
        'description_as_property': 'str',
        'name': 'str',
        'id': 'str',
        'href': 'str',
        'view_ref': 'str'
    }

    attribute_map = {
        'package_thumbnail': 'packageThumbnail',
        'items': 'items',
        'detailed': 'detailed',
        'column_names': 'columnNames',
        'comments': 'comments',
        'workspace_id': 'workspaceId',
        'version_id': 'versionId',
        'revision_rule_id': 'revisionRuleId',
        'linked_version_ids': 'linkedVersionIds',
        'properties': 'properties',
        'description': 'description',
        'workflow': 'workflow',
        'company_id': 'companyId',
        'is_obsoletion': 'isObsoletion',
        'document_id': 'documentId',
        'workflow_id': 'workflowId',
        'name_as_property': 'nameAsProperty',
        'description_as_property': 'descriptionAsProperty',
        'name': 'name',
        'id': 'id',
        'href': 'href',
        'view_ref': 'viewRef'
    }

    def __init__(self, package_thumbnail=None, items=None, detailed=None, column_names=None, comments=None, workspace_id=None, version_id=None, revision_rule_id=None, linked_version_ids=None, properties=None, description=None, workflow=None, company_id=None, is_obsoletion=None, document_id=None, workflow_id=None, name_as_property=None, description_as_property=None, name=None, id=None, href=None, view_ref=None):  # noqa: E501
        """BTReleasePackageInfo - a model defined in OpenAPI"""  # noqa: E501

        self._package_thumbnail = None
        self._items = None
        self._detailed = None
        self._column_names = None
        self._comments = None
        self._workspace_id = None
        self._version_id = None
        self._revision_rule_id = None
        self._linked_version_ids = None
        self._properties = None
        self._description = None
        self._workflow = None
        self._company_id = None
        self._is_obsoletion = None
        self._document_id = None
        self._workflow_id = None
        self._name_as_property = None
        self._description_as_property = None
        self._name = None
        self._id = None
        self._href = None
        self._view_ref = None
        self.discriminator = None

        if package_thumbnail is not None:
            self.package_thumbnail = package_thumbnail
        if items is not None:
            self.items = items
        if detailed is not None:
            self.detailed = detailed
        if column_names is not None:
            self.column_names = column_names
        if comments is not None:
            self.comments = comments
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if version_id is not None:
            self.version_id = version_id
        if revision_rule_id is not None:
            self.revision_rule_id = revision_rule_id
        if linked_version_ids is not None:
            self.linked_version_ids = linked_version_ids
        if properties is not None:
            self.properties = properties
        if description is not None:
            self.description = description
        if workflow is not None:
            self.workflow = workflow
        if company_id is not None:
            self.company_id = company_id
        if is_obsoletion is not None:
            self.is_obsoletion = is_obsoletion
        if document_id is not None:
            self.document_id = document_id
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if name_as_property is not None:
            self.name_as_property = name_as_property
        if description_as_property is not None:
            self.description_as_property = description_as_property
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref

    @property
    def package_thumbnail(self):
        """Gets the package_thumbnail of this BTReleasePackageInfo.  # noqa: E501


        :return: The package_thumbnail of this BTReleasePackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._package_thumbnail

    @package_thumbnail.setter
    def package_thumbnail(self, package_thumbnail):
        """Sets the package_thumbnail of this BTReleasePackageInfo.


        :param package_thumbnail: The package_thumbnail of this BTReleasePackageInfo.  # noqa: E501
        :type: str
        """

        self._package_thumbnail = package_thumbnail

    @property
    def items(self):
        """Gets the items of this BTReleasePackageInfo.  # noqa: E501


        :return: The items of this BTReleasePackageInfo.  # noqa: E501
        :rtype: list[BTReleasePackageItemInfo]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this BTReleasePackageInfo.


        :param items: The items of this BTReleasePackageInfo.  # noqa: E501
        :type: list[BTReleasePackageItemInfo]
        """

        self._items = items

    @property
    def detailed(self):
        """Gets the detailed of this BTReleasePackageInfo.  # noqa: E501


        :return: The detailed of this BTReleasePackageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._detailed

    @detailed.setter
    def detailed(self, detailed):
        """Sets the detailed of this BTReleasePackageInfo.


        :param detailed: The detailed of this BTReleasePackageInfo.  # noqa: E501
        :type: bool
        """

        self._detailed = detailed

    @property
    def column_names(self):
        """Gets the column_names of this BTReleasePackageInfo.  # noqa: E501


        :return: The column_names of this BTReleasePackageInfo.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._column_names

    @column_names.setter
    def column_names(self, column_names):
        """Sets the column_names of this BTReleasePackageInfo.


        :param column_names: The column_names of this BTReleasePackageInfo.  # noqa: E501
        :type: dict(str, str)
        """

        self._column_names = column_names

    @property
    def comments(self):
        """Gets the comments of this BTReleasePackageInfo.  # noqa: E501


        :return: The comments of this BTReleasePackageInfo.  # noqa: E501
        :rtype: list[BTCommentInfo]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this BTReleasePackageInfo.


        :param comments: The comments of this BTReleasePackageInfo.  # noqa: E501
        :type: list[BTCommentInfo]
        """

        self._comments = comments

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTReleasePackageInfo.  # noqa: E501


        :return: The workspace_id of this BTReleasePackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTReleasePackageInfo.


        :param workspace_id: The workspace_id of this BTReleasePackageInfo.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def version_id(self):
        """Gets the version_id of this BTReleasePackageInfo.  # noqa: E501


        :return: The version_id of this BTReleasePackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTReleasePackageInfo.


        :param version_id: The version_id of this BTReleasePackageInfo.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def revision_rule_id(self):
        """Gets the revision_rule_id of this BTReleasePackageInfo.  # noqa: E501


        :return: The revision_rule_id of this BTReleasePackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._revision_rule_id

    @revision_rule_id.setter
    def revision_rule_id(self, revision_rule_id):
        """Sets the revision_rule_id of this BTReleasePackageInfo.


        :param revision_rule_id: The revision_rule_id of this BTReleasePackageInfo.  # noqa: E501
        :type: str
        """

        self._revision_rule_id = revision_rule_id

    @property
    def linked_version_ids(self):
        """Gets the linked_version_ids of this BTReleasePackageInfo.  # noqa: E501


        :return: The linked_version_ids of this BTReleasePackageInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._linked_version_ids

    @linked_version_ids.setter
    def linked_version_ids(self, linked_version_ids):
        """Sets the linked_version_ids of this BTReleasePackageInfo.


        :param linked_version_ids: The linked_version_ids of this BTReleasePackageInfo.  # noqa: E501
        :type: list[str]
        """

        self._linked_version_ids = linked_version_ids

    @property
    def properties(self):
        """Gets the properties of this BTReleasePackageInfo.  # noqa: E501


        :return: The properties of this BTReleasePackageInfo.  # noqa: E501
        :rtype: list[BTWorkflowPropertyInfo]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this BTReleasePackageInfo.


        :param properties: The properties of this BTReleasePackageInfo.  # noqa: E501
        :type: list[BTWorkflowPropertyInfo]
        """

        self._properties = properties

    @property
    def description(self):
        """Gets the description of this BTReleasePackageInfo.  # noqa: E501


        :return: The description of this BTReleasePackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTReleasePackageInfo.


        :param description: The description of this BTReleasePackageInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def workflow(self):
        """Gets the workflow of this BTReleasePackageInfo.  # noqa: E501


        :return: The workflow of this BTReleasePackageInfo.  # noqa: E501
        :rtype: BTWorkflowSnapshotInfo
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this BTReleasePackageInfo.


        :param workflow: The workflow of this BTReleasePackageInfo.  # noqa: E501
        :type: BTWorkflowSnapshotInfo
        """

        self._workflow = workflow

    @property
    def company_id(self):
        """Gets the company_id of this BTReleasePackageInfo.  # noqa: E501


        :return: The company_id of this BTReleasePackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this BTReleasePackageInfo.


        :param company_id: The company_id of this BTReleasePackageInfo.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def is_obsoletion(self):
        """Gets the is_obsoletion of this BTReleasePackageInfo.  # noqa: E501


        :return: The is_obsoletion of this BTReleasePackageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_obsoletion

    @is_obsoletion.setter
    def is_obsoletion(self, is_obsoletion):
        """Sets the is_obsoletion of this BTReleasePackageInfo.


        :param is_obsoletion: The is_obsoletion of this BTReleasePackageInfo.  # noqa: E501
        :type: bool
        """

        self._is_obsoletion = is_obsoletion

    @property
    def document_id(self):
        """Gets the document_id of this BTReleasePackageInfo.  # noqa: E501


        :return: The document_id of this BTReleasePackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTReleasePackageInfo.


        :param document_id: The document_id of this BTReleasePackageInfo.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this BTReleasePackageInfo.  # noqa: E501


        :return: The workflow_id of this BTReleasePackageInfo.  # noqa: E501
        :rtype: BTPublishedWorkflowId
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this BTReleasePackageInfo.


        :param workflow_id: The workflow_id of this BTReleasePackageInfo.  # noqa: E501
        :type: BTPublishedWorkflowId
        """

        self._workflow_id = workflow_id

    @property
    def name_as_property(self):
        """Gets the name_as_property of this BTReleasePackageInfo.  # noqa: E501


        :return: The name_as_property of this BTReleasePackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._name_as_property

    @name_as_property.setter
    def name_as_property(self, name_as_property):
        """Sets the name_as_property of this BTReleasePackageInfo.


        :param name_as_property: The name_as_property of this BTReleasePackageInfo.  # noqa: E501
        :type: str
        """

        self._name_as_property = name_as_property

    @property
    def description_as_property(self):
        """Gets the description_as_property of this BTReleasePackageInfo.  # noqa: E501


        :return: The description_as_property of this BTReleasePackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._description_as_property

    @description_as_property.setter
    def description_as_property(self, description_as_property):
        """Sets the description_as_property of this BTReleasePackageInfo.


        :param description_as_property: The description_as_property of this BTReleasePackageInfo.  # noqa: E501
        :type: str
        """

        self._description_as_property = description_as_property

    @property
    def name(self):
        """Gets the name of this BTReleasePackageInfo.  # noqa: E501


        :return: The name of this BTReleasePackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTReleasePackageInfo.


        :param name: The name of this BTReleasePackageInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTReleasePackageInfo.  # noqa: E501


        :return: The id of this BTReleasePackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTReleasePackageInfo.


        :param id: The id of this BTReleasePackageInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BTReleasePackageInfo.  # noqa: E501


        :return: The href of this BTReleasePackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTReleasePackageInfo.


        :param href: The href of this BTReleasePackageInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTReleasePackageInfo.  # noqa: E501


        :return: The view_ref of this BTReleasePackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTReleasePackageInfo.


        :param view_ref: The view_ref of this BTReleasePackageInfo.  # noqa: E501
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
        if not isinstance(other, BTReleasePackageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
