import bpy
import json
import os

file = os.path.basename(bpy.data.filepath)
file = file.rpartition(".")[0]

directorio = "%s/%s.txt" % (os.path.dirname(bpy.data.filepath),file)

with open(directorio, 'w') as f:
    tv = 0
    for ob in bpy.data.objects:
        if ob.type == "MESH":
            if ob.select_get():
                print("%s" % (ob.name))
                print("%s" % (len(ob.data.vertices)))
                ts=0
                qs=0
                ng=0
                for face in ob.data.polygons:
                    if len(face.vertices) == 3:
                        ts+=1
                    if len(face.vertices) == 4:
                        qs+=1
                    if len(face.vertices) >= 3:
                        qs+=1    
                ts = "Tris: %s \n" % (ts)
                qs = "Quads: %s \n" % (qs)  
                qd = "Ngons: %s \n" % (ng)
                f.writelines("----------\n") 
                f.writelines("Object: %s \n" % (ob.name) )
                f.writelines("Vertices: %s \n" % (len(ob.data.vertices)))
                f.writelines(ts) 
                f.writelines(qs)
                f.writelines(qd)
                if hasattr(ob.data.shape_keys,"key_blocks"):
                    f.writelines("Shapes: %s \n" % (len(ob.data.shape_keys.key_blocks)-1))
                else:    
                    f.writelines("Shapes: %s \n" % (0))
                tv += len(ob.data.vertices)   
                
    f.writelines("\n\n///////////////////////////\n\n")            
    f.writelines("Total Vertices: %s" % (tv))                      
print("-------------------------")                                                    