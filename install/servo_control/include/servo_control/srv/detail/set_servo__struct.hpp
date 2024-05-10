// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from servo_control:srv/SetServo.idl
// generated code does not contain a copyright notice

#ifndef SERVO_CONTROL__SRV__DETAIL__SET_SERVO__STRUCT_HPP_
#define SERVO_CONTROL__SRV__DETAIL__SET_SERVO__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__servo_control__srv__SetServo_Request __attribute__((deprecated))
#else
# define DEPRECATED__servo_control__srv__SetServo_Request __declspec(deprecated)
#endif

namespace servo_control
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetServo_Request_
{
  using Type = SetServo_Request_<ContainerAllocator>;

  explicit SetServo_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0l;
      this->position = 0l;
    }
  }

  explicit SetServo_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0l;
      this->position = 0l;
    }
  }

  // field types and members
  using _id_type =
    int32_t;
  _id_type id;
  using _position_type =
    int32_t;
  _position_type position;

  // setters for named parameter idiom
  Type & set__id(
    const int32_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__position(
    const int32_t & _arg)
  {
    this->position = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    servo_control::srv::SetServo_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const servo_control::srv::SetServo_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<servo_control::srv::SetServo_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<servo_control::srv::SetServo_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      servo_control::srv::SetServo_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<servo_control::srv::SetServo_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      servo_control::srv::SetServo_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<servo_control::srv::SetServo_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<servo_control::srv::SetServo_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<servo_control::srv::SetServo_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__servo_control__srv__SetServo_Request
    std::shared_ptr<servo_control::srv::SetServo_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__servo_control__srv__SetServo_Request
    std::shared_ptr<servo_control::srv::SetServo_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetServo_Request_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->position != other.position) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetServo_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetServo_Request_

// alias to use template instance with default allocator
using SetServo_Request =
  servo_control::srv::SetServo_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace servo_control


#ifndef _WIN32
# define DEPRECATED__servo_control__srv__SetServo_Response __attribute__((deprecated))
#else
# define DEPRECATED__servo_control__srv__SetServo_Response __declspec(deprecated)
#endif

namespace servo_control
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetServo_Response_
{
  using Type = SetServo_Response_<ContainerAllocator>;

  explicit SetServo_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit SetServo_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    servo_control::srv::SetServo_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const servo_control::srv::SetServo_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<servo_control::srv::SetServo_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<servo_control::srv::SetServo_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      servo_control::srv::SetServo_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<servo_control::srv::SetServo_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      servo_control::srv::SetServo_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<servo_control::srv::SetServo_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<servo_control::srv::SetServo_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<servo_control::srv::SetServo_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__servo_control__srv__SetServo_Response
    std::shared_ptr<servo_control::srv::SetServo_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__servo_control__srv__SetServo_Response
    std::shared_ptr<servo_control::srv::SetServo_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetServo_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetServo_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetServo_Response_

// alias to use template instance with default allocator
using SetServo_Response =
  servo_control::srv::SetServo_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace servo_control

namespace servo_control
{

namespace srv
{

struct SetServo
{
  using Request = servo_control::srv::SetServo_Request;
  using Response = servo_control::srv::SetServo_Response;
};

}  // namespace srv

}  // namespace servo_control

#endif  // SERVO_CONTROL__SRV__DETAIL__SET_SERVO__STRUCT_HPP_
