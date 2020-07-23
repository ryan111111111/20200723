# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 14:14:31 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange
for i in range(10):
    x,y,z=mc.player.getTilePos()
    x=x+i
    for j in range(10):
        r=randrange(16)
        z=z+1
        mc.setBlock(x,y,z,35,r)
r=randrange(1,16)
while True:
    hits=mc.events.pollBlockHits()    
    if len(hits)>0:    
        hit=hits[0]    
        block=mc.getBlockWithData(hit.pos)
        d=block.data
        if d==r:
            mc.postToChat("找到了")
            mc.setBlock(hit.pos,41)
            break             
        
        
        
        