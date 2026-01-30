import numpy as np
vertices=[]
for x in np.arange(-10,10.01,0.01):
    for y in np.arange(10,9.98,-0.01):
        vertices.extend([x,y])
eye_vertices = np.array(
      vertices
        , dtype=np.float32)
print(eye_vertices.tolist())
