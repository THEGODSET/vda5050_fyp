// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from vda5050_msgs:msg/NodeState.idl
// generated code does not contain a copyright notice

#ifndef VDA5050_MSGS__MSG__DETAIL__NODE_STATE__STRUCT_HPP_
#define VDA5050_MSGS__MSG__DETAIL__NODE_STATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'position'
#include "vda5050_msgs/msg/detail/node_position__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__vda5050_msgs__msg__NodeState __attribute__((deprecated))
#else
# define DEPRECATED__vda5050_msgs__msg__NodeState __declspec(deprecated)
#endif

namespace vda5050_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct NodeState_
{
  using Type = NodeState_<ContainerAllocator>;

  explicit NodeState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : position(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->node_id = "";
      this->sequence_id = 0ul;
      this->node_description = "";
      this->released = false;
    }
  }

  explicit NodeState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : node_id(_alloc),
    node_description(_alloc),
    position(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->node_id = "";
      this->sequence_id = 0ul;
      this->node_description = "";
      this->released = false;
    }
  }

  // field types and members
  using _node_id_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _node_id_type node_id;
  using _sequence_id_type =
    uint32_t;
  _sequence_id_type sequence_id;
  using _node_description_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _node_description_type node_description;
  using _position_type =
    vda5050_msgs::msg::NodePosition_<ContainerAllocator>;
  _position_type position;
  using _released_type =
    bool;
  _released_type released;

  // setters for named parameter idiom
  Type & set__node_id(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->node_id = _arg;
    return *this;
  }
  Type & set__sequence_id(
    const uint32_t & _arg)
  {
    this->sequence_id = _arg;
    return *this;
  }
  Type & set__node_description(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->node_description = _arg;
    return *this;
  }
  Type & set__position(
    const vda5050_msgs::msg::NodePosition_<ContainerAllocator> & _arg)
  {
    this->position = _arg;
    return *this;
  }
  Type & set__released(
    const bool & _arg)
  {
    this->released = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    vda5050_msgs::msg::NodeState_<ContainerAllocator> *;
  using ConstRawPtr =
    const vda5050_msgs::msg::NodeState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<vda5050_msgs::msg::NodeState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<vda5050_msgs::msg::NodeState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      vda5050_msgs::msg::NodeState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<vda5050_msgs::msg::NodeState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      vda5050_msgs::msg::NodeState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<vda5050_msgs::msg::NodeState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<vda5050_msgs::msg::NodeState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<vda5050_msgs::msg::NodeState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__vda5050_msgs__msg__NodeState
    std::shared_ptr<vda5050_msgs::msg::NodeState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__vda5050_msgs__msg__NodeState
    std::shared_ptr<vda5050_msgs::msg::NodeState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const NodeState_ & other) const
  {
    if (this->node_id != other.node_id) {
      return false;
    }
    if (this->sequence_id != other.sequence_id) {
      return false;
    }
    if (this->node_description != other.node_description) {
      return false;
    }
    if (this->position != other.position) {
      return false;
    }
    if (this->released != other.released) {
      return false;
    }
    return true;
  }
  bool operator!=(const NodeState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct NodeState_

// alias to use template instance with default allocator
using NodeState =
  vda5050_msgs::msg::NodeState_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace vda5050_msgs

#endif  // VDA5050_MSGS__MSG__DETAIL__NODE_STATE__STRUCT_HPP_
