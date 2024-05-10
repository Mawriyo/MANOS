// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from servo_control:srv/SetServo.idl
// generated code does not contain a copyright notice
#include "servo_control/srv/detail/set_servo__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "servo_control/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "servo_control/srv/detail/set_servo__struct.h"
#include "servo_control/srv/detail/set_servo__functions.h"
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


using _SetServo_Request__ros_msg_type = servo_control__srv__SetServo_Request;

static bool _SetServo_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _SetServo_Request__ros_msg_type * ros_message = static_cast<const _SetServo_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: id
  {
    cdr << ros_message->id;
  }

  // Field name: position
  {
    cdr << ros_message->position;
  }

  return true;
}

static bool _SetServo_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _SetServo_Request__ros_msg_type * ros_message = static_cast<_SetServo_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: id
  {
    cdr >> ros_message->id;
  }

  // Field name: position
  {
    cdr >> ros_message->position;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_servo_control
size_t get_serialized_size_servo_control__srv__SetServo_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _SetServo_Request__ros_msg_type * ros_message = static_cast<const _SetServo_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name id
  {
    size_t item_size = sizeof(ros_message->id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name position
  {
    size_t item_size = sizeof(ros_message->position);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _SetServo_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_servo_control__srv__SetServo_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_servo_control
size_t max_serialized_size_servo_control__srv__SetServo_Request(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: position
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _SetServo_Request__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_servo_control__srv__SetServo_Request(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_SetServo_Request = {
  "servo_control::srv",
  "SetServo_Request",
  _SetServo_Request__cdr_serialize,
  _SetServo_Request__cdr_deserialize,
  _SetServo_Request__get_serialized_size,
  _SetServo_Request__max_serialized_size
};

static rosidl_message_type_support_t _SetServo_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_SetServo_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, servo_control, srv, SetServo_Request)() {
  return &_SetServo_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "servo_control/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "servo_control/srv/detail/set_servo__struct.h"
// already included above
// #include "servo_control/srv/detail/set_servo__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

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


using _SetServo_Response__ros_msg_type = servo_control__srv__SetServo_Response;

static bool _SetServo_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _SetServo_Response__ros_msg_type * ros_message = static_cast<const _SetServo_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    cdr << (ros_message->success ? true : false);
  }

  return true;
}

static bool _SetServo_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _SetServo_Response__ros_msg_type * ros_message = static_cast<_SetServo_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->success = tmp ? true : false;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_servo_control
size_t get_serialized_size_servo_control__srv__SetServo_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _SetServo_Response__ros_msg_type * ros_message = static_cast<const _SetServo_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name success
  {
    size_t item_size = sizeof(ros_message->success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _SetServo_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_servo_control__srv__SetServo_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_servo_control
size_t max_serialized_size_servo_control__srv__SetServo_Response(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: success
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _SetServo_Response__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_servo_control__srv__SetServo_Response(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_SetServo_Response = {
  "servo_control::srv",
  "SetServo_Response",
  _SetServo_Response__cdr_serialize,
  _SetServo_Response__cdr_deserialize,
  _SetServo_Response__get_serialized_size,
  _SetServo_Response__max_serialized_size
};

static rosidl_message_type_support_t _SetServo_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_SetServo_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, servo_control, srv, SetServo_Response)() {
  return &_SetServo_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "servo_control/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "servo_control/srv/set_servo.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t SetServo__callbacks = {
  "servo_control::srv",
  "SetServo",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, servo_control, srv, SetServo_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, servo_control, srv, SetServo_Response)(),
};

static rosidl_service_type_support_t SetServo__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &SetServo__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, servo_control, srv, SetServo)() {
  return &SetServo__handle;
}

#if defined(__cplusplus)
}
#endif
