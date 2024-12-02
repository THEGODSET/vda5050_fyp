// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from vda5050_msgs:msg/Envelope3D.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "vda5050_msgs/msg/detail/envelope3_d__rosidl_typesupport_introspection_c.h"
#include "vda5050_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "vda5050_msgs/msg/detail/envelope3_d__functions.h"
#include "vda5050_msgs/msg/detail/envelope3_d__struct.h"


// Include directives for member types
// Member `set`
// Member `format`
// Member `data`
// Member `url`
// Member `description`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void vda5050_msgs__msg__Envelope3D__rosidl_typesupport_introspection_c__Envelope3D_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  vda5050_msgs__msg__Envelope3D__init(message_memory);
}

void vda5050_msgs__msg__Envelope3D__rosidl_typesupport_introspection_c__Envelope3D_fini_function(void * message_memory)
{
  vda5050_msgs__msg__Envelope3D__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember vda5050_msgs__msg__Envelope3D__rosidl_typesupport_introspection_c__Envelope3D_message_member_array[5] = {
  {
    "set",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(vda5050_msgs__msg__Envelope3D, set),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "format",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(vda5050_msgs__msg__Envelope3D, format),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "data",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(vda5050_msgs__msg__Envelope3D, data),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "url",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(vda5050_msgs__msg__Envelope3D, url),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "description",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(vda5050_msgs__msg__Envelope3D, description),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers vda5050_msgs__msg__Envelope3D__rosidl_typesupport_introspection_c__Envelope3D_message_members = {
  "vda5050_msgs__msg",  // message namespace
  "Envelope3D",  // message name
  5,  // number of fields
  sizeof(vda5050_msgs__msg__Envelope3D),
  vda5050_msgs__msg__Envelope3D__rosidl_typesupport_introspection_c__Envelope3D_message_member_array,  // message members
  vda5050_msgs__msg__Envelope3D__rosidl_typesupport_introspection_c__Envelope3D_init_function,  // function to initialize message memory (memory has to be allocated)
  vda5050_msgs__msg__Envelope3D__rosidl_typesupport_introspection_c__Envelope3D_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t vda5050_msgs__msg__Envelope3D__rosidl_typesupport_introspection_c__Envelope3D_message_type_support_handle = {
  0,
  &vda5050_msgs__msg__Envelope3D__rosidl_typesupport_introspection_c__Envelope3D_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_vda5050_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, vda5050_msgs, msg, Envelope3D)() {
  if (!vda5050_msgs__msg__Envelope3D__rosidl_typesupport_introspection_c__Envelope3D_message_type_support_handle.typesupport_identifier) {
    vda5050_msgs__msg__Envelope3D__rosidl_typesupport_introspection_c__Envelope3D_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &vda5050_msgs__msg__Envelope3D__rosidl_typesupport_introspection_c__Envelope3D_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
