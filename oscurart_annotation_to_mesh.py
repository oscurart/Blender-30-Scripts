import bpy



for stroke in bpy.data.grease_pencils[0].layers[0].frames[0].strokes:

    vertlist = [p.co for p in stroke.points]
    
    cantPuntos= len(stroke.points)-1

    edgelist = []
    i = 0
    for a in range(0,cantPuntos):
        edgelist.append((i,i+1))
        i = i+1


    me = bpy.data.meshes.new("data")
    gpdb = bpy.data.objects.new("gp", me)
    me.from_pydata(vertlist,edgelist,[])
    me.update()
    bpy.context.scene.collection.objects.link(gpdb)
