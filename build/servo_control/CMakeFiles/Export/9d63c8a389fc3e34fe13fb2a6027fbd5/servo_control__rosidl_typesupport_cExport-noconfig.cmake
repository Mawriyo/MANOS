#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "servo_control::servo_control__rosidl_typesupport_c" for configuration ""
set_property(TARGET servo_control::servo_control__rosidl_typesupport_c APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(servo_control::servo_control__rosidl_typesupport_c PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libservo_control__rosidl_typesupport_c.so"
  IMPORTED_SONAME_NOCONFIG "libservo_control__rosidl_typesupport_c.so"
  )

list(APPEND _cmake_import_check_targets servo_control::servo_control__rosidl_typesupport_c )
list(APPEND _cmake_import_check_files_for_servo_control::servo_control__rosidl_typesupport_c "${_IMPORT_PREFIX}/lib/libservo_control__rosidl_typesupport_c.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
