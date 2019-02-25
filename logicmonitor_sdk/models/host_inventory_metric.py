# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class HostInventoryMetric(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data_source_id': 'int',
        'instances': 'str',
        'data_source_full_name': 'str'
    }

    attribute_map = {
        'data_source_id': 'dataSourceId',
        'instances': 'instances',
        'data_source_full_name': 'dataSourceFullName'
    }

    def __init__(self, data_source_id=None, instances=None, data_source_full_name=None):  # noqa: E501
        """HostInventoryMetric - a model defined in Swagger"""  # noqa: E501

        self._data_source_id = None
        self._instances = None
        self._data_source_full_name = None
        self.discriminator = None

        self.data_source_id = data_source_id
        if instances is not None:
            self.instances = instances
        if data_source_full_name is not None:
            self.data_source_full_name = data_source_full_name

    @property
    def data_source_id(self):
        """Gets the data_source_id of this HostInventoryMetric.  # noqa: E501


        :return: The data_source_id of this HostInventoryMetric.  # noqa: E501
        :rtype: int
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this HostInventoryMetric.


        :param data_source_id: The data_source_id of this HostInventoryMetric.  # noqa: E501
        :type: int
        """
        if data_source_id is None:
            raise ValueError("Invalid value for `data_source_id`, must not be `None`")  # noqa: E501

        self._data_source_id = data_source_id

    @property
    def instances(self):
        """Gets the instances of this HostInventoryMetric.  # noqa: E501


        :return: The instances of this HostInventoryMetric.  # noqa: E501
        :rtype: str
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this HostInventoryMetric.


        :param instances: The instances of this HostInventoryMetric.  # noqa: E501
        :type: str
        """

        self._instances = instances

    @property
    def data_source_full_name(self):
        """Gets the data_source_full_name of this HostInventoryMetric.  # noqa: E501


        :return: The data_source_full_name of this HostInventoryMetric.  # noqa: E501
        :rtype: str
        """
        return self._data_source_full_name

    @data_source_full_name.setter
    def data_source_full_name(self, data_source_full_name):
        """Sets the data_source_full_name of this HostInventoryMetric.


        :param data_source_full_name: The data_source_full_name of this HostInventoryMetric.  # noqa: E501
        :type: str
        """

        self._data_source_full_name = data_source_full_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(HostInventoryMetric, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HostInventoryMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other