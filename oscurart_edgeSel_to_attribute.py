#select edges, active attr and run

import bpy

mode = bpy.context.object.mode
bpy.ops.object.mode_set(mode="OBJECT")

for edge in bpy.context.object.data.edges:
    bpy.context.object.data.attributes.active.data[edge.index].value = True if edge.select else False    

bpy.ops.object.mode_set(mode="%s" % (mode))