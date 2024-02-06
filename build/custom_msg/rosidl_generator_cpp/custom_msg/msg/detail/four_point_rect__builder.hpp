// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_msg:msg/FourPointRect.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSG__MSG__DETAIL__FOUR_POINT_RECT__BUILDER_HPP_
#define CUSTOM_MSG__MSG__DETAIL__FOUR_POINT_RECT__BUILDER_HPP_

#include "custom_msg/msg/detail/four_point_rect__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_msg
{

namespace msg
{

namespace builder
{

class Init_FourPointRect_ymax
{
public:
  explicit Init_FourPointRect_ymax(::custom_msg::msg::FourPointRect & msg)
  : msg_(msg)
  {}
  ::custom_msg::msg::FourPointRect ymax(::custom_msg::msg::FourPointRect::_ymax_type arg)
  {
    msg_.ymax = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_msg::msg::FourPointRect msg_;
};

class Init_FourPointRect_ymin
{
public:
  explicit Init_FourPointRect_ymin(::custom_msg::msg::FourPointRect & msg)
  : msg_(msg)
  {}
  Init_FourPointRect_ymax ymin(::custom_msg::msg::FourPointRect::_ymin_type arg)
  {
    msg_.ymin = std::move(arg);
    return Init_FourPointRect_ymax(msg_);
  }

private:
  ::custom_msg::msg::FourPointRect msg_;
};

class Init_FourPointRect_xmax
{
public:
  explicit Init_FourPointRect_xmax(::custom_msg::msg::FourPointRect & msg)
  : msg_(msg)
  {}
  Init_FourPointRect_ymin xmax(::custom_msg::msg::FourPointRect::_xmax_type arg)
  {
    msg_.xmax = std::move(arg);
    return Init_FourPointRect_ymin(msg_);
  }

private:
  ::custom_msg::msg::FourPointRect msg_;
};

class Init_FourPointRect_xmin
{
public:
  Init_FourPointRect_xmin()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FourPointRect_xmax xmin(::custom_msg::msg::FourPointRect::_xmin_type arg)
  {
    msg_.xmin = std::move(arg);
    return Init_FourPointRect_xmax(msg_);
  }

private:
  ::custom_msg::msg::FourPointRect msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_msg::msg::FourPointRect>()
{
  return custom_msg::msg::builder::Init_FourPointRect_xmin();
}

}  // namespace custom_msg

#endif  // CUSTOM_MSG__MSG__DETAIL__FOUR_POINT_RECT__BUILDER_HPP_
