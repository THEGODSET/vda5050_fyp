# generated from rosidl_generator_py/resource/_idl.py.em
# with input from vda5050_msgs:msg/Visualization.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Visualization(type):
    """Metaclass of message 'Visualization'."""

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
                'vda5050_msgs.msg.Visualization')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__visualization
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__visualization
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__visualization
            cls._TYPE_SUPPORT = module.type_support_msg__msg__visualization
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__visualization

            from vda5050_msgs.msg import AGVPosition
            if AGVPosition.__class__._TYPE_SUPPORT is None:
                AGVPosition.__class__.__import_type_support__()

            from vda5050_msgs.msg import Velocity
            if Velocity.__class__._TYPE_SUPPORT is None:
                Velocity.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Visualization(metaclass=Metaclass_Visualization):
    """Message class 'Visualization'."""

    __slots__ = [
        '_header_id',
        '_timestamp',
        '_version',
        '_manufacturer',
        '_serial_number',
        '_agv_position',
        '_velocity',
    ]

    _fields_and_field_types = {
        'header_id': 'uint32',
        'timestamp': 'string',
        'version': 'string',
        'manufacturer': 'string',
        'serial_number': 'string',
        'agv_position': 'vda5050_msgs/AGVPosition',
        'velocity': 'vda5050_msgs/Velocity',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['vda5050_msgs', 'msg'], 'AGVPosition'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['vda5050_msgs', 'msg'], 'Velocity'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.header_id = kwargs.get('header_id', int())
        self.timestamp = kwargs.get('timestamp', str())
        self.version = kwargs.get('version', str())
        self.manufacturer = kwargs.get('manufacturer', str())
        self.serial_number = kwargs.get('serial_number', str())
        from vda5050_msgs.msg import AGVPosition
        self.agv_position = kwargs.get('agv_position', AGVPosition())
        from vda5050_msgs.msg import Velocity
        self.velocity = kwargs.get('velocity', Velocity())

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
        if self.header_id != other.header_id:
            return False
        if self.timestamp != other.timestamp:
            return False
        if self.version != other.version:
            return False
        if self.manufacturer != other.manufacturer:
            return False
        if self.serial_number != other.serial_number:
            return False
        if self.agv_position != other.agv_position:
            return False
        if self.velocity != other.velocity:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header_id(self):
        """Message field 'header_id'."""
        return self._header_id

    @header_id.setter
    def header_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'header_id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'header_id' field must be an unsigned integer in [0, 4294967295]"
        self._header_id = value

    @builtins.property
    def timestamp(self):
        """Message field 'timestamp'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'timestamp' field must be of type 'str'"
        self._timestamp = value

    @builtins.property
    def version(self):
        """Message field 'version'."""
        return self._version

    @version.setter
    def version(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'version' field must be of type 'str'"
        self._version = value

    @builtins.property
    def manufacturer(self):
        """Message field 'manufacturer'."""
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'manufacturer' field must be of type 'str'"
        self._manufacturer = value

    @builtins.property
    def serial_number(self):
        """Message field 'serial_number'."""
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'serial_number' field must be of type 'str'"
        self._serial_number = value

    @builtins.property
    def agv_position(self):
        """Message field 'agv_position'."""
        return self._agv_position

    @agv_position.setter
    def agv_position(self, value):
        if __debug__:
            from vda5050_msgs.msg import AGVPosition
            assert \
                isinstance(value, AGVPosition), \
                "The 'agv_position' field must be a sub message of type 'AGVPosition'"
        self._agv_position = value

    @builtins.property
    def velocity(self):
        """Message field 'velocity'."""
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if __debug__:
            from vda5050_msgs.msg import Velocity
            assert \
                isinstance(value, Velocity), \
                "The 'velocity' field must be a sub message of type 'Velocity'"
        self._velocity = value
