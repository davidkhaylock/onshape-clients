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


class BTBillingAllowedPlansInfo(object):
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
        'current_plan': 'BTBillingPlanSummaryInfo',
        'upgrades': 'list[BTBillingPlanSummaryInfo]',
        'downgrades': 'list[BTBillingPlanSummaryInfo]'
    }

    attribute_map = {
        'current_plan': 'currentPlan',
        'upgrades': 'upgrades',
        'downgrades': 'downgrades'
    }

    def __init__(self, current_plan=None, upgrades=None, downgrades=None):  # noqa: E501
        """BTBillingAllowedPlansInfo - a model defined in OpenAPI"""  # noqa: E501

        self._current_plan = None
        self._upgrades = None
        self._downgrades = None
        self.discriminator = None

        if current_plan is not None:
            self.current_plan = current_plan
        if upgrades is not None:
            self.upgrades = upgrades
        if downgrades is not None:
            self.downgrades = downgrades

    @property
    def current_plan(self):
        """Gets the current_plan of this BTBillingAllowedPlansInfo.  # noqa: E501


        :return: The current_plan of this BTBillingAllowedPlansInfo.  # noqa: E501
        :rtype: BTBillingPlanSummaryInfo
        """
        return self._current_plan

    @current_plan.setter
    def current_plan(self, current_plan):
        """Sets the current_plan of this BTBillingAllowedPlansInfo.


        :param current_plan: The current_plan of this BTBillingAllowedPlansInfo.  # noqa: E501
        :type: BTBillingPlanSummaryInfo
        """

        self._current_plan = current_plan

    @property
    def upgrades(self):
        """Gets the upgrades of this BTBillingAllowedPlansInfo.  # noqa: E501


        :return: The upgrades of this BTBillingAllowedPlansInfo.  # noqa: E501
        :rtype: list[BTBillingPlanSummaryInfo]
        """
        return self._upgrades

    @upgrades.setter
    def upgrades(self, upgrades):
        """Sets the upgrades of this BTBillingAllowedPlansInfo.


        :param upgrades: The upgrades of this BTBillingAllowedPlansInfo.  # noqa: E501
        :type: list[BTBillingPlanSummaryInfo]
        """

        self._upgrades = upgrades

    @property
    def downgrades(self):
        """Gets the downgrades of this BTBillingAllowedPlansInfo.  # noqa: E501


        :return: The downgrades of this BTBillingAllowedPlansInfo.  # noqa: E501
        :rtype: list[BTBillingPlanSummaryInfo]
        """
        return self._downgrades

    @downgrades.setter
    def downgrades(self, downgrades):
        """Sets the downgrades of this BTBillingAllowedPlansInfo.


        :param downgrades: The downgrades of this BTBillingAllowedPlansInfo.  # noqa: E501
        :type: list[BTBillingPlanSummaryInfo]
        """

        self._downgrades = downgrades

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
        if not isinstance(other, BTBillingAllowedPlansInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
