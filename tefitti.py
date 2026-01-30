from OpenGL.GL import *
import numpy as np
import ctypes

def tefitti_left_eye():
    eye_vertices = np.array([
        -3, 4.8,
        -1.7, 4.4,
        -2.2, 4.9,
        -3.58, 5.48,
        -4.96, 5.48,
        -4.8, 5,
        -4.32, 4.7,
        -4.02, 4.46,
        -3.6, 4.16,
        -3, 4,
        -2.88, 3.96,
        -2.8, 3.975,
        -2.25,4,
        -2.2, 4.1,
        -2, 4.2
        
        
       
    ], dtype=np.float32)

    indices = np.array([
       0,1,2,
       3,4,5,
       6,7,8,
       9,10,11,
       12,13,14,
       1
    ], dtype=np.uint32)

    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)
    EBO = glGenBuffers(1)

    glBindVertexArray(VAO)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, eye_vertices.nbytes, eye_vertices, GL_STATIC_DRAW)

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return VAO, EBO, len(indices)


def tefitti_left_iris():
    eye_vertices = np.array([
        -3, 4.8,
        -3.85, 5.35,
        -3.83, 5,
        -3.774, 4.698,
        -3.55, 4.22,
        -3,4,
        -2.426, 4.0033,
        -2.25, 4.44,
        -2.2, 4.6,
        -2.18, 4.7,
        -2.163, 4.835,
        -2.46,5.08,
        -3, 5.3
        
        
       
    ], dtype=np.float32)

    indices = np.array([
       0,1,2,
       3,4,5,
       6,7,8,
       9,10,11,
       12,1
    ], dtype=np.uint32)

    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)
    EBO = glGenBuffers(1)

    glBindVertexArray(VAO)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, eye_vertices.nbytes, eye_vertices, GL_STATIC_DRAW)

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return VAO, EBO, len(indices)

def tefitti_left_pupil():
    eye_vertices = np.array([
        -3, 4.8,
        -3.5, 5.2,
        -3.43,4.8,
        -3.3,4.5,
        
        -3.09,4.34,

        -2.76,4.5,
        -2.64,4.67,
        -2.55,5,
        -3,5.2
        
        
       
    ], dtype=np.float32)

    indices = np.array([
       0,1,2,
       3,4,5,
       6,7,1

    ], dtype=np.uint32)

    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)
    EBO = glGenBuffers(1)

    glBindVertexArray(VAO)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, eye_vertices.nbytes, eye_vertices, GL_STATIC_DRAW)

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return VAO, EBO, len(indices)

def byline ():
    
    f=0
    index=[]
    vertices=[]
    for x in np.arange(-10,10.02,0.02):
        for y in np.arange(10,9.96,-0.02):
            index.extend([f])
            vertices.extend([x,y])
            f+=1
    eye_vertices = np.array(
      vertices
        , dtype=np.float32)
    
    indices = np.array(
        index, dtype=np.uint32)

    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)
    EBO = glGenBuffers(1)

    glBindVertexArray(VAO)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, eye_vertices.nbytes, eye_vertices, GL_STATIC_DRAW)

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return VAO, EBO, len(indices)
