#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints information about a Python list.
 * @p: A pointer to a PyObject representing a Python list.
 */
void print_python_list(PyObject *p)
{
	/* Declare variables */
	Py_ssize_t size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	/* Get list size and allocation */
	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	/* Display list information */
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		/* Handle invalid list object */
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	/* Iterate through list elements */
	for (i = 0; i < size; i++)
	{
		/* Get type of the current element */
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);

		/* Check type and call corresponding function */
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: A pointer to a PyObject representing a Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	/* Declare variables */
	Py_ssize_t size, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	/* Display bytes object information */
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		/* Handle invalid Bytes object */
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	/* Determine size for display */
	size = (((PyVarObject *)p)->ob_size >= 10) ? 10 :
		((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints information about a Python float object.
 * @p: A pointer to a PyObject representing a Python float object.
 */
void print_python_float(PyObject *p)
{
	/* Declare variables */
	char *buffer = NULL;
	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	/* Display float object information */
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		/* Handle invalid Float object */
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	/* Convert float to string and display value */
	buffer = PyOS_double_to_string(float_obj->ob_fval,
			'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}
