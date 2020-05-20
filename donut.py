import bpy
import bmesh
from random import randint

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
bpy.ops.mesh.primitive_torus_add(major_radius = 0.05, minor_radius=0.025)

bpy.ops.object.editmode_toggle()
context = bpy.context
bm = bmesh.from_edit_mesh(context.edit_object.data)
bm.verts.ensure_lookup_table()
for v in bm.verts:
    v.select = False
bm.verts[10].select=True
bm.verts[190].select=True
bm.verts[286].select = True
bm.verts[415].select = True

bpy.context.scene.tool_settings.use_proportional_edit = True

bpy.ops.transform.translate(value=(-0.00609417, 0.00408091, -0.00107364), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=True, proportional_edit_falloff='SMOOTH', proportional_size=0.0323492, use_proportional_connected=False, use_proportional_projected=False)
for v in bm.verts:
    v.select = False
bpy.ops.mesh.select_all(action="DESELECT")
bm.faces.ensure_lookup_table()
faces_start_points = [1,2,3,4]
for v in faces_start_points:
    for i in range(0,48):
        bm.faces[v+i*12].select=True

bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
bpy.ops.mesh.separate(type="SELECTED")
bpy.ops.object.editmode_toggle()
print(list(bpy.data.objects))
bpy.context.active_object.name = "donut"
for obj in bpy.data.objects:
    if obj.name!="donut":
        obj.name="iceing"
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.shade_smooth()
for obj in bpy.data.objects:
    bpy.context.view_layer.objects.active  = obj
    bpy.ops.object.modifier_add(type="SUBSURF")
iceing = bpy.data.objects["iceing"]
bpy.context.view_layer.objects.active= iceing
bpy.ops.object.modifier_add(type="SOLIDIFY")
bpy.data.objects["iceing"].modifiers["Solidify"].offset=1.0
bpy.data.objects["iceing"].modifiers["Solidify"].thickness=0.002
bpy.ops.object.modifier_move_down(modifier="Subdivision")
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.editmode_toggle()
bpy.context.object.modifiers["Solidify"].show_in_editmode = False
bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.mesh.subdivide()
bm = bmesh.from_edit_mesh(bpy.context.edit_object.data)
bm.verts.ensure_lookup_table()
bm.edges.ensure_lookup_table()
bpy.ops.mesh.select_all(action="DESELECT")
verts_of_imp = [240]
for v in range(0,240,5):
    verts_of_imp.append(v)
for v in range(253,668,9):
    verts_of_imp.append(v)

for edge in bm.edges:
    edge.select=True

for edge in bm.edges:
    x = edge.verts[0].index
    y = edge.verts[1].index
    if x in verts_of_imp and y in verts_of_imp:
        edge.select=False
bpy.ops.mesh.hide(unselected=False)
bpy.context.scene.tool_settings.snap_elements = {'FACE'}

bpy.context.scene.tool_settings.use_snap_project = True
bpy.context.scene.tool_settings.use_snap_self = False

bm.verts[478].select=True
bpy.ops.transform.translate(value=(-0.00351654, -0.00278462, -0.00966164), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=True, proportional_edit_falloff='SMOOTH', proportional_size=0.0166002, use_proportional_connected=False, use_proportional_projected=False)
bm.verts[478].select=False
bm.verts[388].select=True
bpy.ops.transform.translate(value=(-0.00295906, 0.0024102, -0.0116511), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=True, proportional_edit_falloff='SMOOTH', proportional_size=0.0267348, use_proportional_connected=False, use_proportional_projected=False)
bm.verts[388].select=False
bm.verts[30].select=True
bpy.ops.transform.translate(value=(0.00192655, 0.0037049, -0.0070949), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=True, proportional_edit_falloff='SMOOTH', proportional_size=0.0220949, use_proportional_connected=False, use_proportional_projected=False)
bm.verts[30].select=False
bm.verts[0].select=True
bpy.ops.transform.translate(value=(0.0021398, -0.00151541, -0.00745702), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=True, proportional_edit_falloff='SMOOTH', proportional_size=0.0220949, use_proportional_connected=False, use_proportional_projected=False)
bm.verts[0].select=False
bm.verts[190].select=True
bpy.ops.transform.translate(value=(0.00181161, -0.00455373, -0.0100743), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=True, proportional_edit_falloff='SMOOTH', proportional_size=0.0200863, use_proportional_connected=False, use_proportional_projected=False)
bm.verts[190].select=False
bm.verts[165].select=True

bpy.ops.transform.translate(value=(-0.00175121, -0.00280249, -0.00689739), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=True, proportional_edit_falloff='SMOOTH', proportional_size=0.0166002, use_proportional_connected=False, use_proportional_projected=False)
bm.verts[165].select=False
bpy.ops.mesh.reveal()
bpy.ops.object.editmode_toggle()
donut = bpy.data.objects["donut"]
bpy.context.view_layer.objects.active= donut
bpy.ops.object.light_add(location=(1,0,0),type="POINT")
bpy.context.object.data.energy = 30

bpy.ops.transform.translate(value=(0.0352137, -0.0963782, -0.0944191), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=True, proportional_edit_falloff='SMOOTH', proportional_size=0.00437136, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.translate(value=(-0.660988, -0.000605613, 0.304262), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=True, proportional_edit_falloff='SMOOTH', proportional_size=0.0166002, use_proportional_connected=False, use_proportional_projected=False)

bpy.ops.transform.translate(value=(-0.0127333, -0.0623953, 0.170317), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=True, proportional_edit_falloff='SMOOTH', proportional_size=0.0029857, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.mesh.primitive_plane_add(location=(0,0,-0.020))

bpy.context.scene.render.engine = 'CYCLES'

bpy.context.scene.cycles.device = 'GPU'
bpy.ops.object.camera_add(location=(0.30383  ,-0.28981  ,0.2307 ),rotation=(63.6,0,46.7),align="CURSOR")
bpy.ops.transform.translate(value=(-0.281124, 0.339831, -0.187616), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=0.000106243, use_proportional_connected=False, use_proportional_projected=False)

#objectToSelect = bpy.data.objects["Plane"]
#objectToSelect.select_set(True)  
#bpy.context.view_layer.objects.active = objectToSelect
#bpy.data.materials["Material.018"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.0144029, 0.736794, 0.8, 1)
#bpy.data.materials["Material.018"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.0144029, 0.736794, 0.8, 1)

#activeObject = bpy.context.active_object #Set active object to variable
#mat = bpy.data.materials["Material.018"] #set new material to variable
#activeObject.data.materials.append(mat)



objectToSelect = bpy.data.objects["iceing"]
objectToSelect.select_set(True)  

bpy.context.view_layer.objects.active = objectToSelect
 #Set active object to variable
mat = bpy.data.materials.new(name="iceing_mat")
mat.use_nodes=True
mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.162481, 0.554308, 1)
 #set new material to variable
objectToSelect.data.materials.append(mat)
bpy.context.object.active_material = mat


objectToSelect = bpy.data.objects["donut"]
objectToSelect.select_set(True)  

bpy.context.view_layer.objects.active = objectToSelect
 #Set active object to variable
mat = bpy.data.materials.new(name="donut_mat")
mat.use_nodes=True
mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.277431, 0.0240143, 1)
 #set new material to variable
objectToSelect.data.materials.append(mat)
bpy.context.object.active_material = mat

objectToSelect = bpy.data.objects["Plane"]
objectToSelect.select_set(True)  

bpy.context.view_layer.objects.active = objectToSelect
 #Set active object to variable
mat = bpy.data.materials.new(name="plane_mat")
mat.use_nodes=True
mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.0256643, 0.8, 0.772547, 1)
 #set new material to variable
objectToSelect.data.materials.append(mat)
bpy.context.object.active_material = mat
