#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: Pointer to a Python object
 */
void print_python_string(PyObject *p)
{
Py_ssize_t length;
Py_ssize_t i;
const char *str;

printf("[.] string object info\n");

if (!PyUnicode_Check(p))
{
printf("  [ERROR] Invalid String Object\n");
return;
}

length = PyUnicode_GET_LENGTH(p);
str = PyUnicode_AsUTF8(p);

printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
printf("  length: %ld\n", length);
printf("  value: %s\n", str);
}
