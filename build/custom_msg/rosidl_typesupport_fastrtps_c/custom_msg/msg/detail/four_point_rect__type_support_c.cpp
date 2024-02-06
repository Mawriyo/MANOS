// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from custom_msg:msg/FourPointRect.idl
// generated code does not contain a copyright notice
#include "custom_msg/msg/detail/four_point_rect__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "custom_msg/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "custom_msg/msg/detail/four_point_rect__struct.h"
#include "custom_msg/msg/detail/four_point_rect__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _FourPointRect__ros_msg_type = custom_msg__msg__FourPointRect;

static bool _FourPointRect__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _FourPointRect__ros_msg_type * ros_message = static_cast<const _FourPointRect__ros_msg_type *>(untyped_ros_message);
  // Field name: xmin
  {
    cdr << ros_message->xmin;
  }

  // Field name: xmax
  {
    cdr << ros_message->xmax;
  }

  // Field name: ymin
  {
    cdr << ros_message->ymin;
  }

  // Field name: ymax
  {
    cdr << ros_message->ymax;
  }

  return true;
}

static bool _FourPointRect__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _FourPointRect__ros_msg_type * ros_message = static_cast<_FourPointRect__ros_msg_type *>(untyped_ros_message);
  // Field name: xmin
  {
    cdr >> ros_message->xmin;
  }

  // Field name: xmax
  {
    cdr >> ros_message->xmax;
  }

  // Field name: ymin
  {
    cdr >> ros_message->ymin;
  }

  // Field name: ymax
  {
    cdr >> ros_message->ymax;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_msg
size_t get_serialized_size_custom_msg__msg__FourPointRect(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _FourPointRect__ros_msg_type * ros_message = static_cast<const _FourPointRect__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name xmin
  {
    size_t item_size = sizeof(ros_message->xmin);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name xmax
  {
    size_t item_size = sizeof(ros_message->xmax);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ymin
  {
    size_t item_size = sizeof(ros_message->ymin);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ymax
  {
    size_t item_size = sizeof(ros_message->ymax);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _FourPointRect__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_custom_msg__msg__FourPointRect(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_custom_msg
size_t max_serialized_size_custom_msg__msg__FourPointRect(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: xmin
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: xmax
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ymin
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ymax
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _FourPointRect__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_custom_msg__msg__FourPointRect(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_FourPointRect = {
  "custom_msg::msg",
  "FourPointRect",
  _FourPointRect__cdr_serialize,
  _FourPointRect__cdr_deserialize,
  _FourPointRect__get_serialized_size,
  _FourPointRect__max_serialized_size
};

static rosidl_message_type_support_t _FourPointRect__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_FourPointRect,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, custom_msg, msg, FourPointRect)() {
  return &_FourPointRect__type_support;
}

#if defined(__cplusplus)
}
#endif
