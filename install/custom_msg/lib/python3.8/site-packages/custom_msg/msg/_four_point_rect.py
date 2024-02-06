# generated from rosidl_generator_py/resource/_idl.py.em
# with input from custom_msg:msg/FourPointRect.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FourPointRect(type):
    """Metaclass of message 'FourPointRect'."""

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
            module = import_type_support('custom_msg')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'custom_msg.msg.FourPointRect')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__four_point_rect
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__four_point_rect
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__four_point_rect
            cls._TYPE_SUPPORT = module.type_support_msg__msg__four_point_rect
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__four_point_rect

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class FourPointRect(metaclass=Metaclass_FourPointRect):
    """Message class 'FourPointRect'."""

    __slots__ = [
        '_xmin',
        '_xmax',
        '_ymin',
        '_ymax',
    ]

    _fields_and_field_types = {
        'xmin': 'float',
        'xmax': 'float',
        'ymin': 'float',
        'ymax': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.xmin = kwargs.get('xmin', float())
        self.xmax = kwargs.get('xmax', float())
        self.ymin = kwargs.get('ymin', float())
        self.ymax = kwargs.get('ymax', float())

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
        if self.xmin != other.xmin:
            return False
        if self.xmax != other.xmax:
            return False
        if self.ymin != other.ymin:
            return False
        if self.ymax != other.ymax:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def xmin(self):
        """Message field 'xmin'."""
        return self._xmin

    @xmin.setter
    def xmin(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'xmin' field must be of type 'float'"
        self._xmin = value

    @property
    def xmax(self):
        """Message field 'xmax'."""
        return self._xmax

    @xmax.setter
    def xmax(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'xmax' field must be of type 'float'"
        self._xmax = value

    @property
    def ymin(self):
        """Message field 'ymin'."""
        return self._ymin

    @ymin.setter
    def ymin(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ymin' field must be of type 'float'"
        self._ymin = value

    @property
    def ymax(self):
        """Message field 'ymax'."""
        return self._ymax

    @ymax.setter
    def ymax(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ymax' field must be of type 'float'"
        self._ymax = value
