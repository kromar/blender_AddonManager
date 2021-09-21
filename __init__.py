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


if "bpy" in locals():
    import importlib
    importlib.reload(preferences)
    importlib.reload(addon_updater)
    importlib.reload(addon_manager)
else:
    from . import preferences
    from . import addon_updater
    from . import addon_manager

import bpy
import os
import bpy.utils.previews


bl_info = {
    "name": "Addon Manager",
    "description": "Addon Manager",
    "author": "Daniel Grauer",
    "version": (0, 1, 0),
    "blender": (2, 93, 0),
    "location": "Preferences",
    "doc_url": "https://github.com/kromar/blender_AddonManager/wiki",                
    "tracker_url": "https://github.com/kromar/blender_AddonManager/issues/new",
    "category": "!System"}


classes = (
    preferences.AddonPreferences,
    addon_updater.AddonUpdater_OT_SearchUpdates,
    addon_manager.AddonManager_OT_SearchTrackers,
    )


def register():
    [bpy.utils.register_class(c) for c in classes]
    #bpy.types.TOPBAR_HT_upper_bar.append(addon_manager.draw_addon_manager_buttons)


def unregister():
    #bpy.types.TOPBAR_HT_upper_bar.remove(addon_manager.draw_addon_manager_buttons)
    [bpy.utils.unregister_class(c) for c in classes]
