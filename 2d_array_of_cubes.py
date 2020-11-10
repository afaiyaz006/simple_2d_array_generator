bl_info = {
    "name": "2D Array of Cubes",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy


class create_array(bpy.types.Operator):
		"""Create 2D Array of Cube"""     
		bl_idname = "object.create_array"        
		bl_label = "Create Array"         
		bl_options = {'REGISTER', 'UNDO'}
		flag=True
		row_numbers:bpy.props.IntProperty(name="Number of rows",default=10,min=1,max=20)
		col_numbers:bpy.props.IntProperty(name="Number of columns",default=10,min=1,max=20)
		cube_size:bpy.props.IntProperty(name="Cube Size",default=1,min=1,max=10)
		min_dis:bpy.props.FloatProperty(name="Minimum distance",default=0.1,min=0,max=100)
		
		def create_cubes(self,loc):
			#create the main cube
			if not self.flag:
				bpy.ops.mesh.primitive_cube_add(location=loc,size=self.cube_size)
				bpy.ops.object.duplicate
			#copy object and place its location	
			else:
				scene=bpy.context.scene
				cube=bpy.context.active_object
				cubes=cube.copy()
				self.scene.collection.objects.link(cubes)
				cubes.location=loc
				

			
		def execute(self, context):        
			row_factor=0
			col_factor=0
			#generating cubes row and column wise
			for posy in range(1,self.col_numbers+1):
				if(posy==1):
					self.flag=False
				col_factor=posy*(self.cube_size+self.min_dis)
				for posx in range(1,self.row_numbers+1):
					row_factor=posx*(self.cube_size+self.min_dis)
					loc=(posx+row_factor,posy+col_factor,0)
					self.create_cubes(loc)
				
			return {'FINISHED'}    
			        
def menu_func(self,context):
	self.layout.operator(create_array.bl_idname)

def register():
    bpy.utils.register_class(create_array)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(create_array)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()
             


