# coding: utf-8
import arcpy
p = arcpy.mp.ArcGISProject("CURRENT")
m = p.listMaps('Map')[0]
l = m.listLayers('GarageParking*')[0]
sym = l.symbology
sym.updateRenderer('GraduatedColorsRenderer')
sym.renderer.classificationField = "Shape_Area"
sym.renderer.breakCount = 10
sym.renderer.colorRamp = p.listColorRamps('Cyan to Purple')[0]
l.symbology = sym
def __init__(self):
    """Define the tool (Graduated_Color)."""
    self.label = "Graduated Color"
    self.description = "Determines area of buildings"
    self.canRunInBackground = False # Only used in ArcMap
    self.category = "Building Tools"
class Toolbox(object):
    def __init__(self):
        """Define the toolbox (Graduated_Color.pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (Shape_Area)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return
def execute(self, parameters, messages):
        """The source code of the tool."""
        # Define our progressor variables
        readTime = 2.5
        start = 0
        maximum = 100
        step = 25

        # Setup the progressor
        arcpy.SetProgressor("step", "Checking building area...", start, maximum, step)
        time.sleep(readTime)
        # Add message to the results pane
        arcpy.AddMessage("Checking building area...")

        campus = r"C:/output/Homework6_Judman.gdb"
        
        # Setup our user input variables
        buildingNumber_input = parameters[0].valueAsText
        bufferSize_input = int(parameters[1].value)

        # Generate our where_clause
        where_clause = "Bldg = '%s'" % buildingNumber_input

        # Check if building exists
        structures = campus + "/Structures"
        cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
        shouldProceed = False

        # Increment the progressor and change the label; add message to the results pane
        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Validating building area once more...")
        time.sleep(readTime)
        arcpy.AddMessage("Validating building area once more...")

        for row in cursor:
            if row.getValue("Bldg") == buildingNumber_input:
                shouldProceed = True
        else:
            print("Seems we couldn't find the building you entered")
        return None