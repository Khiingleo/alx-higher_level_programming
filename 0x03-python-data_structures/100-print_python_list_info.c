#include <Python.h>

/**
 * print_python_list_info - ===
 * @p: ====
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	int alloc;
	PyObject *item;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
