
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


import bpy
import addon_utils
from bpy.types import Operator 

def prefs():
    user_preferences = bpy.context.preferences
    return user_preferences.addons[__package__].preferences 

    
def draw_addon_manager_buttons(self, context):
    if context.region.alignment != 'RIGHT':
        layout = self.layout
        row = layout.row(align=True)

        row.operator(operator="addon_updater.check_updates", text="", emboss=True, icon='FILE_REFRESH')

class AddonManager_OT_SearchTrackers(Operator):
    '''search the installed addons for valid tracker urls to populate the updater list'''
    bl_idname = "addon_manager.search_trackers"
    bl_label = "Search Addon Trackers" 
    
    def execute(self, context): 
        self.find_addon_trackers()
        return{'FINISHED'}
    
    def find_addon_trackers(self):        
        tracked_addons = []  
        untracked_addons = []      
        for mod in addon_utils.modules():
            if mod.bl_info.get('tracker_url') and 'git' in mod.bl_info.get('tracker_url'):
                print(mod.bl_info.get('name'))
                print("    \_____", mod.bl_info.get('tracker_url'))
                tracked_addons.append((mod.bl_info.get('name'), mod.bl_info.get('tracker_url')))
            else:
                #print('============', mod.bl_info.get('name'))            
                untracked_addons.append((mod.bl_info.get('name'), 'NONE'))
                
        print('============')  
        
            