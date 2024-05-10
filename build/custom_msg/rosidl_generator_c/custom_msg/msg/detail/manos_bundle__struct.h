// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_msg:msg/MANOSBundle.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSG__MSG__DETAIL__MANOS_BUNDLE__STRUCT_H_
#define CUSTOM_MSG__MSG__DETAIL__MANOS_BUNDLE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'data'
// Member 'type'
// Member 'topic'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/MANOSBundle in the package custom_msg.
typedef struct custom_msg__msg__MANOSBundle
{
  rosidl_runtime_c__String__Sequence data;
  rosidl_runtime_c__String type;
  rosidl_runtime_c__String topic;
} custom_msg__msg__MANOSBundle;

// Struct for a sequence of custom_msg__msg__MANOSBundle.
typedef struct custom_msg__msg__MANOSBundle__Sequence
{
  custom_msg__msg__MANOSBundle * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_msg__msg__MANOSBundle__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_MSG__MSG__DETAIL__MANOS_BUNDLE__STRUCT_H_
