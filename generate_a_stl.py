import numpy as np
from stl import mesh, Mode

# Define the vertices of the 3D Triangle


vertices = np.array([
    [0,0,0],    #vertex O (index 0)
    [1,0,0],    #vertex A (index 1)
    [0.5,0.87,0],   #vertex B (index 2)
    [0.5,0.29,0.82] #vertex C (index 3)
])

# Define the faces (Triangles) with vertex indices

faces = np.array([
    [0,1,3], # Triangle OAC
    [1,2,3], # Triangle ABC
    [0,2,3], # Traingle OBC
    [0,1,2]  # Triangle OAB
])

my_mesh = mesh.Mesh(np.zeros(np.shape(faces)[0], dtype=mesh.Mesh.dtype))
print(my_mesh)

for i, face in enumerate(faces):
    for j in range(3):
        my_mesh.vectors[i][j] = vertices[face[j]]

print(my_mesh.vectors)

# Save the mesh to an ASCII STL File

my_mesh.save('tetrahedron_ASCII.stl', mode=Mode.ASCII)

my_mesh.save('tetrahedron_BINARY.stl', mode=Mode.BINARY)