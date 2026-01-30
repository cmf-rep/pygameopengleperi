from OpenGL.GL import *
import numpy as np
import ctypes

def create_square():
    square_vertices = np.array([
        #-3,2,
        #-1,4,
        #0,2,
        #-2,0,
        #-1,0,
        #1,2,
        #2,1,
        #0,-1,
        #1,-2,
        #3,0,
        #4,-2,
        #2,-4,
        -6,6,
        -6,4,
        -1,4,
        -1,1,
        -6,1,
        -6,-6,
        -4,-6,
        -4,-1,
        -1,-1,
        -1,-6,
        6,-6,
        6,-4,
        1,-4,
        1,-1,
        6,-1,
        6,6,
        4,6,
        4,1,
        1,1,
        1,6
        
       
    ], dtype=np.float32)

    indices = np.array([
        19,0,1,
        2,19,9,
        12,11,10,
        9,12,3,
        8,4,7,
        6,5,4,
        7,18,14,
        17,15,16
        
    ], dtype=np.uint32)

    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)
    EBO = glGenBuffers(1)

    glBindVertexArray(VAO)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, square_vertices.nbytes, square_vertices, GL_STATIC_DRAW)

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return VAO, EBO, len(indices)

