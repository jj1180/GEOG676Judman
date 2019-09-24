﻿# coding: utf-8
import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (Judman_676.pyt file)."""
        self.label = "Judman_676"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [BuildingProximity]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Building Proximity"
        self.description = "Determines which buildings on TAMU's campus are near a tergeted building"
        self.canRunInBackground = False
        self.category = "Building Tools"
        
    def getParameterInfo(self):
        """Define parameter definitions"""
         # the first parameter the tool will ask of the user
        param0 = arcpy.Parameter(
           displayName="Building Number",
           name="buildingNumber",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        
        # the second parameter the tool will ask of the user
        param1 = arcpy.Parameter(
            displayName="Buffer radius",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
        )

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True
def execute(self, parameters, messages):
        """The source code of the tool."""
        campus = r"C:/output/GEOG_676_JudmanLab4.gdb"

        # Setup our user input variables
        buildingNumber_input = parameters[0].valueAsText
        bufferSize_input = int(parameters[1].value)

        # Generate our where_clause
        where_clause = "Bldg = '%s'" % buildingNumber_input

        # Check if building exists
        structures = campus + "/Structures"
        cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
        shouldProceed = False

        for row in cursor:
            if row.getValue("Bldg") == buildingNumber_input:
                shouldProceed = True

        # If we shouldProceed do so
        if shouldProceed:
            # Generate the name for our generated buffer layer
            buildingBuff = "/building_%s_buffed_%s" % (buildingNumber_input, bufferSize_input)
            # Get reference to building
            buildingFeature = arcpy.Select_analysis(structures, campus + "/building_%s" % (buildingNumber_input), where_clause)
            # Buffer the selected building
            arcpy.Buffer_analysis(buildingFeature, campus + buildingBuff, bufferSize_input)
            # Clip the structures to our buffered feature
            arcpy.Clip_analysis(structures, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
            # Remove the feature class we just created
            arcpy.Delete_management(campus + "/building_%s" % (buildingNumber_input))
        else:
            print("Seems we couldn't find the building you entered")
        return None