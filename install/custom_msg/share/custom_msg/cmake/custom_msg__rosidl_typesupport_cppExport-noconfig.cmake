#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "custom_msg::custom_msg__rosidl_typesupport_cpp" for configuration ""
set_property(TARGET custom_msg::custom_msg__rosidl_typesupport_cpp APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(custom_msg::custom_msg__rosidl_typesupport_cpp PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libcustom_msg__rosidl_typesupport_cpp.so"
  IMPORTED_SONAME_NOCONFIG "libcustom_msg__rosidl_typesupport_cpp.so"
  )

list(APPEND _cmake_import_check_targets custom_msg::custom_msg__rosidl_typesupport_cpp )
list(APPEND _cmake_import_check_files_for_custom_msg::custom_msg__rosidl_typesupport_cpp "${_IMPORT_PREFIX}/lib/libcustom_msg__rosidl_typesupport_cpp.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
