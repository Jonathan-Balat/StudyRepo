#include "opaque.h"
// #include <alloca.h>

/*
Allocation schemes:
There are three approaches to generating an opaque object, as its size isn't clear to accessors outside the opaque class. Approaches are:
1. Stack allocation (not familiar) - uses alloca and is automatically released upon function exit.
2. Dynamic allocation - uses malloc, can fragment when not managed correctly.
3. Static allocation - uses a static variable in the opaque.c, but can be thread unsafe and can lead to issues if multiple instances are needed.
*/

int main(void)
{  
    // 2) Dynamic Allocation (less preferred as creating and destroying objects can lead to fragmentation if not managed correctly)
    struct opaque *obj2 = opaque_create();
    opaque_init(obj2);
    opaque_set_data(obj2, 456);
    opaque_deinit(obj2);
    opaque_free(obj2);

    // 3) Static Allocation (not thread safe, can lead to issues if multiple instances are needed)
    opaque_init_static_instance();
    struct opaque *obj3 = opaque_get_static_instance(); // Pointer to static instance
    opaque_set_data(obj3, 789);
    opaque_deinit_static_instance();

    return 0;
}