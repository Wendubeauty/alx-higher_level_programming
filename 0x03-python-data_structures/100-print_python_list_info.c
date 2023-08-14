#include <Python.h>

/**
 * print_python_list_info - Prints basic information about a Python list.
 * @p: A pointer to a PyObject representing a Python list.
 */
void print_python_list_info(PyObject *p)
{
    int size, allocated, i;
    PyObject *item;

    size = Py_SIZE(p); // Get the size of the list
    allocated = ((PyListObject *)p)->allocated; // Get the allocated memory

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", allocated);

    // Iterate through the list and print element types
    for (i = 0; i < size; i++)
    {
        printf("Element %d: ", i);

        item = PyList_GetItem(p, i); // Get the item at index i
        printf("%s\n", Py_TYPE(item)->tp_name); // Print the type name
    }
}
