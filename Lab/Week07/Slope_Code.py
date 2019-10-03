# coding: utf-8
import arcpy
from arcpy import env
env.workspace = "C:/output"
inRaster = "C:/output/CollegeStationElevation.tif"
outRaster = "C:/output/SlopeCS"
outMeasurement = "DEGREE"
zFactor = ""
method = "GEODESIC"
zUnit = "METER"
arcpy.Slope_3d(inRaster, outRaster, outMeasurement, zFactor, method, zUnit)
# <Result 'C:\\output\\SlopeCS'>