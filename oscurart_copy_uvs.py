#copy active uvs
#copy from active to selected
#select all models and run. Active will be the object with the desired uv.
import bpy

selobs = [ ob for ob in bpy.context.selected_objects]

selobs.remove(bpy.context.active_object)    

ob = bpy.context.active_object


for targetOb in selobs:
    for source,target in zip(ob.data.uv_layers.active.data,targetOb.data.uv_layers.active.data):
        target.uv = source.uv