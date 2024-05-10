// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from servo_control:srv/SetServo.idl
// generated code does not contain a copyright notice

#ifndef SERVO_CONTROL__SRV__DETAIL__SET_SERVO__BUILDER_HPP_
#define SERVO_CONTROL__SRV__DETAIL__SET_SERVO__BUILDER_HPP_

#include "servo_control/srv/detail/set_servo__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace servo_control
{

namespace srv
{

namespace builder
{

class Init_SetServo_Request_position
{
public:
  explicit Init_SetServo_Request_position(::servo_control::srv::SetServo_Request & msg)
  : msg_(msg)
  {}
  ::servo_control::srv::SetServo_Request position(::servo_control::srv::SetServo_Request::_position_type arg)
  {
    msg_.position = std::move(arg);
    return std::move(msg_);
  }

private:
  ::servo_control::srv::SetServo_Request msg_;
};

class Init_SetServo_Request_id
{
public:
  Init_SetServo_Request_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetServo_Request_position id(::servo_control::srv::SetServo_Request::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_SetServo_Request_position(msg_);
  }

private:
  ::servo_control::srv::SetServo_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::servo_control::srv::SetServo_Request>()
{
  return servo_control::srv::builder::Init_SetServo_Request_id();
}

}  // namespace servo_control


namespace servo_control
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
  ::servo_control::srv::SetServo_Response success(::servo_control::srv::SetServo_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::servo_control::srv::SetServo_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::servo_control::srv::SetServo_Response>()
{
  return servo_control::srv::builder::Init_SetServo_Response_success();
}

}  // namespace servo_control

#endif  // SERVO_CONTROL__SRV__DETAIL__SET_SERVO__BUILDER_HPP_
