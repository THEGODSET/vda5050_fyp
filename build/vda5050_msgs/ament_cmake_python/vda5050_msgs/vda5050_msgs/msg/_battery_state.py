# generated from rosidl_generator_py/resource/_idl.py.em
# with input from vda5050_msgs:msg/BatteryState.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_BatteryState(type):
    """Metaclass of message 'BatteryState'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('vda5050_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'vda5050_msgs.msg.BatteryState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__battery_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__battery_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__battery_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__battery_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__battery_state

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class BatteryState(metaclass=Metaclass_BatteryState):
    """Message class 'BatteryState'."""

    __slots__ = [
        '_battery_charge',
        '_battery_voltage',
        '_battery_health',
        '_charging',
        '_reach',
    ]

    _fields_and_field_types = {
        'battery_charge': 'double',
        'battery_voltage': 'double',
        'battery_health': 'int8',
        'charging': 'boolean',
        'reach': 'uint32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.battery_charge = kwargs.get('battery_charge', float())
        self.battery_voltage = kwargs.get('battery_voltage', float())
        self.battery_health = kwargs.get('battery_health', int())
        self.charging = kwargs.get('charging', bool())
        self.reach = kwargs.get('reach', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.battery_charge != other.battery_charge:
            return False
        if self.battery_voltage != other.battery_voltage:
            return False
        if self.battery_health != other.battery_health:
            return False
        if self.charging != other.charging:
            return False
        if self.reach != other.reach:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def battery_charge(self):
        """Message field 'battery_charge'."""
        return self._battery_charge

    @battery_charge.setter
    def battery_charge(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'battery_charge' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'battery_charge' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._battery_charge = value

    @builtins.property
    def battery_voltage(self):
        """Message field 'battery_voltage'."""
        return self._battery_voltage

    @battery_voltage.setter
    def battery_voltage(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'battery_voltage' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'battery_voltage' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._battery_voltage = value

    @builtins.property
    def battery_health(self):
        """Message field 'battery_health'."""
        return self._battery_health

    @battery_health.setter
    def battery_health(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'battery_health' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'battery_health' field must be an integer in [-128, 127]"
        self._battery_health = value

    @builtins.property
    def charging(self):
        """Message field 'charging'."""
        return self._charging

    @charging.setter
    def charging(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'charging' field must be of type 'bool'"
        self._charging = value

    @builtins.property
    def reach(self):
        """Message field 'reach'."""
        return self._reach

    @reach.setter
    def reach(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'reach' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'reach' field must be an unsigned integer in [0, 4294967295]"
        self._reach = value
