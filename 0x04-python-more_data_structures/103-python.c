#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints information about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid Python List\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List: %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - prints information about Python bytes objects
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *buffer;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	buffer = ((PyBytesObject *)p)->ob_sval;

	printf("  [.] size: %ld\n", size);
	printf("  [.] trying string: %s\n", buffer);

	if (size > 10)
		size = 10;

	printf("  [.] first %ld bytes: ");

	for (i = 0; i < size; i++)
	{
		printf("%02hhx", buffer[i]);
		if (i < size - 1)
			printf(" ");

	}
	printf("\n");
}
