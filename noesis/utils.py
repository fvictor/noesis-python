import javabridge as jb
import numpy as np
import math
from itertools import product

def class_exists(class_name):
    return jb.run_script('exists = true; try { java.lang.Class.forName(\''+class_name+'\'); } catch(e) { exists = false; }  exists;')

def get_class_wrapper(class_name, packages):
    for package in packages:
        class_id = package+'.'+class_name
        if(class_exists(class_id)):
            return jb.JClassWrapper(class_id)

    raise ValueError('{} is not a valid method'.format(class_name))

def java_int_array_to_list(jv_array):
    return jb.get_env().get_int_array_elements(jv_array.o).tolist()

def java_matrix_to_numpy(jv_matrix):
    rows = jv_matrix.rows()
    columns = jv_matrix.columns()
    np_matrix = np.zeros( (rows, columns) )
    for row_idx, col_idx in product(range(rows), range(columns)):
        np_matrix[row_idx][col_idx] = jv_matrix.get(row_idx, col_idx)
    return np_matrix

def java_collection_to_list(jv_collection, transform):
    return [transform(jv_collection.get(i)) for i in range(jv_collection.size())]

def java_one_row_matrix_to_list(jv_matrix, transform):
    return [transform(jv_matrix.get(0,i)) for i in range(jv_matrix.columns())]
