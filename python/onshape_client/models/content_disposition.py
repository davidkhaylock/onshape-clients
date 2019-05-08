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


class ContentDisposition(object):
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
        'type': 'str',
        'parameters': 'dict(str, str)',
        'file_name': 'str',
        'creation_date': 'datetime',
        'modification_date': 'datetime',
        'read_date': 'datetime',
        'size': 'int'
    }

    attribute_map = {
        'type': 'type',
        'parameters': 'parameters',
        'file_name': 'fileName',
        'creation_date': 'creationDate',
        'modification_date': 'modificationDate',
        'read_date': 'readDate',
        'size': 'size'
    }

    def __init__(self, type=None, parameters=None, file_name=None, creation_date=None, modification_date=None, read_date=None, size=None):  # noqa: E501
        """ContentDisposition - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._parameters = None
        self._file_name = None
        self._creation_date = None
        self._modification_date = None
        self._read_date = None
        self._size = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if parameters is not None:
            self.parameters = parameters
        if file_name is not None:
            self.file_name = file_name
        if creation_date is not None:
            self.creation_date = creation_date
        if modification_date is not None:
            self.modification_date = modification_date
        if read_date is not None:
            self.read_date = read_date
        if size is not None:
            self.size = size

    @property
    def type(self):
        """Gets the type of this ContentDisposition.  # noqa: E501


        :return: The type of this ContentDisposition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ContentDisposition.


        :param type: The type of this ContentDisposition.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def parameters(self):
        """Gets the parameters of this ContentDisposition.  # noqa: E501


        :return: The parameters of this ContentDisposition.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ContentDisposition.


        :param parameters: The parameters of this ContentDisposition.  # noqa: E501
        :type: dict(str, str)
        """

        self._parameters = parameters

    @property
    def file_name(self):
        """Gets the file_name of this ContentDisposition.  # noqa: E501


        :return: The file_name of this ContentDisposition.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ContentDisposition.


        :param file_name: The file_name of this ContentDisposition.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def creation_date(self):
        """Gets the creation_date of this ContentDisposition.  # noqa: E501


        :return: The creation_date of this ContentDisposition.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ContentDisposition.


        :param creation_date: The creation_date of this ContentDisposition.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def modification_date(self):
        """Gets the modification_date of this ContentDisposition.  # noqa: E501


        :return: The modification_date of this ContentDisposition.  # noqa: E501
        :rtype: datetime
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this ContentDisposition.


        :param modification_date: The modification_date of this ContentDisposition.  # noqa: E501
        :type: datetime
        """

        self._modification_date = modification_date

    @property
    def read_date(self):
        """Gets the read_date of this ContentDisposition.  # noqa: E501


        :return: The read_date of this ContentDisposition.  # noqa: E501
        :rtype: datetime
        """
        return self._read_date

    @read_date.setter
    def read_date(self, read_date):
        """Sets the read_date of this ContentDisposition.


        :param read_date: The read_date of this ContentDisposition.  # noqa: E501
        :type: datetime
        """

        self._read_date = read_date

    @property
    def size(self):
        """Gets the size of this ContentDisposition.  # noqa: E501


        :return: The size of this ContentDisposition.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ContentDisposition.


        :param size: The size of this ContentDisposition.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if not isinstance(other, ContentDisposition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
