from stl import mesh, Mode
# specify the path of our stl model

stl_path = "/Volumes/Studies/3D Objects and STL/STL_FILES/mini_car.stl"

stl_model = mesh.Mesh.from_file(stl_path)

# If we want faces alone 

vectors = stl_model.vectors
normals = stl_model.normals

print(vectors[:10])
print(normals[:10])

stl_model.save("/Volumes/Studies/3D Objects and STL/STL_FILES/mini_car_ascii.stl", mode= Mode.ASCII)
