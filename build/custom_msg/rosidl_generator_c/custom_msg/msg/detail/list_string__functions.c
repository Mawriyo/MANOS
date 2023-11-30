// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_msg:msg/ListString.idl
// generated code does not contain a copyright notice
#include "custom_msg/msg/detail/list_string__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `data`
#include "rosidl_runtime_c/string_functions.h"

bool
custom_msg__msg__ListString__init(custom_msg__msg__ListString * msg)
{
  if (!msg) {
    return false;
  }
  // data
  if (!rosidl_runtime_c__String__Sequence__init(&msg->data, 0)) {
    custom_msg__msg__ListString__fini(msg);
    return false;
  }
  return true;
}

void
custom_msg__msg__ListString__fini(custom_msg__msg__ListString * msg)
{
  if (!msg) {
    return;
  }
  // data
  rosidl_runtime_c__String__Sequence__fini(&msg->data);
}

bool
custom_msg__msg__ListString__are_equal(const custom_msg__msg__ListString * lhs, const custom_msg__msg__ListString * rhs)
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
  return true;
}

bool
custom_msg__msg__ListString__copy(
  const custom_msg__msg__ListString * input,
  custom_msg__msg__ListString * output)
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
  return true;
}

custom_msg__msg__ListString *
custom_msg__msg__ListString__create()
{
  custom_msg__msg__ListString * msg = (custom_msg__msg__ListString *)malloc(sizeof(custom_msg__msg__ListString));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_msg__msg__ListString));
  bool success = custom_msg__msg__ListString__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
custom_msg__msg__ListString__destroy(custom_msg__msg__ListString * msg)
{
  if (msg) {
    custom_msg__msg__ListString__fini(msg);
  }
  free(msg);
}


bool
custom_msg__msg__ListString__Sequence__init(custom_msg__msg__ListString__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  custom_msg__msg__ListString * data = NULL;
  if (size) {
    data = (custom_msg__msg__ListString *)calloc(size, sizeof(custom_msg__msg__ListString));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_msg__msg__ListString__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_msg__msg__ListString__fini(&data[i - 1]);
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
custom_msg__msg__ListString__Sequence__fini(custom_msg__msg__ListString__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      custom_msg__msg__ListString__fini(&array->data[i]);
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

custom_msg__msg__ListString__Sequence *
custom_msg__msg__ListString__Sequence__create(size_t size)
{
  custom_msg__msg__ListString__Sequence * array = (custom_msg__msg__ListString__Sequence *)malloc(sizeof(custom_msg__msg__ListString__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = custom_msg__msg__ListString__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
custom_msg__msg__ListString__Sequence__destroy(custom_msg__msg__ListString__Sequence * array)
{
  if (array) {
    custom_msg__msg__ListString__Sequence__fini(array);
  }
  free(array);
}

bool
custom_msg__msg__ListString__Sequence__are_equal(const custom_msg__msg__ListString__Sequence * lhs, const custom_msg__msg__ListString__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_msg__msg__ListString__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_msg__msg__ListString__Sequence__copy(
  const custom_msg__msg__ListString__Sequence * input,
  custom_msg__msg__ListString__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_msg__msg__ListString);
    custom_msg__msg__ListString * data =
      (custom_msg__msg__ListString *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_msg__msg__ListString__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          custom_msg__msg__ListString__fini(&data[i]);
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
    if (!custom_msg__msg__ListString__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
