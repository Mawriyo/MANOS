// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from servo_control:srv/SetServo.idl
// generated code does not contain a copyright notice
#include "servo_control/srv/detail/set_servo__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool
servo_control__srv__SetServo_Request__init(servo_control__srv__SetServo_Request * msg)
{
  if (!msg) {
    return false;
  }
  // id
  // position
  return true;
}

void
servo_control__srv__SetServo_Request__fini(servo_control__srv__SetServo_Request * msg)
{
  if (!msg) {
    return;
  }
  // id
  // position
}

bool
servo_control__srv__SetServo_Request__are_equal(const servo_control__srv__SetServo_Request * lhs, const servo_control__srv__SetServo_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // id
  if (lhs->id != rhs->id) {
    return false;
  }
  // position
  if (lhs->position != rhs->position) {
    return false;
  }
  return true;
}

bool
servo_control__srv__SetServo_Request__copy(
  const servo_control__srv__SetServo_Request * input,
  servo_control__srv__SetServo_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // id
  output->id = input->id;
  // position
  output->position = input->position;
  return true;
}

servo_control__srv__SetServo_Request *
servo_control__srv__SetServo_Request__create()
{
  servo_control__srv__SetServo_Request * msg = (servo_control__srv__SetServo_Request *)malloc(sizeof(servo_control__srv__SetServo_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(servo_control__srv__SetServo_Request));
  bool success = servo_control__srv__SetServo_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
servo_control__srv__SetServo_Request__destroy(servo_control__srv__SetServo_Request * msg)
{
  if (msg) {
    servo_control__srv__SetServo_Request__fini(msg);
  }
  free(msg);
}


bool
servo_control__srv__SetServo_Request__Sequence__init(servo_control__srv__SetServo_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  servo_control__srv__SetServo_Request * data = NULL;
  if (size) {
    data = (servo_control__srv__SetServo_Request *)calloc(size, sizeof(servo_control__srv__SetServo_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = servo_control__srv__SetServo_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        servo_control__srv__SetServo_Request__fini(&data[i - 1]);
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
servo_control__srv__SetServo_Request__Sequence__fini(servo_control__srv__SetServo_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      servo_control__srv__SetServo_Request__fini(&array->data[i]);
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

servo_control__srv__SetServo_Request__Sequence *
servo_control__srv__SetServo_Request__Sequence__create(size_t size)
{
  servo_control__srv__SetServo_Request__Sequence * array = (servo_control__srv__SetServo_Request__Sequence *)malloc(sizeof(servo_control__srv__SetServo_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = servo_control__srv__SetServo_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
servo_control__srv__SetServo_Request__Sequence__destroy(servo_control__srv__SetServo_Request__Sequence * array)
{
  if (array) {
    servo_control__srv__SetServo_Request__Sequence__fini(array);
  }
  free(array);
}

bool
servo_control__srv__SetServo_Request__Sequence__are_equal(const servo_control__srv__SetServo_Request__Sequence * lhs, const servo_control__srv__SetServo_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!servo_control__srv__SetServo_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
servo_control__srv__SetServo_Request__Sequence__copy(
  const servo_control__srv__SetServo_Request__Sequence * input,
  servo_control__srv__SetServo_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(servo_control__srv__SetServo_Request);
    servo_control__srv__SetServo_Request * data =
      (servo_control__srv__SetServo_Request *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!servo_control__srv__SetServo_Request__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          servo_control__srv__SetServo_Request__fini(&data[i]);
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
    if (!servo_control__srv__SetServo_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
servo_control__srv__SetServo_Response__init(servo_control__srv__SetServo_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  return true;
}

void
servo_control__srv__SetServo_Response__fini(servo_control__srv__SetServo_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
}

bool
servo_control__srv__SetServo_Response__are_equal(const servo_control__srv__SetServo_Response * lhs, const servo_control__srv__SetServo_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
servo_control__srv__SetServo_Response__copy(
  const servo_control__srv__SetServo_Response * input,
  servo_control__srv__SetServo_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  return true;
}

servo_control__srv__SetServo_Response *
servo_control__srv__SetServo_Response__create()
{
  servo_control__srv__SetServo_Response * msg = (servo_control__srv__SetServo_Response *)malloc(sizeof(servo_control__srv__SetServo_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(servo_control__srv__SetServo_Response));
  bool success = servo_control__srv__SetServo_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
servo_control__srv__SetServo_Response__destroy(servo_control__srv__SetServo_Response * msg)
{
  if (msg) {
    servo_control__srv__SetServo_Response__fini(msg);
  }
  free(msg);
}


bool
servo_control__srv__SetServo_Response__Sequence__init(servo_control__srv__SetServo_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  servo_control__srv__SetServo_Response * data = NULL;
  if (size) {
    data = (servo_control__srv__SetServo_Response *)calloc(size, sizeof(servo_control__srv__SetServo_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = servo_control__srv__SetServo_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        servo_control__srv__SetServo_Response__fini(&data[i - 1]);
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
servo_control__srv__SetServo_Response__Sequence__fini(servo_control__srv__SetServo_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      servo_control__srv__SetServo_Response__fini(&array->data[i]);
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

servo_control__srv__SetServo_Response__Sequence *
servo_control__srv__SetServo_Response__Sequence__create(size_t size)
{
  servo_control__srv__SetServo_Response__Sequence * array = (servo_control__srv__SetServo_Response__Sequence *)malloc(sizeof(servo_control__srv__SetServo_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = servo_control__srv__SetServo_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
servo_control__srv__SetServo_Response__Sequence__destroy(servo_control__srv__SetServo_Response__Sequence * array)
{
  if (array) {
    servo_control__srv__SetServo_Response__Sequence__fini(array);
  }
  free(array);
}

bool
servo_control__srv__SetServo_Response__Sequence__are_equal(const servo_control__srv__SetServo_Response__Sequence * lhs, const servo_control__srv__SetServo_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!servo_control__srv__SetServo_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
servo_control__srv__SetServo_Response__Sequence__copy(
  const servo_control__srv__SetServo_Response__Sequence * input,
  servo_control__srv__SetServo_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(servo_control__srv__SetServo_Response);
    servo_control__srv__SetServo_Response * data =
      (servo_control__srv__SetServo_Response *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!servo_control__srv__SetServo_Response__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          servo_control__srv__SetServo_Response__fini(&data[i]);
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
    if (!servo_control__srv__SetServo_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
