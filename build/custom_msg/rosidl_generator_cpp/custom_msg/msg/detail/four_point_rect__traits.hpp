// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_msg:msg/FourPointRect.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSG__MSG__DETAIL__FOUR_POINT_RECT__TRAITS_HPP_
#define CUSTOM_MSG__MSG__DETAIL__FOUR_POINT_RECT__TRAITS_HPP_

#include "custom_msg/msg/detail/four_point_rect__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const custom_msg::msg::FourPointRect & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: xmin
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "xmin: ";
    value_to_yaml(msg.xmin, out);
    out << "\n";
  }

  // member: xmax
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "xmax: ";
    value_to_yaml(msg.xmax, out);
    out << "\n";
  }

  // member: ymin
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ymin: ";
    value_to_yaml(msg.ymin, out);
    out << "\n";
  }

  // member: ymax
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ymax: ";
    value_to_yaml(msg.ymax, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const custom_msg::msg::FourPointRect & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<custom_msg::msg::FourPointRect>()
{
  return "custom_msg::msg::FourPointRect";
}

template<>
inline const char * name<custom_msg::msg::FourPointRect>()
{
  return "custom_msg/msg/FourPointRect";
}

template<>
struct has_fixed_size<custom_msg::msg::FourPointRect>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<custom_msg::msg::FourPointRect>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<custom_msg::msg::FourPointRect>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_MSG__MSG__DETAIL__FOUR_POINT_RECT__TRAITS_HPP_
