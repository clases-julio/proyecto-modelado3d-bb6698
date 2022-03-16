import bpy
import bmesh
from math import radians

'''*********************************************************************'''
'''Funciones comunes útiles para selección/activación/borrado de objetos'''
'''*********************************************************************'''
def seleccionarObjeto(nombreObjeto): # Seleccionar un objeto por su nombre
    bpy.ops.object.select_all(action='DESELECT') # deseleccionamos todos...
    bpy.ops.object.select_pattern(pattern=nombreObjeto) # ...excepto el buscado

def activarObjeto(nombreObjeto): # Activar un objeto por su nombre
    bpy.ops.object.select_pattern(pattern=nombreObjeto)
    bpy.context.active_object.select_set(state=True)

def borrarObjeto(nombreObjeto): # Borrar un objeto por su nombre
    seleccionarObjeto(nombreObjeto)
    bpy.ops.object.delete(use_global=False)

def borrarObjetos(): # Borrar todos los objetos
    if(len(bpy.data.objects) != 0):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        
        
def unirObjetos(objetos):
    for obj in objetos:
       activarObjeto(obj)
    bpy.ops.object.join()
    
def cambiarColor(R, G, B):
    activeObject = bpy.context.active_object
    mat = bpy.data.materials.new("")
    activeObject.data.materials.append(mat)
    bpy.context.object.active_material.diffuse_color = (R, G, B, 1)
    

def borrarObjetosExcepto(objetos):
    if(len(bpy.data.objects) != 0):
        bpy.ops.object.select_all(action='SELECT')
        for obj in objetos:
            bpy.data.objects[obj].select_set(False)
        bpy.ops.object.delete(use_global=False)
    
        

'''****************************************************************'''
'''Clase para realizar transformaciones sobre objetos seleccionados'''
'''****************************************************************'''
class Seleccionado:
    def mover(v):
        bpy.ops.transform.translate(
            value=v, constraint_axis=(True, True, True))

    def escalar(v):
        bpy.ops.transform.resize(value=v, constraint_axis=(True, True, True))

    def rotarX(v):
        bpy.ops.transform.rotate(value=v, orient_axis='X')

    def rotarY(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Y')

    def rotarZ(v):
        bpy.ops.transform.rotate(value=v, orient_axis='Z')

'''**********************************************************'''
'''Clase para realizar transformaciones sobre objetos activos'''
'''**********************************************************'''
class Activo:
    def posicionar(v):
        bpy.context.object.location = v

    def escalar(v):
        bpy.context.object.scale = v

    def rotar(v):
        bpy.context.object.rotation_euler = v

    def renombrar(nombreObjeto):
        bpy.context.object.name = nombreObjeto

'''**************************************************************'''
'''Clase para realizar transformaciones sobre objetos específicos'''
'''**************************************************************'''
class Especifico:
    def escalar(nombreObjeto, v):
        bpy.data.objects[nombreObjeto].scale = v

    def posicionar(nombreObjeto, v):
        bpy.data.objects[nombreObjeto].location = v

    def rotar(nombreObjeto, v):
        bpy.data.objects[nombreObjeto].rotation_euler = v

'''************************'''
'''Clase para crear objetos'''
'''************************'''
class Objeto:
    def crearCubo(objName):
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 0, 0))
        Activo.renombrar(objName)

    def crearEsfera(objName,r):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=(0, 0, 0))
        Activo.renombrar(objName)

    def crearCono(objName):
        bpy.ops.mesh.primitive_cone_add(radius1=0.5, location=(0, 0, 0))
        Activo.renombrar(objName)
        
    def crearTorus(objName):
        bpy.ops.mesh.primitive_torus_add(location=(0, 0, 0), rotation=(0, 0, 0), major_radius=1, minor_radius=0.25, abso_major_rad=1.25, abso_minor_rad=0.75)
        Activo.renombrar(objName)
        
    def crearCiclindro(objName):
        bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(0, 0, 0))
        Activo.renombrar(objName)
        
    def crearIcosfera(objName):
        bpy.ops.mesh.primitive_ico_sphere_add(radius=1, enter_editmode=False, location=(0, 0, 0))
        Activo.renombrar(objName)

class Wheel:
    def create_wheel():
        Objeto.crearTorus('Grossor')
        Seleccionado.rotarX(3.1415/2)
        Seleccionado.escalar((1,1.17,1))

class bb6:
  def crear_rueda_1():
        Objeto.crearTorus('Grossor')
        Seleccionado.rotarX(3.1415/2)
        Seleccionado.escalar((1,1.17,1))
        cambiarColor(0, 0, 0)
        
        Objeto.crearEsfera("Llanta",1.0)
        bpy.data.objects['Llanta'].scale = (1.0,-0.0022,1.00)
        activarObjeto('Llanta')
        cambiarColor(1, 1, 1)

        
        Objeto.crearEsfera("Circulo",0.9)
        bpy.data.objects['Circulo'].scale = (0.169,-0.021,0.171)
        bpy.data.objects['Circulo'].location = (-0.0016,0.0015,0.001196)
        
        Objeto.crearCiclindro("P1")
        bpy.data.objects['P1'].location = (-0.17347,-0.002601,0.428)
        bpy.data.objects['P1'].scale = (0.062,0.001,-0.275)
        bpy.data.objects['P1'].rotation_euler = (0, radians(-30), 0)

       
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0.386203, 0.0678201, -0.0615151), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})

        bpy.context.object.name = 'P2'
        bpy.data.objects['P2'].rotation_euler = (0, radians(90), 0)
        bpy.data.objects['P2'].location = (0.4436,-0.032,0.0056)


        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0.386203, 0.0678201, -0.0615151), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
        bpy.context.object.name = 'P3'
        bpy.data.objects['P3'].rotation_euler = (0, radians(45), 0)
        bpy.data.objects['P3'].location = (-0.3090,-0.038,-0.32533)

        unirObjetos(["Circulo","P1","P2","P3"])
        bpy.context.object.name = 'Decorado'
        activarObjeto('Decorado')
        cambiarColor(0, 0, 0)
        
  def crear_rueda_2():
        Objeto.crearTorus('Grossor')
        Seleccionado.rotarX(3.1415/2)
        Seleccionado.escalar((1,1.17,1))
        cambiarColor(0, 0, 0)
          
        bpy.data.objects['Grossor'].location = (0,3.4025,0)
        Objeto.crearEsfera("Llanta-2",1.0)
        bpy.data.objects['Llanta-2'].scale = (1.0,-0.0022,1.00)
        bpy.data.objects['Llanta-2'].location = (0,3.4025,0)
        seleccionarObjeto('Llanta-2')
        activarObjeto('Llanta-2')
        
        #--cambiarColor(0.9, 0.9, 0.9)

    
    
    
        seleccionarObjeto("Decorado")
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0.386203, 0.0678201, -0.0615151), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":True, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
        bpy.data.objects['Decorado.001'].location = (-0.309,3.4085,-0.32533)
        activarObjeto('Decorado.001')
        cambiarColor(1, 1, 1)
      
  def base_inferior():
      #--CILINDROS DE ABAJO----------------------------------------------------------
        Objeto.crearCiclindro("Soporte-Ruedas-1")
        bpy.data.objects['Soporte-Ruedas-1'].scale = (0.5367,0.496,0.2564)
        bpy.data.objects['Soporte-Ruedas-1'].rotation_euler = (radians(90), 0, 0)
        bpy.data.objects['Soporte-Ruedas-1'].location = (0,0.353,0)
        
        Objeto.crearCiclindro("Soporte-Ruedas")
        bpy.data.objects['Soporte-Ruedas'].scale = (0.5367,0.496,0.2564)
        bpy.data.objects['Soporte-Ruedas'].rotation_euler = (radians(90), 0, 0)
        bpy.data.objects['Soporte-Ruedas'].location = (0,3.0653,0)
        
        unirObjetos(["Soporte-Ruedas-1","Soporte-Ruedas"])
        
    
    
    
  
        Objeto.crearCiclindro("C1")
        bpy.data.objects['C1'].rotation_euler = (radians(90), 0, 0)
        bpy.data.objects['C1'].location = (0,1.673,0)
        bpy.data.objects['C1'].scale = (1,1,1.12)
        
        
        activarObjeto('Soporte-Ruedas')
        cambiarColor(0.6, 0.6, 0.6)
        activarObjeto('C1')
        cambiarColor(1, 1, 1)
        
    
  def crear_logo():
     
        Objeto.crearEsfera("Logo",0.8)
        bpy.data.objects['Logo'].scale = (-0.126,0.277,0.273)
        bpy.data.objects['Logo'].location = (0.90139,1.6941,0.529)
        activarObjeto('Logo')
    
    
  def base_superior():
      
        Objeto.crearCiclindro("S1")
        bpy.data.objects['S1'].location = (-0.0169,1.7189,1.0423)
        bpy.data.objects['S1'].scale = (0.571,0.595,0.1)
        
        Objeto.crearCiclindro("S2")
        bpy.data.objects['S2'].location = (-0.0169,1.7189,1.2852)
        bpy.data.objects['S2'].scale = (0.571,0.821,0.144)
        
        activarObjeto('S1')
        cambiarColor(1, 1, 1)
        activarObjeto('S2')
        cambiarColor(1, 1, 1)
   
    
  def crear_cuerpo():
        Objeto.crearCiclindro("Base")
        bpy.data.objects['Base'].location = (0.0233,1.7148,2.5975)
        bpy.data.objects['Base'].scale = (0.996,0.902,1.124)
        
        activarObjeto('Base')
        cambiarColor(1, 1, 1)
        

    
  def crear_tablet():
        Objeto.crearCubo("Tablet")
        bpy.data.objects['Tablet'].rotation_euler = (radians(90), 0, radians(90))
        bpy.data.objects['Tablet'].scale = (2.165,1.604,0.227)
        bpy.data.objects['Tablet'].location = (1.0566,1.7709,2.8216)
        
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.bevel(offset=0.0462643, offset_pct=0, release_confirm=True)
        bpy.ops.object.editmode_toggle()
     

        
        
        Objeto.crearCubo("Tablet-2")
        bpy.data.objects['Tablet-2'].rotation_euler = (radians(90), 0, radians(90))
        bpy.data.objects['Tablet-2'].scale = (2,1.184,0.150)
        bpy.data.objects['Tablet-2'].location = (1.0841,1.7709,2.8216)
        
        unirObjetos(["Tablet","Tablet-2"])
        
        bpy.data.objects['Tablet-2'].location = (1.0841,1.6628,2.8216) 
        
        activarObjeto('Tablet-2') 
        
  def crear_rostro():
      #--CABEZA
        Objeto.crearEsfera("Cabeza",1)
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.bevel(offset=0.0773576, offset_pct=0, release_confirm=True)
        bpy.ops.object.editmode_toggle()
        
        bpy.data.objects['Cabeza'].rotation_euler = (radians(90), 0, 0)
        bpy.data.objects['Cabeza'].scale = (1.0,0.929,1.466)
        bpy.data.objects['Cabeza'].location = (0,1.6979,4.6389)
        
        activarObjeto('Cabeza')
        cambiarColor(0.9, 0.9, 0.9)
        
        Objeto.crearCiclindro("Cuello")
        bpy.data.objects['Cuello'].location = (-0.0169,1.7189,3.8025)
        bpy.data.objects['Cuello'].scale = (0.571,0.595,0.1)
        
        activarObjeto('Cuello')
        cambiarColor(0, 0, 0)
        
        Objeto.crearTorus("Rostro")
        bpy.data.objects['Rostro'].location = (0,1.6768,4.877)
        
        activarObjeto('Rostro')
        cambiarColor(0.304, 0.522, 0.800)
        
        
        Objeto.crearIcosfera("Ojo-I")
        bpy.data.objects['Ojo-I'].scale = (0.235,0.160,0.199)
        bpy.data.objects['Ojo-I'].location = (1.0745,1.205,4.9242)
        
        Objeto.crearIcosfera("Ojos")
        bpy.data.objects['Ojos'].scale = (0.235,0.160,0.199)
        bpy.data.objects['Ojos'].location = (1.07,1.9783,4.9242)
        
        unirObjetos(["Ojo-I","Ojos"]) 
        
        activarObjeto('Ojos')
        cambiarColor(0, 0, 0)
        
        
    
  def crear_identificador():
        seleccionarObjeto("Tablet-2")
        bpy.ops.view3d.pastebuffer()
        bpy.data.objects['Tablet-2.001'].scale = (0.794,0.373,0.150)
        bpy.data.objects['Tablet-2.001'].location = (1.08,1.9905,3.46)  
        
        activarObjeto('Tablet-2.001')   
        
        
        

'''************'''
''' M  A  I  N '''
'''************'''
if __name__ == "__main__":

    borrarObjetosExcepto(['Camera', 'Light'])
    bb6.crear_rueda_1()
    bb6.crear_rueda_2()
    bb6.base_inferior()
    bb6.base_superior()
    bb6.crear_logo()
    bb6.crear_cuerpo()
    bb6.crear_tablet()
    bb6.crear_rostro()

    
    bpy.ops.object.light_add(type='POINT', location=(-12.931, -10.176, 5.9))
    
