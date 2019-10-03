# coding: utf-8
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/output"

# Set local variables
inRaster = "C:/output/CollegeStationElevation.tif"
outRaster = "C:/output/HillshadeCS"
azimuth = 180
altitude = 75
modelShadows = "SHADOWS"
zFactor = 0.348

# Execute HillShade
arcpy.HillShade_3d(inRaster, outRaster, azimuth, altitude, 
                   modelShadows, zFactor)