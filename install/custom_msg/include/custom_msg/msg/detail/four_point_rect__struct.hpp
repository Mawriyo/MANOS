// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from custom_msg:msg/FourPointRect.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSG__MSG__DETAIL__FOUR_POINT_RECT__STRUCT_HPP_
#define CUSTOM_MSG__MSG__DETAIL__FOUR_POINT_RECT__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__custom_msg__msg__FourPointRect __attribute__((deprecated))
#else
# define DEPRECATED__custom_msg__msg__FourPointRect __declspec(deprecated)
#endif

namespace custom_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct FourPointRect_
{
  using Type = FourPointRect_<ContainerAllocator>;

  explicit FourPointRect_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->xmin = 0.0f;
      this->xmax = 0.0f;
      this->ymin = 0.0f;
      this->ymax = 0.0f;
    }
  }

  explicit FourPointRect_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->xmin = 0.0f;
      this->xmax = 0.0f;
      this->ymin = 0.0f;
      this->ymax = 0.0f;
    }
  }

  // field types and members
  using _xmin_type =
    float;
  _xmin_type xmin;
  using _xmax_type =
    float;
  _xmax_type xmax;
  using _ymin_type =
    float;
  _ymin_type ymin;
  using _ymax_type =
    float;
  _ymax_type ymax;

  // setters for named parameter idiom
  Type & set__xmin(
    const float & _arg)
  {
    this->xmin = _arg;
    return *this;
  }
  Type & set__xmax(
    const float & _arg)
  {
    this->xmax = _arg;
    return *this;
  }
  Type & set__ymin(
    const float & _arg)
  {
    this->ymin = _arg;
    return *this;
  }
  Type & set__ymax(
    const float & _arg)
  {
    this->ymax = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    custom_msg::msg::FourPointRect_<ContainerAllocator> *;
  using ConstRawPtr =
    const custom_msg::msg::FourPointRect_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<custom_msg::msg::FourPointRect_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<custom_msg::msg::FourPointRect_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      custom_msg::msg::FourPointRect_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<custom_msg::msg::FourPointRect_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      custom_msg::msg::FourPointRect_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<custom_msg::msg::FourPointRect_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<custom_msg::msg::FourPointRect_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<custom_msg::msg::FourPointRect_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__custom_msg__msg__FourPointRect
    std::shared_ptr<custom_msg::msg::FourPointRect_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__custom_msg__msg__FourPointRect
    std::shared_ptr<custom_msg::msg::FourPointRect_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FourPointRect_ & other) const
  {
    if (this->xmin != other.xmin) {
      return false;
    }
    if (this->xmax != other.xmax) {
      return false;
    }
    if (this->ymin != other.ymin) {
      return false;
    }
    if (this->ymax != other.ymax) {
      return false;
    }
    return true;
  }
  bool operator!=(const FourPointRect_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FourPointRect_

// alias to use template instance with default allocator
using FourPointRect =
  custom_msg::msg::FourPointRect_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace custom_msg

#endif  // CUSTOM_MSG__MSG__DETAIL__FOUR_POINT_RECT__STRUCT_HPP_
