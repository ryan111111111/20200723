# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:55:35 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
a=2
for i in range(8):
    for i in range(a):
        mc.spawnEntity(x,y,z,69)
    a=a*2
    mc.postToChat(str(a))