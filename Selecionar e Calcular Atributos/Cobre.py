# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Cobre.py
# Created on: 2021-06-22 16:49:34.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: Cobre <Cobre_poly> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Cobre_poly = arcpy.GetParameterAsText(0)
if Cobre_poly == '#' or not Cobre_poly:
    Cobre_poly = "Cobre_poly" # provide a default value if unspecified

# Local variables:
arg_poly__2_ = Cobre_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Cobre_mg_d\" >=0.30 AND \"Cobre_mg_d\" <0.60"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Cobre_mg_d\" >=0.60 AND \"Cobre_mg_d\" <1.5"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Cobre_mg_d\" >=1.5 AND \"Cobre_mg_d\" <3"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Cobre_mg_d\" >=3 AND \"Cobre_mg_d\" <10"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"

# Process: Adicionar campo dis
arcpy.AddField_management(Cobre_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Selecionar Abaixo de 120
arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)

# Process: Identificador 1
arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")

# Process: Selecionar 120 - 180
arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)

# Process: Identificador 2
arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")

# Process: Selecionar 180 - 220
arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)

# Process: Identificador 3
arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")

# Process: Selecionar 220 - 250
arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)

# Process: Identificador 4
arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")

