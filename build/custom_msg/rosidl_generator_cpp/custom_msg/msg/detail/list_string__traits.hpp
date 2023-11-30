// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from custom_msg:msg/ListString.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_MSG__MSG__DETAIL__LIST_STRING__TRAITS_HPP_
#define CUSTOM_MSG__MSG__DETAIL__LIST_STRING__TRAITS_HPP_

#include "custom_msg/msg/detail/list_string__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const custom_msg::msg::ListString & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.data.size() == 0) {
      out << "data: []\n";
    } else {
      out << "data:\n";
      for (auto item : msg.data) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const custom_msg::msg::ListString & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<custom_msg::msg::ListString>()
{
  return "custom_msg::msg::ListString";
}

template<>
inline const char * name<custom_msg::msg::ListString>()
{
  return "custom_msg/msg/ListString";
}

template<>
struct has_fixed_size<custom_msg::msg::ListString>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<custom_msg::msg::ListString>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<custom_msg::msg::ListString>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CUSTOM_MSG__MSG__DETAIL__LIST_STRING__TRAITS_HPP_
