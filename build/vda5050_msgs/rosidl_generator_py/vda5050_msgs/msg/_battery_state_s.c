// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from vda5050_msgs:msg/BatteryState.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "vda5050_msgs/msg/detail/battery_state__struct.h"
#include "vda5050_msgs/msg/detail/battery_state__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool vda5050_msgs__msg__battery_state__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[45];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("vda5050_msgs.msg._battery_state.BatteryState", full_classname_dest, 44) == 0);
  }
  vda5050_msgs__msg__BatteryState * ros_message = _ros_message;
  {  // battery_charge
    PyObject * field = PyObject_GetAttrString(_pymsg, "battery_charge");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->battery_charge = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // battery_voltage
    PyObject * field = PyObject_GetAttrString(_pymsg, "battery_voltage");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->battery_voltage = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // battery_health
    PyObject * field = PyObject_GetAttrString(_pymsg, "battery_health");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->battery_health = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // charging
    PyObject * field = PyObject_GetAttrString(_pymsg, "charging");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->charging = (Py_True == field);
    Py_DECREF(field);
  }
  {  // reach
    PyObject * field = PyObject_GetAttrString(_pymsg, "reach");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->reach = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * vda5050_msgs__msg__battery_state__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of BatteryState */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("vda5050_msgs.msg._battery_state");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "BatteryState");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  vda5050_msgs__msg__BatteryState * ros_message = (vda5050_msgs__msg__BatteryState *)raw_ros_message;
  {  // battery_charge
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->battery_charge);
    {
      int rc = PyObject_SetAttrString(_pymessage, "battery_charge", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // battery_voltage
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->battery_voltage);
    {
      int rc = PyObject_SetAttrString(_pymessage, "battery_voltage", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // battery_health
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->battery_health);
    {
      int rc = PyObject_SetAttrString(_pymessage, "battery_health", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // charging
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->charging ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "charging", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // reach
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->reach);
    {
      int rc = PyObject_SetAttrString(_pymessage, "reach", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
