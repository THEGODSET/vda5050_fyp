// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from vda5050_msgs:msg/Trajectory.idl
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
#include "vda5050_msgs/msg/detail/trajectory__struct.h"
#include "vda5050_msgs/msg/detail/trajectory__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

// Nested array functions includes
#include "vda5050_msgs/msg/detail/control_point__functions.h"
// end nested array functions include
bool vda5050_msgs__msg__control_point__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * vda5050_msgs__msg__control_point__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool vda5050_msgs__msg__trajectory__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[40];
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
    assert(strncmp("vda5050_msgs.msg._trajectory.Trajectory", full_classname_dest, 39) == 0);
  }
  vda5050_msgs__msg__Trajectory * ros_message = _ros_message;
  {  // degree
    PyObject * field = PyObject_GetAttrString(_pymsg, "degree");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->degree = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // knot_vector
    PyObject * field = PyObject_GetAttrString(_pymsg, "knot_vector");
    if (!field) {
      return false;
    }
    if (PyObject_CheckBuffer(field)) {
      // Optimization for converting arrays of primitives
      Py_buffer view;
      int rc = PyObject_GetBuffer(field, &view, PyBUF_SIMPLE);
      if (rc < 0) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = view.len / sizeof(double);
      if (!rosidl_runtime_c__double__Sequence__init(&(ros_message->knot_vector), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create double__Sequence ros_message");
        PyBuffer_Release(&view);
        Py_DECREF(field);
        return false;
      }
      double * dest = ros_message->knot_vector.data;
      rc = PyBuffer_ToContiguous(dest, &view, view.len, 'C');
      if (rc < 0) {
        PyBuffer_Release(&view);
        Py_DECREF(field);
        return false;
      }
      PyBuffer_Release(&view);
    } else {
      PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'knot_vector'");
      if (!seq_field) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = PySequence_Size(field);
      if (-1 == size) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      if (!rosidl_runtime_c__double__Sequence__init(&(ros_message->knot_vector), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create double__Sequence ros_message");
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      double * dest = ros_message->knot_vector.data;
      for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject * item = PySequence_Fast_GET_ITEM(seq_field, i);
        if (!item) {
          Py_DECREF(seq_field);
          Py_DECREF(field);
          return false;
        }
        assert(PyFloat_Check(item));
        double tmp = PyFloat_AS_DOUBLE(item);
        memcpy(&dest[i], &tmp, sizeof(double));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // control_points
    PyObject * field = PyObject_GetAttrString(_pymsg, "control_points");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'control_points'");
    if (!seq_field) {
      Py_DECREF(field);
      return false;
    }
    Py_ssize_t size = PySequence_Size(field);
    if (-1 == size) {
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    if (!vda5050_msgs__msg__ControlPoint__Sequence__init(&(ros_message->control_points), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create vda5050_msgs__msg__ControlPoint__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    vda5050_msgs__msg__ControlPoint * dest = ros_message->control_points.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!vda5050_msgs__msg__control_point__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * vda5050_msgs__msg__trajectory__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Trajectory */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("vda5050_msgs.msg._trajectory");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Trajectory");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  vda5050_msgs__msg__Trajectory * ros_message = (vda5050_msgs__msg__Trajectory *)raw_ros_message;
  {  // degree
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->degree);
    {
      int rc = PyObject_SetAttrString(_pymessage, "degree", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // knot_vector
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "knot_vector");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "array.array") == 0);
    // ensure that itemsize matches the sizeof of the ROS message field
    PyObject * itemsize_attr = PyObject_GetAttrString(field, "itemsize");
    assert(itemsize_attr != NULL);
    size_t itemsize = PyLong_AsSize_t(itemsize_attr);
    Py_DECREF(itemsize_attr);
    if (itemsize != sizeof(double)) {
      PyErr_SetString(PyExc_RuntimeError, "itemsize doesn't match expectation");
      Py_DECREF(field);
      return NULL;
    }
    // clear the array, poor approach to remove potential default values
    Py_ssize_t length = PyObject_Length(field);
    if (-1 == length) {
      Py_DECREF(field);
      return NULL;
    }
    if (length > 0) {
      PyObject * pop = PyObject_GetAttrString(field, "pop");
      assert(pop != NULL);
      for (Py_ssize_t i = 0; i < length; ++i) {
        PyObject * ret = PyObject_CallFunctionObjArgs(pop, NULL);
        if (!ret) {
          Py_DECREF(pop);
          Py_DECREF(field);
          return NULL;
        }
        Py_DECREF(ret);
      }
      Py_DECREF(pop);
    }
    if (ros_message->knot_vector.size > 0) {
      // populating the array.array using the frombytes method
      PyObject * frombytes = PyObject_GetAttrString(field, "frombytes");
      assert(frombytes != NULL);
      double * src = &(ros_message->knot_vector.data[0]);
      PyObject * data = PyBytes_FromStringAndSize((const char *)src, ros_message->knot_vector.size * sizeof(double));
      assert(data != NULL);
      PyObject * ret = PyObject_CallFunctionObjArgs(frombytes, data, NULL);
      Py_DECREF(data);
      Py_DECREF(frombytes);
      if (!ret) {
        Py_DECREF(field);
        return NULL;
      }
      Py_DECREF(ret);
    }
    Py_DECREF(field);
  }
  {  // control_points
    PyObject * field = NULL;
    size_t size = ros_message->control_points.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    vda5050_msgs__msg__ControlPoint * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->control_points.data[i]);
      PyObject * pyitem = vda5050_msgs__msg__control_point__convert_to_py(item);
      if (!pyitem) {
        Py_DECREF(field);
        return NULL;
      }
      int rc = PyList_SetItem(field, i, pyitem);
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    {
      int rc = PyObject_SetAttrString(_pymessage, "control_points", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
