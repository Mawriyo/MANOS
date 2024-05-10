// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from servo_control:srv/SetServo.idl
// generated code does not contain a copyright notice

#ifndef SERVO_CONTROL__SRV__DETAIL__SET_SERVO__STRUCT_H_
#define SERVO_CONTROL__SRV__DETAIL__SET_SERVO__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in srv/SetServo in the package servo_control.
typedef struct servo_control__srv__SetServo_Request
{
  int32_t id;
  int32_t position;
} servo_control__srv__SetServo_Request;

// Struct for a sequence of servo_control__srv__SetServo_Request.
typedef struct servo_control__srv__SetServo_Request__Sequence
{
  servo_control__srv__SetServo_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} servo_control__srv__SetServo_Request__Sequence;


// Constants defined in the message

// Struct defined in srv/SetServo in the package servo_control.
typedef struct servo_control__srv__SetServo_Response
{
  bool success;
} servo_control__srv__SetServo_Response;

// Struct for a sequence of servo_control__srv__SetServo_Response.
typedef struct servo_control__srv__SetServo_Response__Sequence
{
  servo_control__srv__SetServo_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} servo_control__srv__SetServo_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SERVO_CONTROL__SRV__DETAIL__SET_SERVO__STRUCT_H_
