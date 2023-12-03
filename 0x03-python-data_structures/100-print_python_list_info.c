#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - Print information about a Python list
 * @p: PyObject representing the list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

	/* Print general information about the list */
	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n", list->allocated);

	/* Print information about each element in the list */
	for (Py_ssize_t i = 0; i < Py_SIZE(p); i++)
	{
		PyObject *element = PyList_GetItem(p, i);
		const char *type_name = Py_TYPE(element)->tp_name;

		printf("Element %ld: %s\n", i, type_name);
	}
}
