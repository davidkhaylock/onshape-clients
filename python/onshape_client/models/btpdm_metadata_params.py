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


class BTPDMMetadataParams(object):
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
        'id': 'str',
        'state': 'str',
        'description': 'str',
        'revision': 'str',
        'project': 'str',
        'element_id': 'str',
        'part_id': 'str',
        'vendor': 'str',
        'product_line': 'str',
        'title1': 'str',
        'title2': 'str',
        'title3': 'str',
        'configuration': 'str',
        'part_number': 'str',
        'custom_properties': 'list[BTNameValuePair]'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'state': 'state',
        'description': 'description',
        'revision': 'revision',
        'project': 'project',
        'element_id': 'elementId',
        'part_id': 'partId',
        'vendor': 'vendor',
        'product_line': 'productLine',
        'title1': 'title1',
        'title2': 'title2',
        'title3': 'title3',
        'configuration': 'configuration',
        'part_number': 'partNumber',
        'custom_properties': 'customProperties'
    }

    def __init__(self, name=None, id=None, state=None, description=None, revision=None, project=None, element_id=None, part_id=None, vendor=None, product_line=None, title1=None, title2=None, title3=None, configuration=None, part_number=None, custom_properties=None):  # noqa: E501
        """BTPDMMetadataParams - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._id = None
        self._state = None
        self._description = None
        self._revision = None
        self._project = None
        self._element_id = None
        self._part_id = None
        self._vendor = None
        self._product_line = None
        self._title1 = None
        self._title2 = None
        self._title3 = None
        self._configuration = None
        self._part_number = None
        self._custom_properties = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if description is not None:
            self.description = description
        if revision is not None:
            self.revision = revision
        if project is not None:
            self.project = project
        if element_id is not None:
            self.element_id = element_id
        if part_id is not None:
            self.part_id = part_id
        if vendor is not None:
            self.vendor = vendor
        if product_line is not None:
            self.product_line = product_line
        if title1 is not None:
            self.title1 = title1
        if title2 is not None:
            self.title2 = title2
        if title3 is not None:
            self.title3 = title3
        if configuration is not None:
            self.configuration = configuration
        if part_number is not None:
            self.part_number = part_number
        if custom_properties is not None:
            self.custom_properties = custom_properties

    @property
    def name(self):
        """Gets the name of this BTPDMMetadataParams.  # noqa: E501


        :return: The name of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTPDMMetadataParams.


        :param name: The name of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTPDMMetadataParams.  # noqa: E501


        :return: The id of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTPDMMetadataParams.


        :param id: The id of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this BTPDMMetadataParams.  # noqa: E501


        :return: The state of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BTPDMMetadataParams.


        :param state: The state of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "PENDING", "RELEASED", "OBSOLETE", "REJECTED", "DISCARDED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def description(self):
        """Gets the description of this BTPDMMetadataParams.  # noqa: E501


        :return: The description of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTPDMMetadataParams.


        :param description: The description of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def revision(self):
        """Gets the revision of this BTPDMMetadataParams.  # noqa: E501


        :return: The revision of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this BTPDMMetadataParams.


        :param revision: The revision of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def project(self):
        """Gets the project of this BTPDMMetadataParams.  # noqa: E501


        :return: The project of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this BTPDMMetadataParams.


        :param project: The project of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def element_id(self):
        """Gets the element_id of this BTPDMMetadataParams.  # noqa: E501


        :return: The element_id of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTPDMMetadataParams.


        :param element_id: The element_id of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def part_id(self):
        """Gets the part_id of this BTPDMMetadataParams.  # noqa: E501


        :return: The part_id of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this BTPDMMetadataParams.


        :param part_id: The part_id of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

    @property
    def vendor(self):
        """Gets the vendor of this BTPDMMetadataParams.  # noqa: E501


        :return: The vendor of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this BTPDMMetadataParams.


        :param vendor: The vendor of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def product_line(self):
        """Gets the product_line of this BTPDMMetadataParams.  # noqa: E501


        :return: The product_line of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._product_line

    @product_line.setter
    def product_line(self, product_line):
        """Sets the product_line of this BTPDMMetadataParams.


        :param product_line: The product_line of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._product_line = product_line

    @property
    def title1(self):
        """Gets the title1 of this BTPDMMetadataParams.  # noqa: E501


        :return: The title1 of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._title1

    @title1.setter
    def title1(self, title1):
        """Sets the title1 of this BTPDMMetadataParams.


        :param title1: The title1 of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._title1 = title1

    @property
    def title2(self):
        """Gets the title2 of this BTPDMMetadataParams.  # noqa: E501


        :return: The title2 of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._title2

    @title2.setter
    def title2(self, title2):
        """Sets the title2 of this BTPDMMetadataParams.


        :param title2: The title2 of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._title2 = title2

    @property
    def title3(self):
        """Gets the title3 of this BTPDMMetadataParams.  # noqa: E501


        :return: The title3 of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._title3

    @title3.setter
    def title3(self, title3):
        """Sets the title3 of this BTPDMMetadataParams.


        :param title3: The title3 of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._title3 = title3

    @property
    def configuration(self):
        """Gets the configuration of this BTPDMMetadataParams.  # noqa: E501


        :return: The configuration of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this BTPDMMetadataParams.


        :param configuration: The configuration of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def part_number(self):
        """Gets the part_number of this BTPDMMetadataParams.  # noqa: E501


        :return: The part_number of this BTPDMMetadataParams.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this BTPDMMetadataParams.


        :param part_number: The part_number of this BTPDMMetadataParams.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def custom_properties(self):
        """Gets the custom_properties of this BTPDMMetadataParams.  # noqa: E501


        :return: The custom_properties of this BTPDMMetadataParams.  # noqa: E501
        :rtype: list[BTNameValuePair]
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this BTPDMMetadataParams.


        :param custom_properties: The custom_properties of this BTPDMMetadataParams.  # noqa: E501
        :type: list[BTNameValuePair]
        """

        self._custom_properties = custom_properties

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
        if not isinstance(other, BTPDMMetadataParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
