#include <Python.h>
#include <stdio.h>
#include <objects.h>
#include <listobject.h>

/**
 * print_python_list - prints information about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		Py_ssize_t i;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List: %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; i++)
			printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
	else
		fprintf(stderr, "Invalid List Object\n");
}

/**
 * print_python_bytes - prints information about Python bytes objects
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		Py_ssize_t size = PyBytes_Size(p);
		Py_ssize_t i;

		printf("[.] bytes object info\n");
		printf("size: %ld\n", size);
		printf("trying string: %s\n", PyBytes_AS_STRING(p));

		if (size > 10)
			size = 10;

		printf("first %ld bytes: ");
		for (i = 0; i < size; i++)
		{
			printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
			if (i < size - 1)
				printf(" ");
		}
		printf("\n");
	}
	else
		fprintf(stderr, "Invalid Bytes Object\n");
}
