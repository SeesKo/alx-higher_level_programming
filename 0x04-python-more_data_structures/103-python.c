#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Pointer to the Python object.
 *
 * Return: Void.
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t length, i;

	printf("[.] bytes object info\n");

	/* Check if the given object is a bytes object */
	if (!PyBytes_Check(p))
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{
		/* Extract string and size information from the bytes object */
		PyBytes_AsStringAndSize(p, &str, &length);

		/* Print size and initial portion of the string */
		printf("  size: %lu\n", length);
		printf("  trying string: %s\n", str);

		/* Display the first 10 bytes or the entire string if it's shorter */
		if (length > 10)
			length = 10;
		else
			length++;

		printf("  first %lu bytes: ", length);
		for (i = 0; i < length - 1; i++)
			printf("%02x ", str[i] & 0xff);

		printf("%02x\n", str[length - 1] & 0xff);
	}
}

/**
 * print_python_list - Prints information about a Python list object.
 * @p: Pointer to the Python object.
 *
 * Return: Void.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyObject *list;

	/* Check if the given object is a Python list */
	if (PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		/* Iterate through the list elements */
		for (i = 0; i < PyList_Size(p); i++)
		{
			list = PySequence_GetItem(p, i);
			printf("Element %lu: %s\n", i, list->ob_type->tp_name);

			/* If the element is a bytes object, print its information */
			if (strcmp(list->ob_type->tp_name, "bytes") == 0)
				print_python_bytes(list);
		}
	}
}
