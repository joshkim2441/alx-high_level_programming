#include <Python.h>

void print_python_list(PyObject *p)
{
	long int size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [Error] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	long int size, i;
	char *str;

	printf("[*] Python bytes\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	str = PyBytes_AsString(p);
	size = PyBytes_Size(p);
	printf("  Size of Python Bytes = %ld\n", size);
	printf("  Trying string: %s\n", str);
	printf("  First 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx ", str[i]);
	}
	printf("\n");
}
