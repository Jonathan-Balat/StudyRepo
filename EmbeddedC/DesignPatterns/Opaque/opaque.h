/**
 * @file opaque.h
 * @brief Opaque pointer design pattern implementation for embedded C.
 * @author Jonathan Balat
 * @date April 6, 2026
 * @version 1.0
 */

#ifndef __OPAQUE_H__
#define __OPAQUE_H__

#ifdef __cplusplus
extern "C" {
#endif

#include <stddef.h>
#include <stdint.h>

struct opaque;

/**
 * @brief Initializes an opaque object.
 * @param[in,out] self Pointer to opaque object
 * @return 0 on success, non-zero on failure.
 */
int opaque_init(struct opaque *self);

/**
 * @brief Deinitializes an opaque object.
 * @param[in,out] self Pointer to opaque object
 * @return 0 on success, non-zero on failure.
 */
int opaque_deinit(struct opaque *self);

/**
 * @brief Sets the data value in the opaque object.
 * @param[in,out] self Pointer to opaque object
 * @return void 
 */
void opaque_set_data(struct opaque *self, uint32_t data);

/**
 * @brief Retrieves the data value from the opaque object.
 * @param[in,out] self Pointer to opaque object
 * @return The data value stored in the opaque object.
 */
uint32_t opaque_get_data(struct opaque *self);

/**
 * @brief Get the size of the opaque structure. Used for Stack allocation.
 * 
 * @return The size of the opaque structure in bytes.
 */
size_t opaque_size(void);

/**
 * @brief Create a new opaque structure. Used for Dynamic allocation.
 * 
 * @return Pointer to the newly created opaque structure, or NULL on failure.
 */
struct opaque *opaque_create(void);

/**
 * @brief Free an opaque structure. Used for Dynamic allocation.
 * 
 * @param[in,out] obj Pointer to the opaque structure to be freed.
 */
void opaque_free(struct opaque *obj);

/** 
 * @brief Initializes the static instance of the opaque structure. Used for Static allocation.
 * 
 * @return void
 */
void opaque_init_static_instance(void);

/**
 * @brief Get the static instance of the opaque structure. Used for Static allocation.
 * 
 * @return Pointer to the static instance of the opaque structure.
 */
struct opaque *opaque_get_static_instance(void);

/**
 * @brief Deinitializes the static instance of the opaque structure. Used for Static allocation.
 * 
 * @return void
 */
void opaque_deinit_static_instance(void);

#ifdef __cplusplus
}
#endif

#endif /* __OPAQUE_H__ */