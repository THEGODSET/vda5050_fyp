// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from vda5050_msgs:msg/InfoReference.idl
// generated code does not contain a copyright notice
#include "vda5050_msgs/msg/detail/info_reference__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `reference_key`
// Member `reference_value`
#include "rosidl_runtime_c/string_functions.h"

bool
vda5050_msgs__msg__InfoReference__init(vda5050_msgs__msg__InfoReference * msg)
{
  if (!msg) {
    return false;
  }
  // reference_key
  if (!rosidl_runtime_c__String__init(&msg->reference_key)) {
    vda5050_msgs__msg__InfoReference__fini(msg);
    return false;
  }
  // reference_value
  if (!rosidl_runtime_c__String__init(&msg->reference_value)) {
    vda5050_msgs__msg__InfoReference__fini(msg);
    return false;
  }
  return true;
}

void
vda5050_msgs__msg__InfoReference__fini(vda5050_msgs__msg__InfoReference * msg)
{
  if (!msg) {
    return;
  }
  // reference_key
  rosidl_runtime_c__String__fini(&msg->reference_key);
  // reference_value
  rosidl_runtime_c__String__fini(&msg->reference_value);
}

bool
vda5050_msgs__msg__InfoReference__are_equal(const vda5050_msgs__msg__InfoReference * lhs, const vda5050_msgs__msg__InfoReference * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // reference_key
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->reference_key), &(rhs->reference_key)))
  {
    return false;
  }
  // reference_value
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->reference_value), &(rhs->reference_value)))
  {
    return false;
  }
  return true;
}

bool
vda5050_msgs__msg__InfoReference__copy(
  const vda5050_msgs__msg__InfoReference * input,
  vda5050_msgs__msg__InfoReference * output)
{
  if (!input || !output) {
    return false;
  }
  // reference_key
  if (!rosidl_runtime_c__String__copy(
      &(input->reference_key), &(output->reference_key)))
  {
    return false;
  }
  // reference_value
  if (!rosidl_runtime_c__String__copy(
      &(input->reference_value), &(output->reference_value)))
  {
    return false;
  }
  return true;
}

vda5050_msgs__msg__InfoReference *
vda5050_msgs__msg__InfoReference__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  vda5050_msgs__msg__InfoReference * msg = (vda5050_msgs__msg__InfoReference *)allocator.allocate(sizeof(vda5050_msgs__msg__InfoReference), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(vda5050_msgs__msg__InfoReference));
  bool success = vda5050_msgs__msg__InfoReference__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
vda5050_msgs__msg__InfoReference__destroy(vda5050_msgs__msg__InfoReference * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    vda5050_msgs__msg__InfoReference__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
vda5050_msgs__msg__InfoReference__Sequence__init(vda5050_msgs__msg__InfoReference__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  vda5050_msgs__msg__InfoReference * data = NULL;

  if (size) {
    data = (vda5050_msgs__msg__InfoReference *)allocator.zero_allocate(size, sizeof(vda5050_msgs__msg__InfoReference), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = vda5050_msgs__msg__InfoReference__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        vda5050_msgs__msg__InfoReference__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
vda5050_msgs__msg__InfoReference__Sequence__fini(vda5050_msgs__msg__InfoReference__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      vda5050_msgs__msg__InfoReference__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

vda5050_msgs__msg__InfoReference__Sequence *
vda5050_msgs__msg__InfoReference__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  vda5050_msgs__msg__InfoReference__Sequence * array = (vda5050_msgs__msg__InfoReference__Sequence *)allocator.allocate(sizeof(vda5050_msgs__msg__InfoReference__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = vda5050_msgs__msg__InfoReference__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
vda5050_msgs__msg__InfoReference__Sequence__destroy(vda5050_msgs__msg__InfoReference__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    vda5050_msgs__msg__InfoReference__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
vda5050_msgs__msg__InfoReference__Sequence__are_equal(const vda5050_msgs__msg__InfoReference__Sequence * lhs, const vda5050_msgs__msg__InfoReference__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!vda5050_msgs__msg__InfoReference__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
vda5050_msgs__msg__InfoReference__Sequence__copy(
  const vda5050_msgs__msg__InfoReference__Sequence * input,
  vda5050_msgs__msg__InfoReference__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(vda5050_msgs__msg__InfoReference);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    vda5050_msgs__msg__InfoReference * data =
      (vda5050_msgs__msg__InfoReference *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!vda5050_msgs__msg__InfoReference__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          vda5050_msgs__msg__InfoReference__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!vda5050_msgs__msg__InfoReference__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
