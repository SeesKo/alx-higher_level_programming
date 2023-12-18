#include <Python.h>

void display_python_list(PyObject *p);
void display_python_bytes(PyObject *p);
void display_python_float(PyObject *p);

/**
 * display_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void display_python_list(PyObject *p)
{
	Py_ssize_t list_size, capacity, index;
	const char *data_type;
	PyListObject *python_list = (PyListObject *)p;
	PyVarObject *python_var = (PyVarObject *)p;

	list_size = python_var->ob_size;
	capacity = python_list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", capacity);

	for (index = 0; index < list_size; index++)
	{
		data_type = python_list->ob_item[index]->ob_type->tp_name;
		printf("Element %ld: %s\n", index, data_type);

		// Check data type and call corresponding function
		if (strcmp(data_type, "bytes") == 0)
			display_python_bytes(python_list->ob_item[index]);
		else if (strcmp(data_type, "float") == 0)
			display_python_float(python_list->ob_item[index]);
	}
}

/**
 * display_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void display_python_bytes(PyObject *p)
{
	Py_ssize_t byte_size, i;
	PyBytesObject *python_bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_size = ((PyVarObject *)p)->ob_size;
	printf("size: %ld\n", byte_size);

	printf("trying string: %s\n", python_bytes->ob_sval);

	byte_size = (byte_size >= 10) ? 10 : byte_size + 1;

	printf("first %ld bytes: ", byte_size);
	for (i = 0; i < byte_size; i++)
	{
		printf("%02hhx", python_bytes->ob_sval[i]);
		if (i == (byte_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * display_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void display_python_float(PyObject *p)
{
	char *result_buffer = NULL;
	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	result_buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("value: %s\n", result_buffer);
	PyMem_Free(result_buffer);
}
