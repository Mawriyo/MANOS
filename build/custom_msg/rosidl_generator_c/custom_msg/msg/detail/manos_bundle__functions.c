// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_msg:msg/MANOSBundle.idl
// generated code does not contain a copyright notice
#include "custom_msg/msg/detail/manos_bundle__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `data`
// Member `type`
// Member `topic`
#include "rosidl_runtime_c/string_functions.h"

bool
custom_msg__msg__MANOSBundle__init(custom_msg__msg__MANOSBundle * msg)
{
  if (!msg) {
    return false;
  }
  // data
  if (!rosidl_runtime_c__String__Sequence__init(&msg->data, 0)) {
    custom_msg__msg__MANOSBundle__fini(msg);
    return false;
  }
  // type
  if (!rosidl_runtime_c__String__init(&msg->type)) {
    custom_msg__msg__MANOSBundle__fini(msg);
    return false;
  }
  // topic
  if (!rosidl_runtime_c__String__init(&msg->topic)) {
    custom_msg__msg__MANOSBundle__fini(msg);
    return false;
  }
  return true;
}

void
custom_msg__msg__MANOSBundle__fini(custom_msg__msg__MANOSBundle * msg)
{
  if (!msg) {
    return;
  }
  // data
  rosidl_runtime_c__String__Sequence__fini(&msg->data);
  // type
  rosidl_runtime_c__String__fini(&msg->type);
  // topic
  rosidl_runtime_c__String__fini(&msg->topic);
}

bool
custom_msg__msg__MANOSBundle__are_equal(const custom_msg__msg__MANOSBundle * lhs, const custom_msg__msg__MANOSBundle * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // data
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->data), &(rhs->data)))
  {
    return false;
  }
  // type
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->type), &(rhs->type)))
  {
    return false;
  }
  // topic
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->topic), &(rhs->topic)))
  {
    return false;
  }
  return true;
}

bool
custom_msg__msg__MANOSBundle__copy(
  const custom_msg__msg__MANOSBundle * input,
  custom_msg__msg__MANOSBundle * output)
{
  if (!input || !output) {
    return false;
  }
  // data
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->data), &(output->data)))
  {
    return false;
  }
  // type
  if (!rosidl_runtime_c__String__copy(
      &(input->type), &(output->type)))
  {
    return false;
  }
  // topic
  if (!rosidl_runtime_c__String__copy(
      &(input->topic), &(output->topic)))
  {
    return false;
  }
  return true;
}

custom_msg__msg__MANOSBundle *
custom_msg__msg__MANOSBundle__create()
{
  custom_msg__msg__MANOSBundle * msg = (custom_msg__msg__MANOSBundle *)malloc(sizeof(custom_msg__msg__MANOSBundle));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_msg__msg__MANOSBundle));
  bool success = custom_msg__msg__MANOSBundle__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
custom_msg__msg__MANOSBundle__destroy(custom_msg__msg__MANOSBundle * msg)
{
  if (msg) {
    custom_msg__msg__MANOSBundle__fini(msg);
  }
  free(msg);
}


bool
custom_msg__msg__MANOSBundle__Sequence__init(custom_msg__msg__MANOSBundle__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  custom_msg__msg__MANOSBundle * data = NULL;
  if (size) {
    data = (custom_msg__msg__MANOSBundle *)calloc(size, sizeof(custom_msg__msg__MANOSBundle));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_msg__msg__MANOSBundle__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_msg__msg__MANOSBundle__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
custom_msg__msg__MANOSBundle__Sequence__fini(custom_msg__msg__MANOSBundle__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      custom_msg__msg__MANOSBundle__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

custom_msg__msg__MANOSBundle__Sequence *
custom_msg__msg__MANOSBundle__Sequence__create(size_t size)
{
  custom_msg__msg__MANOSBundle__Sequence * array = (custom_msg__msg__MANOSBundle__Sequence *)malloc(sizeof(custom_msg__msg__MANOSBundle__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = custom_msg__msg__MANOSBundle__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
custom_msg__msg__MANOSBundle__Sequence__destroy(custom_msg__msg__MANOSBundle__Sequence * array)
{
  if (array) {
    custom_msg__msg__MANOSBundle__Sequence__fini(array);
  }
  free(array);
}

bool
custom_msg__msg__MANOSBundle__Sequence__are_equal(const custom_msg__msg__MANOSBundle__Sequence * lhs, const custom_msg__msg__MANOSBundle__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_msg__msg__MANOSBundle__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_msg__msg__MANOSBundle__Sequence__copy(
  const custom_msg__msg__MANOSBundle__Sequence * input,
  custom_msg__msg__MANOSBundle__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_msg__msg__MANOSBundle);
    custom_msg__msg__MANOSBundle * data =
      (custom_msg__msg__MANOSBundle *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_msg__msg__MANOSBundle__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          custom_msg__msg__MANOSBundle__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!custom_msg__msg__MANOSBundle__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
