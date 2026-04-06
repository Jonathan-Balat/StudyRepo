/**
 * @file opaque.c
 * @brief Brief description of the opaque module functionality.
 * @details Detailed description of what this module does and how it works.
 * 
 * @author Jonathan Balat
 * @date April 6, 2026
 * @version 1.0
 */

#include "opaque.h"
#include <stdlib.h>
#include <string.h>


struct opaque
{
	uint32_t data;
};

// Static allocation
static struct opaque obj3;


/**
 * @brief Initialize the opaque structure.
 * 
 * @param[in,out] handle Pointer to the opaque handle.
 * @return Status code (0 for success, non-zero for error).
 * 
 * @note This function must be called before using the handle.
 */
int opaque_init(struct opaque *self)
{
	memset(self, 0, sizeof(*self));
	return 0;
}

/**
 * @brief Deinitialize the opaque structure.
 * 
 * @param[in,out] handle Pointer to the opaque handle.
 * @return Status code (0 for success, non-zero for error).
 * 
 * @note This function should be called to clean up resources before freeing the handle.
 */
int opaque_deinit(struct opaque *self)
{
    /* Placeholder deinit for future resource teardown. */
    (void)self;
    return 0;
}

/**
 * @brief Set the data value in the opaque structure.
 * 
 * @param[in,out] handle Pointer to the opaque handle.
 * @return void
 */

void opaque_set_data(struct opaque *self, uint32_t data)
{
	// Validate data if necessary

	// Set data into object
	self->data = data;
}

/**
 * @brief Get the data value from the opaque structure.
 * 
 * @param[in,out] handle Pointer to the opaque handle.
 * @return The data value stored in the opaque structure.
 */
uint32_t opaque_get_data(struct opaque *self)
{
	return self->data;
}

/**
 * @brief Get the size of the opaque structure. Used for Stack allocation.
 * 
 * @return The size of the opaque structure in bytes.
 */
size_t opaque_size(void)
{
	// Simply returns the size of the structure.
	return sizeof(struct opaque);
}

/********** DYNAMIC ALLOCATION EXAMPLE METHODS **********/
/**
 * @brief Create a new opaque structure. Used for Dynamic allocation.
 * 
 * @return Pointer to the newly created opaque structure, or NULL on failure.
 */
struct opaque *opaque_create(void)
{
    struct opaque *obj = malloc(sizeof(struct opaque));
    if (obj != NULL)
    {
        opaque_init(obj);
    }
    return obj;
}
/**
 * @brief Free an opaque structure. Used for Dynamic allocation.
 * 
 * @param[in,out] obj Pointer to the opaque structure to be freed.
 */
void opaque_free(struct opaque *obj)
{
    if (obj != NULL)
    {
        opaque_deinit(obj);
        free(obj);
    }
}

/********** STATIC ALLOCATION EXAMPLE METHODS **********/

void opaque_init_static_instance(void)
{
    obj3.data = 0; // Reset data to default value
    // obj3.pData = &pSomeDataThatExists; // (eg. only) Clear pointer if it exists
}

struct opaque *opaque_get_static_instance(void)
{
    return &obj3;
}

void opaque_deinit_static_instance(void)
{
    obj3.data = 0; // Reset data to default value
    // obj3.pData = NULL; // (eg. only) Clear pointer if it exists
}