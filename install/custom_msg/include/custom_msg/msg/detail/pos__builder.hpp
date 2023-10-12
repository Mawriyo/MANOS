// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_msg:msg/Pos.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSG__MSG__DETAIL__POS__BUILDER_HPP_
#define CUSTOM_MSG__MSG__DETAIL__POS__BUILDER_HPP_

#include "custom_msg/msg/detail/pos__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_msg
{

namespace msg
{

namespace builder
{

class Init_Pos_y
{
public:
  explicit Init_Pos_y(::custom_msg::msg::Pos & msg)
  : msg_(msg)
  {}
  ::custom_msg::msg::Pos y(::custom_msg::msg::Pos::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_msg::msg::Pos msg_;
};

class Init_Pos_x
{
public:
  Init_Pos_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Pos_y x(::custom_msg::msg::Pos::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Pos_y(msg_);
  }

private:
  ::custom_msg::msg::Pos msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_msg::msg::Pos>()
{
  return custom_msg::msg::builder::Init_Pos_x();
}

}  // namespace custom_msg

#endif  // CUSTOM_MSG__MSG__DETAIL__POS__BUILDER_HPP_
