"""
Util functions
"""

import javabridge as jb
import numpy as np
from itertools import product

def class_exists(class_name):
    """Check if the given class exists and return True, or False, otherwise."""
    script = 'exists = true; try { java.lang.Class.forName(\''+class_name+'\'); } catch(e) { exists = false; }  exists;'
    return jb.run_script(script)

def get_class_wrapper(class_name, packages, tail=None):
    """Get a wrapper for a given class, with an optional defined tail, by checking in the list of specified packages."""
    if tail is not None and not class_name.endswith(tail):
        class_name += tail
    for package in packages:
        class_id = package+'.'+class_name
        if(class_exists(class_id)):
            return jb.JClassWrapper(class_id)

    raise ValueError('{} is not a valid method'.format(class_name))

def java_int_array_to_list(jv_array):
    """Get a Java array of integers as a Python list."""
    return jb.get_env().get_int_array_elements(jv_array.o).tolist()

def java_matrix_to_numpy(jv_matrix):
    """Get a Java matrix as a numpy multidimensional array."""
    rows = jv_matrix.rows()
    columns = jv_matrix.columns()
    np_matrix = np.zeros( (rows, columns) )
    for row_idx, col_idx in product(range(rows), range(columns)):
        np_matrix[row_idx][col_idx] = jv_matrix.get(row_idx, col_idx)
    return np_matrix

def java_collection_to_numpy(jv_collection, transform):
    """Get a Java collection as a numpy array."""
    return np.array([transform(jv_collection.get(i)) for i in range(jv_collection.size())])

def java_one_row_matrix_to_list(jv_matrix, transform):
    """Get the first row from a Java matrix as a Python list."""
    return [transform(jv_matrix.get(0,i)) for i in range(jv_matrix.columns())]
