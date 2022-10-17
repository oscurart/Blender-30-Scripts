import bpy

vi = 0
edgelist = []
vertlist = []

for stroke in bpy.data.grease_pencils[0].layers[0].frames[0].strokes:

    
    for p in stroke.points:
        vertlist.append(p.co) 
    
    cantPuntos= len(stroke.points)-1    
    
    for a in range(0,cantPuntos):
        edgelist.append((vi,vi+1))
        vi = vi+1

    vi += 1 
    
me = bpy.data.meshes.new("data")
gpdb = bpy.data.objects.new("Annotation", me)
me.from_pydata(vertlist,edgelist,[])
me.update()
bpy.context.scene.collection.objects.link(gpdb)
    
