// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_msg:msg/Pos.idl
// generated code does not contain a copyright notice
#include "custom_msg/msg/detail/pos__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
custom_msg__msg__Pos__init(custom_msg__msg__Pos * msg)
{
  if (!msg) {
    return false;
  }
  // x
  // y
  return true;
}

void
custom_msg__msg__Pos__fini(custom_msg__msg__Pos * msg)
{
  if (!msg) {
    return;
  }
  // x
  // y
}

bool
custom_msg__msg__Pos__are_equal(const custom_msg__msg__Pos * lhs, const custom_msg__msg__Pos * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // x
  if (lhs->x != rhs->x) {
    return false;
  }
  // y
  if (lhs->y != rhs->y) {
    return false;
  }
  return true;
}

bool
custom_msg__msg__Pos__copy(
  const custom_msg__msg__Pos * input,
  custom_msg__msg__Pos * output)
{
  if (!input || !output) {
    return false;
  }
  // x
  output->x = input->x;
  // y
  output->y = input->y;
  return true;
}

custom_msg__msg__Pos *
custom_msg__msg__Pos__create()
{
  custom_msg__msg__Pos * msg = (custom_msg__msg__Pos *)malloc(sizeof(custom_msg__msg__Pos));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_msg__msg__Pos));
  bool success = custom_msg__msg__Pos__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
custom_msg__msg__Pos__destroy(custom_msg__msg__Pos * msg)
{
  if (msg) {
    custom_msg__msg__Pos__fini(msg);
  }
  free(msg);
}


bool
custom_msg__msg__Pos__Sequence__init(custom_msg__msg__Pos__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  custom_msg__msg__Pos * data = NULL;
  if (size) {
    data = (custom_msg__msg__Pos *)calloc(size, sizeof(custom_msg__msg__Pos));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_msg__msg__Pos__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_msg__msg__Pos__fini(&data[i - 1]);
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
custom_msg__msg__Pos__Sequence__fini(custom_msg__msg__Pos__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      custom_msg__msg__Pos__fini(&array->data[i]);
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

custom_msg__msg__Pos__Sequence *
custom_msg__msg__Pos__Sequence__create(size_t size)
{
  custom_msg__msg__Pos__Sequence * array = (custom_msg__msg__Pos__Sequence *)malloc(sizeof(custom_msg__msg__Pos__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = custom_msg__msg__Pos__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
custom_msg__msg__Pos__Sequence__destroy(custom_msg__msg__Pos__Sequence * array)
{
  if (array) {
    custom_msg__msg__Pos__Sequence__fini(array);
  }
  free(array);
}

bool
custom_msg__msg__Pos__Sequence__are_equal(const custom_msg__msg__Pos__Sequence * lhs, const custom_msg__msg__Pos__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_msg__msg__Pos__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_msg__msg__Pos__Sequence__copy(
  const custom_msg__msg__Pos__Sequence * input,
  custom_msg__msg__Pos__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_msg__msg__Pos);
    custom_msg__msg__Pos * data =
      (custom_msg__msg__Pos *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_msg__msg__Pos__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          custom_msg__msg__Pos__fini(&data[i]);
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
    if (!custom_msg__msg__Pos__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
