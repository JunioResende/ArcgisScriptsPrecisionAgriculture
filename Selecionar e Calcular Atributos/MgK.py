# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# MgK.py
# Created on: 2021-06-22 16:49:03.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: MgK <MgK_poly> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
MgK_poly = arcpy.GetParameterAsText(0)
if MgK_poly == '#' or not MgK_poly:
    MgK_poly = "MgK_poly" # provide a default value if unspecified

# Local variables:
arg_poly__2_ = MgK_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Mg_K__1__\" >=0.5 AND \"Mg_K__1__\" <1"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Mg_K__1__\" >=1 AND \"Mg_K__1__\" <2"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Mg_K__1__\" >=2 AND \"Mg_K__1__\" <3"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Mg_K__1__\" >=3 AND \"Mg_K__1__\" <4.9"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Mg_K__1__\" >=4.9 AND \"Mg_K__1__\" <5"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Mg_K__1__\" >=5 AND \"Mg_K__1__\" <6"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"
arg_poly__14_ = arg_poly__13_
v350_400 = "\"Mg_K__1__\" >=6 AND \"Mg_K__1__\" <7"
arg_poly__15_ = arg_poly__14_
Identificador_350___400 = "7"

# Process: Adicionar campo dis
arcpy.AddField_management(MgK_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")

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

# Process: Selecionar 250 - 300
arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)

# Process: Identificador 5
arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")

# Process: Selecionar 300 - 350
arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)

# Process: Identificador 6
arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")

# Process: Selecionar 350 - 400
arcpy.SelectLayerByAttribute_management(arg_poly__13_, "NEW_SELECTION", v350_400)

# Process: Identificador 7
arcpy.CalculateField_management(arg_poly__14_, "dis", Identificador_350___400, "VB", "")

