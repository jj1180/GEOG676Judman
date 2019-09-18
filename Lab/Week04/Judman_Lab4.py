# coding: utf-8
import arcpy
open("c:\garages.csv", "r")
# <_io.TextIOWrapper name='c:\\garages.csv' mode='r' encoding='cp1252'>
# Name: CreateFileGDB_Example2.py
# Description: Create a file GDB
# Import system modules
import arcpy
# Set local variables
out_folder_path = "C:/output"
out_name = "GEOG_676_JudmanLab4.gdb"
# Execute CreateFileGDB
arcpy.CreateFileGDB_management(out_folder_path, out_name)
# <Result 'C:/output\\GEOG_676_JudmanLab4.gdb'>
import arcpy
arcpy.env.workspace = "C:/output"
arcpy.CreateFileGDB_management(arcpy.env.workspace, "GEOG_676_JudmanLab4.gdb")
# <Result 'C:/output\\GEOG_676_JudmanLab4.gdb'>
garages = arcpy.management.MakeXYEventLayer("coordinates.csv", "x", "y", "coordinates")
import arcpy
input_layers = ["structures", "garages_coordinates"]
arcpy.FeatureClassToGeodatabase_conversion(input_layers, r"C:/output/GEOG_676_JudmanLab4.gdb")
# <Result 'C:\\output\\GEOG_676_JudmanLab4.gdb'>
distance = 100
arcpy.Buffer_analysis('garages_coordinates', 'Garages_Buffer', str(100) + " meters")
arcpy.Intersect_analysis([dcGdb + "/Garages_Buffer", dcGdb + "/Structures"], dcGdb + "/intersection", "ALL")
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\analysis.py", line 442, in Intersect
#     raise e
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\analysis.py", line 439, in Intersect
#     retval = convertArcObjectToPythonObject(gp.Intersect_analysis(*gp_fixargs((in_features, out_feature_class, join_attributes, cluster_tolerance, output_type), True)))
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\geoprocessing\_base.py", line 506, in <lambda>
#     return lambda *args: val(*gp_fixargs(args, True))
# arcgisscripting.ExecuteError: Failed to execute. Parameters are not valid.
# ERROR 000732: Input Features: Dataset C:/output/JudmanLab4.gdb/Garages_Buffer does not exist or is not supported
# Failed to execute (Intersect).
# 
dcGdb = r"C:/output/GEOG_676_JudmanLab4.gdb"
arcpy.Intersect_analysis([dcGdb + "/Garages_Buffer", dcGdb + "/Structures"], dcGdb + "/intersection", "ALL")
# <Result 'C:\\output\\GEOG_676_JudmanLab4.gdb\\intersection'>
arcpy.TableToTable_conversion(dcGdb + "/intersection.dbf", "C:/output", "intersection.csv")
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\conversion.py", line 1975, in TableToTable
#     raise e
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\conversion.py", line 1972, in TableToTable
#     retval = convertArcObjectToPythonObject(gp.TableToTable_conversion(*gp_fixargs((in_rows, out_path, out_name, where_clause, field_mapping, config_keyword), True)))
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\geoprocessing\_base.py", line 506, in <lambda>
#     return lambda *args: val(*gp_fixargs(args, True))
# arcgisscripting.ExecuteError: ERROR 001156: Failed on input OID 1, could not write value ' ' to output field Number
# Failed to execute (TableToTable).
# 
dcGdb = r"C:/output/GEOG_676_JudmanLab4.gdb"
arcpy.TableToTable_conversion(dcGdb + "/intersection.dbf", "C:/output", "intersection.csv")
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\conversion.py", line 1975, in TableToTable
#     raise e
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\conversion.py", line 1972, in TableToTable
#     retval = convertArcObjectToPythonObject(gp.TableToTable_conversion(*gp_fixargs((in_rows, out_path, out_name, where_clause, field_mapping, config_keyword), True)))
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\geoprocessing\_base.py", line 506, in <lambda>
#     return lambda *args: val(*gp_fixargs(args, True))
# arcgisscripting.ExecuteError: ERROR 999999: Something unexpected caused the tool to fail. Contact Esri Technical Support (http://esriurl.com/support) to Report a Bug, and refer to the error help for potential solutions or workarounds.
# Failed to execute (TableToTable).
# 
dcGdb = r"C:/output/GEOG_676_JudmanLab4.gdb"
arcpy.TableToTable_conversion(dcGdb + "/intersection.dbf", "C:/output", "intersection.csv")
# Traceback (most recent call last):
#   File "<string>", line 2, in <module>
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\conversion.py", line 1975, in TableToTable
#     raise e
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\conversion.py", line 1972, in TableToTable
#     retval = convertArcObjectToPythonObject(gp.TableToTable_conversion(*gp_fixargs((in_rows, out_path, out_name, where_clause, field_mapping, config_keyword), True)))
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\geoprocessing\_base.py", line 506, in <lambda>
#     return lambda *args: val(*gp_fixargs(args, True))
# arcgisscripting.ExecuteError: ERROR 999999: Something unexpected caused the tool to fail. Contact Esri Technical Support (http://esriurl.com/support) to Report a Bug, and refer to the error help for potential solutions or workarounds.
# Failed to execute (TableToTable).
# 
arcpy.TableToTable_conversion(dcGdb + "/intersection.dbf", "C:/outputlab4", "intersection.csv")
# <Result 'C:/outputlab4\\intersection.csv'>