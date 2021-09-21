# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

if "bpy" in locals():
    import importlib
    importlib.reload(addon_updater)
else:
    from . import addon_updater
    
"""Addon preferences"""
import bpy
import os
from bpy.types import AddonPreferences
from bpy.props import ( StringProperty, 
                        BoolProperty, 
                        FloatProperty,
                        EnumProperty)


class AddonPreferences(AddonPreferences):
    bl_idname = __package__

    ############################################
    #       ADDON UPDATER    
    ############################################
    repository_path: StringProperty(
        name="Project", 
        description="Github Project url example: https://github.com/JoseConseco/GoB", 
        subtype='DIR_PATH',
        default="https://github.com/JoseConseco/GoB") 
    
    zip_filename: StringProperty(
        name="zip_filename", 
        description="zip_filename", 
        subtype='FILE_PATH',
        default="blender_addon_updater.zip") 

    auto_update_check: BoolProperty(
        name="Check for updates automaticaly",
        description="auto_update_check",
        default=False)

    experimental_versions: BoolProperty(
        name="Experimental Verions",
        description="Check for experimental verions",
        default=False)
    ############################################

    
  
    def draw(self, context):
        # GoB Troubleshooting
        layout = self.layout
        layout.use_property_split = True

      
        #advanced & dev options
        #         
        ############################################
        #       ADDON UPDATER
        ############################################
        box = layout.box() 
        box.label(text='Addon Updater', icon='PREFERENCES')  
        col  = box.column(align=False) 
        row  = col.row(align=False)         
        
        row.operator("addon_updater.check_updates", text="Check for Updates", icon='FILE_REFRESH', depress=False).button_input = 0
        
        if addon_updater.update_available == False:
            row.operator("addon_updater.check_updates", text="Addon is up to date", icon='IMPORT', emboss=True, depress=True).button_input = -1
        
        elif addon_updater.update_available == None:
            row.operator("addon_updater.check_updates", text="nothing to show", icon='ERROR', emboss=False, depress=True).button_input = -1
        
        elif addon_updater.update_available == 'TIME':
            row.operator("addon_updater.check_updates", text="Limit exceeded! Try again later", icon='COLORSET_01_VEC', emboss=False, depress=True).button_input = -1
        
        else:
            row.operator("addon_updater.check_updates", text="Download: " + addon_updater.update_available, icon='COLORSET_03_VEC').button_input = 1
        
        col  = box.column(align=False)              
        col.prop(self, 'repository_path') 
        #col.prop(self, 'zip_filename')
        col.prop(self, 'experimental_versions') 
        #col.prop(self, 'auto_update_check')

        ############################################

 
