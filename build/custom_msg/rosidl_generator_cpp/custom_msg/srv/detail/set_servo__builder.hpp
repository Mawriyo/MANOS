// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_msg:srv/SetServo.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSG__SRV__DETAIL__SET_SERVO__BUILDER_HPP_
#define CUSTOM_MSG__SRV__DETAIL__SET_SERVO__BUILDER_HPP_

#include "custom_msg/srv/detail/set_servo__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_msg
{

namespace srv
{

namespace builder
{

class Init_SetServo_Request_position
{
public:
  explicit Init_SetServo_Request_position(::custom_msg::srv::SetServo_Request & msg)
  : msg_(msg)
  {}
  ::custom_msg::srv::SetServo_Request position(::custom_msg::srv::SetServo_Request::_position_type arg)
  {
    msg_.position = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_msg::srv::SetServo_Request msg_;
};

class Init_SetServo_Request_id
{
public:
  Init_SetServo_Request_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetServo_Request_position id(::custom_msg::srv::SetServo_Request::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_SetServo_Request_position(msg_);
  }

private:
  ::custom_msg::srv::SetServo_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_msg::srv::SetServo_Request>()
{
  return custom_msg::srv::builder::Init_SetServo_Request_id();
}

}  // namespace custom_msg


namespace custom_msg
{

namespace srv
{

namespace builder
{

class Init_SetServo_Response_success
{
public:
  Init_SetServo_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_msg::srv::SetServo_Response success(::custom_msg::srv::SetServo_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_msg::srv::SetServo_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_msg::srv::SetServo_Response>()
{
  return custom_msg::srv::builder::Init_SetServo_Response_success();
}

}  // namespace custom_msg

#endif  // CUSTOM_MSG__SRV__DETAIL__SET_SERVO__BUILDER_HPP_
