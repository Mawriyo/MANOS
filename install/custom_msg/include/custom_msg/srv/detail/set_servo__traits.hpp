// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_msg:srv/SetServo.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSG__SRV__DETAIL__SET_SERVO__TRAITS_HPP_
#define CUSTOM_MSG__SRV__DETAIL__SET_SERVO__TRAITS_HPP_

#include "custom_msg/srv/detail/set_servo__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const custom_msg::srv::SetServo_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "id: ";
    value_to_yaml(msg.id, out);
    out << "\n";
  }

  // member: position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position: ";
    value_to_yaml(msg.position, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const custom_msg::srv::SetServo_Request & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<custom_msg::srv::SetServo_Request>()
{
  return "custom_msg::srv::SetServo_Request";
}

template<>
inline const char * name<custom_msg::srv::SetServo_Request>()
{
  return "custom_msg/srv/SetServo_Request";
}

template<>
struct has_fixed_size<custom_msg::srv::SetServo_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<custom_msg::srv::SetServo_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<custom_msg::srv::SetServo_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

inline void to_yaml(
  const custom_msg::srv::SetServo_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const custom_msg::srv::SetServo_Response & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<custom_msg::srv::SetServo_Response>()
{
  return "custom_msg::srv::SetServo_Response";
}

template<>
inline const char * name<custom_msg::srv::SetServo_Response>()
{
  return "custom_msg/srv/SetServo_Response";
}

template<>
struct has_fixed_size<custom_msg::srv::SetServo_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<custom_msg::srv::SetServo_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<custom_msg::srv::SetServo_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<custom_msg::srv::SetServo>()
{
  return "custom_msg::srv::SetServo";
}

template<>
inline const char * name<custom_msg::srv::SetServo>()
{
  return "custom_msg/srv/SetServo";
}

template<>
struct has_fixed_size<custom_msg::srv::SetServo>
  : std::integral_constant<
    bool,
    has_fixed_size<custom_msg::srv::SetServo_Request>::value &&
    has_fixed_size<custom_msg::srv::SetServo_Response>::value
  >
{
};

template<>
struct has_bounded_size<custom_msg::srv::SetServo>
  : std::integral_constant<
    bool,
    has_bounded_size<custom_msg::srv::SetServo_Request>::value &&
    has_bounded_size<custom_msg::srv::SetServo_Response>::value
  >
{
};

template<>
struct is_service<custom_msg::srv::SetServo>
  : std::true_type
{
};

template<>
struct is_service_request<custom_msg::srv::SetServo_Request>
  : std::true_type
{
};

template<>
struct is_service_response<custom_msg::srv::SetServo_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_MSG__SRV__DETAIL__SET_SERVO__TRAITS_HPP_
