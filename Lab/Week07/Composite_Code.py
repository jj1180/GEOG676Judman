# coding: utf-8
import arcpy
source = r"C:/output/KyleField.tif/"
band1 = arcpy.sa.Raster(source + "Band_1") # red
band2 = arcpy.sa.Raster(source + "Band_2") # green
band3 = arcpy.sa.Raster(source + "Band_3") # blue
band4 = arcpy.sa.Raster(source + "Band_4") # NIR
composite = arcpy.CompositeBands_management([band1, band2, band3, band4], source + "KyleField_combined.tif")