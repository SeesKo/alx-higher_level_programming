#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list.
 * @p: A pointer to a PyObject representing a Python list.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	for (i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: A pointer to a PyObject representing a Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes_data;
	int i;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes_data = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("	[.] size: %ld\n", size);
	printf("	[.] trying string: %s\n", bytes_data);

	if (size > 10)
	{
		printf("	[.] first 10 bytes: ");
		for (i = 0; i < 10; ++i)
			printf("%02x ", bytes_data[i] & 0xFF);

		printf("\n");
	}
	else
	{
		printf("	[.] first %ld bytes: ", size);
		for (i = 0; i < size; ++i)
			printf("%02x ", bytes_data[i] & 0xFF);

		printf("\n");
	}
}

/**
 * print_python_float - Prints information about a Python float object.
 * @p: A pointer to a PyObject representing a Python float object.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("	[.] value: %f\n", PyFloat_AsDouble(p));
}
