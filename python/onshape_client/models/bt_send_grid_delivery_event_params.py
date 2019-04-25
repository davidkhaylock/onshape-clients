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


class BTSendGridDeliveryEventParams(object):
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
        'ip': 'str',
        'smtpid': 'str',
        'event': 'str',
        'timestamp': 'int',
        'email': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'smtpid': 'smtpid',
        'event': 'event',
        'timestamp': 'timestamp',
        'email': 'email'
    }

    def __init__(self, ip=None, smtpid=None, event=None, timestamp=None, email=None):  # noqa: E501
        """BTSendGridDeliveryEventParams - a model defined in OpenAPI"""  # noqa: E501

        self._ip = None
        self._smtpid = None
        self._event = None
        self._timestamp = None
        self._email = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if smtpid is not None:
            self.smtpid = smtpid
        if event is not None:
            self.event = event
        if timestamp is not None:
            self.timestamp = timestamp
        if email is not None:
            self.email = email

    @property
    def ip(self):
        """Gets the ip of this BTSendGridDeliveryEventParams.  # noqa: E501


        :return: The ip of this BTSendGridDeliveryEventParams.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this BTSendGridDeliveryEventParams.


        :param ip: The ip of this BTSendGridDeliveryEventParams.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def smtpid(self):
        """Gets the smtpid of this BTSendGridDeliveryEventParams.  # noqa: E501


        :return: The smtpid of this BTSendGridDeliveryEventParams.  # noqa: E501
        :rtype: str
        """
        return self._smtpid

    @smtpid.setter
    def smtpid(self, smtpid):
        """Sets the smtpid of this BTSendGridDeliveryEventParams.


        :param smtpid: The smtpid of this BTSendGridDeliveryEventParams.  # noqa: E501
        :type: str
        """

        self._smtpid = smtpid

    @property
    def event(self):
        """Gets the event of this BTSendGridDeliveryEventParams.  # noqa: E501


        :return: The event of this BTSendGridDeliveryEventParams.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this BTSendGridDeliveryEventParams.


        :param event: The event of this BTSendGridDeliveryEventParams.  # noqa: E501
        :type: str
        """

        self._event = event

    @property
    def timestamp(self):
        """Gets the timestamp of this BTSendGridDeliveryEventParams.  # noqa: E501


        :return: The timestamp of this BTSendGridDeliveryEventParams.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BTSendGridDeliveryEventParams.


        :param timestamp: The timestamp of this BTSendGridDeliveryEventParams.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def email(self):
        """Gets the email of this BTSendGridDeliveryEventParams.  # noqa: E501


        :return: The email of this BTSendGridDeliveryEventParams.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BTSendGridDeliveryEventParams.


        :param email: The email of this BTSendGridDeliveryEventParams.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if not isinstance(other, BTSendGridDeliveryEventParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
