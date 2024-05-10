// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_msg:msg/MANOSBundle.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSG__MSG__DETAIL__MANOS_BUNDLE__BUILDER_HPP_
#define CUSTOM_MSG__MSG__DETAIL__MANOS_BUNDLE__BUILDER_HPP_

#include "custom_msg/msg/detail/manos_bundle__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_msg
{

namespace msg
{

namespace builder
{

class Init_MANOSBundle_topic
{
public:
  explicit Init_MANOSBundle_topic(::custom_msg::msg::MANOSBundle & msg)
  : msg_(msg)
  {}
  ::custom_msg::msg::MANOSBundle topic(::custom_msg::msg::MANOSBundle::_topic_type arg)
  {
    msg_.topic = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_msg::msg::MANOSBundle msg_;
};

class Init_MANOSBundle_type
{
public:
  explicit Init_MANOSBundle_type(::custom_msg::msg::MANOSBundle & msg)
  : msg_(msg)
  {}
  Init_MANOSBundle_topic type(::custom_msg::msg::MANOSBundle::_type_type arg)
  {
    msg_.type = std::move(arg);
    return Init_MANOSBundle_topic(msg_);
  }

private:
  ::custom_msg::msg::MANOSBundle msg_;
};

class Init_MANOSBundle_data
{
public:
  Init_MANOSBundle_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MANOSBundle_type data(::custom_msg::msg::MANOSBundle::_data_type arg)
  {
    msg_.data = std::move(arg);
    return Init_MANOSBundle_type(msg_);
  }

private:
  ::custom_msg::msg::MANOSBundle msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_msg::msg::MANOSBundle>()
{
  return custom_msg::msg::builder::Init_MANOSBundle_data();
}

}  // namespace custom_msg

#endif  // CUSTOM_MSG__MSG__DETAIL__MANOS_BUNDLE__BUILDER_HPP_
