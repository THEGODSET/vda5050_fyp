// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from vda5050_msgs:msg/NodeState.idl
// generated code does not contain a copyright notice
#include "vda5050_msgs/msg/detail/node_state__rosidl_typesupport_fastrtps_cpp.hpp"
#include "vda5050_msgs/msg/detail/node_state__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions
namespace vda5050_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const vda5050_msgs::msg::NodePosition &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  vda5050_msgs::msg::NodePosition &);
size_t get_serialized_size(
  const vda5050_msgs::msg::NodePosition &,
  size_t current_alignment);
size_t
max_serialized_size_NodePosition(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace vda5050_msgs


namespace vda5050_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_vda5050_msgs
cdr_serialize(
  const vda5050_msgs::msg::NodeState & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: node_id
  cdr << ros_message.node_id;
  // Member: sequence_id
  cdr << ros_message.sequence_id;
  // Member: node_description
  cdr << ros_message.node_description;
  // Member: position
  vda5050_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.position,
    cdr);
  // Member: released
  cdr << (ros_message.released ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_vda5050_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  vda5050_msgs::msg::NodeState & ros_message)
{
  // Member: node_id
  cdr >> ros_message.node_id;

  // Member: sequence_id
  cdr >> ros_message.sequence_id;

  // Member: node_description
  cdr >> ros_message.node_description;

  // Member: position
  vda5050_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.position);

  // Member: released
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.released = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_vda5050_msgs
get_serialized_size(
  const vda5050_msgs::msg::NodeState & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: node_id
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.node_id.size() + 1);
  // Member: sequence_id
  {
    size_t item_size = sizeof(ros_message.sequence_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: node_description
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.node_description.size() + 1);
  // Member: position

  current_alignment +=
    vda5050_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.position, current_alignment);
  // Member: released
  {
    size_t item_size = sizeof(ros_message.released);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_vda5050_msgs
max_serialized_size_NodeState(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: node_id
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: sequence_id
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: node_description
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: position
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size =
        vda5050_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_NodePosition(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  // Member: released
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = vda5050_msgs::msg::NodeState;
    is_plain =
      (
      offsetof(DataType, released) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _NodeState__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const vda5050_msgs::msg::NodeState *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _NodeState__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<vda5050_msgs::msg::NodeState *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _NodeState__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const vda5050_msgs::msg::NodeState *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _NodeState__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_NodeState(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _NodeState__callbacks = {
  "vda5050_msgs::msg",
  "NodeState",
  _NodeState__cdr_serialize,
  _NodeState__cdr_deserialize,
  _NodeState__get_serialized_size,
  _NodeState__max_serialized_size
};

static rosidl_message_type_support_t _NodeState__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_NodeState__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace vda5050_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_vda5050_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<vda5050_msgs::msg::NodeState>()
{
  return &vda5050_msgs::msg::typesupport_fastrtps_cpp::_NodeState__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, vda5050_msgs, msg, NodeState)() {
  return &vda5050_msgs::msg::typesupport_fastrtps_cpp::_NodeState__handle;
}

#ifdef __cplusplus
}
#endif
