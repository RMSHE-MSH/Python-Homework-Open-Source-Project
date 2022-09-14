from MountPenglai import MountPenglai
from MountPenglai import MPColorSystem
from MountPenglai import MountPenglaiExamples
from turtle import *

MP = MountPenglai()
MPC = MPColorSystem()
MPE = MountPenglaiExamples()

'''
MP.initgraph(800, 800)

MP.BeginBatchDraw()
MP.line(0, 400, 800, 400)
MP.line(400, 0, 400, 800)
MP.rectangle(0, 0, 800, 800)
'''

# MP.polyline([300, 300, 200, 200, 100, 200])
# MP.rectangle(100, 100, 200, 200, j, 300, 300)
# MP.polygon(300, 300, 100, 6, 0, 300, 300)
# MP.fillrectangle(200, 200, 300, 300)
# MP.fillellipse(10, 10, 590, 400, 45)

# MPC.RGB(255, 255, 255)
# print(MPC.GetRGBValue(MPC.RGB(40, 44, 52)))
'''
for i in range(0, 360, 1):
    R, G, B = MPC.HSVtoRGB(i, 0.5, 0.8)
    fillcolor(MPC.RGB(R, G, B))
    MP.solidpolygon(200, 200, 100, 3, i, 400, 400)
'''
# R, G, B = MPC.HSVtoRGB(128, 0.5, 0.5)

'''
SRGB = []
for i in range(360):
    R, G, B = MPC.HSVtoRGB(i, 0.5, 0.8)
    SRGB.append(MPC.RGB(R, G, B))

Channel = MPC.RGBChannelExtraction(SRGB, "B")
print(Channel)
for i in range(0, 360, 6):
    fillcolor(Channel[i])
    MP.solidpolygon(200, 200, 100, 3, i, 400, 400)
'''

'''
SRGB = []
for i in range(360):
    R, G, B = MPC.HSVtoRGB(i, 0.5, 0.8)
    SRGB.append(MPC.RGB(R, G, B))

Channel = MPC.RGBChannelEdit(SRGB, "B", 0, 0, 128)
print(Channel)
for i in range(0, 360, 6):
    fillcolor(Channel[i])
    MP.solidpolygon(200, 200, 100, 3, i, 400, 400)
'''

'''
SRGB = []
for i in range(360):
    R, G, B = MPC.HSVtoRGB(i, 0.5, 0.8)
    SRGB.append(MPC.RGB(R, G, B))

Channel = MPC.RGBChannelDrift(SRGB, "B", 128, 0, 255)
for i in range(0, 360, 2):
    fillcolor(Channel[i])
    MP.solidpolygon(200, 200, 100, 3, i, 400, 400)
'''
'''
HSV = []
for i in range(360):
    HSV.append(MPC.HSV(i, 0.6, 0.8))

Channel = MPC.HSVChannelExtraction(HSV, "H")

for i in range(0, 360, 8):
    fillcolor(Channel[i])
    MP.solidpolygon(200, 200, 100, 3, i, 400, 400)
    '''

'''
HSV = []
for i in range(360):
    HSV.append(MPC.HSV(i, 0.8, 0.9))

Channel = MPC.HSVChannelDrift(HSV, "H", 60, "H", 0, 360)

for i in range(0, 360, 1):
    fillcolor(Channel[i])
    MP.solidpolygon(200, 200, 90, 25, i, 400, 400)
'''

'''
for i in range(0, 400, 32):
    MP.BeginBatchDraw()
    # MP.clearellipse(200, 200, 600, 400, 45)

    fillcolor(MPC.RGB(30, 30, 30))
    MP.Circle(400, 400, i)
    MP.FlushBatchDraw()
'''

'''
MP.fillroundrect(200, 200, 600, 600, 100, 45)
MP.clearroundrect(300, 300, 500, 500, 50, 45)
'''

'''
for i in range(0, 360, 4):
    pencolor(MPC.HSV(i, 0.6, 0.8))
    MP.ellipse(200, 100, 600, 400, i, 400, 550)
    MP.FlushBatchDraw()
    '''
# MP.fillpie(300, 300, 600, 600, 0, 90)

# MP.drawtext(400, 400, "RMSHE", "Consolas", 32)

# MPE.MPE01()
# MPE.MPE02(16, 1)
# MPE.MPE03()

MPE.MPE04()

MP.saveimage("01")

MP.EndBatchDraw()
done()
