// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_msg:msg/ListString.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSG__MSG__DETAIL__LIST_STRING__BUILDER_HPP_
#define CUSTOM_MSG__MSG__DETAIL__LIST_STRING__BUILDER_HPP_

#include "custom_msg/msg/detail/list_string__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_msg
{

namespace msg
{

namespace builder
{

class Init_ListString_data
{
public:
  Init_ListString_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_msg::msg::ListString data(::custom_msg::msg::ListString::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_msg::msg::ListString msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_msg::msg::ListString>()
{
  return custom_msg::msg::builder::Init_ListString_data();
}

}  // namespace custom_msg

#endif  // CUSTOM_MSG__MSG__DETAIL__LIST_STRING__BUILDER_HPP_
