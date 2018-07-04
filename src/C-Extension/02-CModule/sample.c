#include "Python.h"

/* int add_int(int, int) */
static PyObject *py_add_int(PyObject *self, PyObject *args) {
  int x, y, result;

  if (!PyArg_ParseTuple(args,"ii", &x, &y)) {
    return NULL;
  }
  result = x + y;
  return Py_BuildValue("i", result);
}

/* double add_float(double, double) */
static PyObject *py_add_float(PyObject *self, PyObject *args) {
  double x, y, result;

  if (!PyArg_ParseTuple(args, "dd", &x, &y)) {
    return NULL;
  }
  result = x + y;
  return Py_BuildValue("d", result);
}

/* Module method table */
static PyMethodDef SampleMethods[] = {
  {"add_int",  py_add_int, METH_VARARGS, "Add 2 int"},
  {"add_float", py_add_float, METH_VARARGS, "Add 2 float"},
  { NULL, NULL, 0, NULL}
};

/* Module structure */
static struct PyModuleDef samplemodule = {
  PyModuleDef_HEAD_INIT,

  "sample",           /* name of module */
  "A sample module",  /* Doc string (may be NULL) */
  -1,                 /* Size of per-interpreter state or -1 */
  SampleMethods       /* Method table */
};

/* Module initialization function */
PyMODINIT_FUNC
PyInit_sample(void) {
  return PyModule_Create(&samplemodule);
}
