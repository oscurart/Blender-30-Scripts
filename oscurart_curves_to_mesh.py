import bpy

vi = 0
edgelist = []
vertlist = []

for stroke in bpy.context.object.data.curves:

    
    for p in stroke.points:
        vertlist.append(p.position) 
    
    cantPuntos= len(stroke.points)-1    
    
    for a in range(0,cantPuntos):
        edgelist.append((vi,vi+1))
        vi = vi+1

    vi += 1 

me = bpy.data.meshes.new("data")
gpdb = bpy.data.objects.new("Curves", me)
me.from_pydata(vertlist,edgelist,[])
me.update()
bpy.context.scene.collection.objects.link(gpdb)
    
