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


class BTInAppMessageContent(object):
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
        'title': 'str',
        'show_items': 'bool',
        'content_items': 'list[BTInAppMessageContentItem]',
        'max_num_survey_responses': 'int',
        'state': 'str'
    }

    attribute_map = {
        'title': 'title',
        'show_items': 'showItems',
        'content_items': 'contentItems',
        'max_num_survey_responses': 'maxNumSurveyResponses',
        'state': 'state'
    }

    def __init__(self, title=None, show_items=None, content_items=None, max_num_survey_responses=None, state=None):  # noqa: E501
        """BTInAppMessageContent - a model defined in OpenAPI"""  # noqa: E501

        self._title = None
        self._show_items = None
        self._content_items = None
        self._max_num_survey_responses = None
        self._state = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if show_items is not None:
            self.show_items = show_items
        if content_items is not None:
            self.content_items = content_items
        if max_num_survey_responses is not None:
            self.max_num_survey_responses = max_num_survey_responses
        if state is not None:
            self.state = state

    @property
    def title(self):
        """Gets the title of this BTInAppMessageContent.  # noqa: E501


        :return: The title of this BTInAppMessageContent.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BTInAppMessageContent.


        :param title: The title of this BTInAppMessageContent.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def show_items(self):
        """Gets the show_items of this BTInAppMessageContent.  # noqa: E501


        :return: The show_items of this BTInAppMessageContent.  # noqa: E501
        :rtype: bool
        """
        return self._show_items

    @show_items.setter
    def show_items(self, show_items):
        """Sets the show_items of this BTInAppMessageContent.


        :param show_items: The show_items of this BTInAppMessageContent.  # noqa: E501
        :type: bool
        """

        self._show_items = show_items

    @property
    def content_items(self):
        """Gets the content_items of this BTInAppMessageContent.  # noqa: E501


        :return: The content_items of this BTInAppMessageContent.  # noqa: E501
        :rtype: list[BTInAppMessageContentItem]
        """
        return self._content_items

    @content_items.setter
    def content_items(self, content_items):
        """Sets the content_items of this BTInAppMessageContent.


        :param content_items: The content_items of this BTInAppMessageContent.  # noqa: E501
        :type: list[BTInAppMessageContentItem]
        """

        self._content_items = content_items

    @property
    def max_num_survey_responses(self):
        """Gets the max_num_survey_responses of this BTInAppMessageContent.  # noqa: E501


        :return: The max_num_survey_responses of this BTInAppMessageContent.  # noqa: E501
        :rtype: int
        """
        return self._max_num_survey_responses

    @max_num_survey_responses.setter
    def max_num_survey_responses(self, max_num_survey_responses):
        """Sets the max_num_survey_responses of this BTInAppMessageContent.


        :param max_num_survey_responses: The max_num_survey_responses of this BTInAppMessageContent.  # noqa: E501
        :type: int
        """

        self._max_num_survey_responses = max_num_survey_responses

    @property
    def state(self):
        """Gets the state of this BTInAppMessageContent.  # noqa: E501


        :return: The state of this BTInAppMessageContent.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BTInAppMessageContent.


        :param state: The state of this BTInAppMessageContent.  # noqa: E501
        :type: str
        """
        allowed_values = ["DELETED", "TRASH", "ACTIVE"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, BTInAppMessageContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
