import bpy
from mathutils import Vector

actObj = bpy.context.object
avg = bpy.context.object.vertex_groups.active

ai = bpy.context.object.vertex_groups.active_index

min = {}
may = {}

for vert in actObj.data.vertices:
    if vert.co[0] >= 0:
        may[vert.co[:]]=vert.index
    else:
        min[vert.co[:]]=vert.index    
        
for minco,index in min.items():
    i = (Vector(minco)*Vector((-1,1,1)))[:]
    print(index,may[i])
    actObj.data.vertices[index].groups[ai].weight = actObj.data.vertices[may[i]].groups[ai].weight