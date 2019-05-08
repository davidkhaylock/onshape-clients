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


class BTTraceSamplingRateParams(object):
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
        'sampling_rate': 'float'
    }

    attribute_map = {
        'sampling_rate': 'samplingRate'
    }

    def __init__(self, sampling_rate=None):  # noqa: E501
        """BTTraceSamplingRateParams - a model defined in OpenAPI"""  # noqa: E501

        self._sampling_rate = None
        self.discriminator = None

        if sampling_rate is not None:
            self.sampling_rate = sampling_rate

    @property
    def sampling_rate(self):
        """Gets the sampling_rate of this BTTraceSamplingRateParams.  # noqa: E501


        :return: The sampling_rate of this BTTraceSamplingRateParams.  # noqa: E501
        :rtype: float
        """
        return self._sampling_rate

    @sampling_rate.setter
    def sampling_rate(self, sampling_rate):
        """Sets the sampling_rate of this BTTraceSamplingRateParams.


        :param sampling_rate: The sampling_rate of this BTTraceSamplingRateParams.  # noqa: E501
        :type: float
        """

        self._sampling_rate = sampling_rate

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
        if not isinstance(other, BTTraceSamplingRateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
