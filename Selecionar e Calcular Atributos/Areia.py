# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Areia.py
# Created on: 2021-06-22 16:26:08.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: Areia <Areia_poly> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Areia_poly = arcpy.GetParameterAsText(0)
if Areia_poly == '#' or not Areia_poly:
    Areia_poly = "Areia_poly" # provide a default value if unspecified

# Local variables:
arg_poly__2_ = Areia_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_350 = "\"Areia_g_dm\"  >=300 AND\"Areia_g_dm\"<350"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_350 = "1"
arg_poly = arg_poly__5_
v350___400_ = "\"Areia_g_dm\"  >=350 AND\"Areia_g_dm\"<400"
arg_poly__6_ = arg_poly
Identificador_350___400_ = "2"
arg_poly__3_ = arg_poly__6_
v400___450_ = "\"Areia_g_dm\"  >=400 AND\"Areia_g_dm\"<450"
arg_poly__8_ = arg_poly__3_
Identificador_400___450_ = "3"
arg_poly__7_ = arg_poly__8_
v450___500_ = "\"Areia_g_dm\"  >=450 AND\"Areia_g_dm\"<500"
arg_poly__9_ = arg_poly__7_
Identificador_450___500_ = "4"
arg_poly__10_ = arg_poly__9_
v500___550 = "\"Areia_g_dm\"  >=500 AND\"Areia_g_dm\"<550"
arg_poly__11_ = arg_poly__10_
Identificador_500___550 = "5"
arg_poly__12_ = arg_poly__11_
v550___600_ = "\"Areia_g_dm\"  >=550 AND\"Areia_g_dm\"<600"
arg_poly__13_ = arg_poly__12_
Identificador_550___600 = "6"
arg_poly__14_ = arg_poly__13_
v600___700_ = "\"Areia_g_dm\"  >=600 AND\"Areia_g_dm\"<700"
arg_poly__15_ = arg_poly__14_
Identificador_600___700 = "7"
arg_poly__16_ = arg_poly__15_
v400___450 = "\"Areia_g_dm\"  >=700 AND\"Areia_g_dm\"<800"
arg_poly__17_ = arg_poly__16_
Identificador_400_450 = "8"
arg_poly__18_ = arg_poly__17_
v450___500 = "\"Areia_g_dm\"  >=800 AND\"Areia_g_dm\"<900"
arg_poly__19_ = arg_poly__18_
Identificador_450___500 = "9"

# Process: Adicionar campo dis
arcpy.AddField_management(Areia_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Selecionar Abaixo de 350
arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_350)

# Process: Identificador 1
arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_350, "VB", "")

# Process: Selecionar 350 - 400!
arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v350___400_)

# Process: Identificador 2
arcpy.CalculateField_management(arg_poly, "dis", Identificador_350___400_, "VB", "")

# Process: Selecionar 400 - 450!
arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v400___450_)

# Process: Identificador 3
arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_400___450_, "VB", "")

# Process: Selecionar 450 - 500!
arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v450___500_)

# Process: Identificador 4
arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_450___500_, "VB", "")

# Process: Selecionar 500 - 550!
arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v500___550)

# Process: Identificador 5
arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_500___550, "VB", "")

# Process: Selecionar 550 - 600!
arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v550___600_)

# Process: Identificador 6
arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_550___600, "VB", "")

# Process: Selecionar 600 - 700!
arcpy.SelectLayerByAttribute_management(arg_poly__13_, "NEW_SELECTION", v600___700_)

# Process: Identificador 7
arcpy.CalculateField_management(arg_poly__14_, "dis", Identificador_600___700, "VB", "")

# Process: Selecionar 400 - 450
arcpy.SelectLayerByAttribute_management(arg_poly__15_, "NEW_SELECTION", v400___450)

# Process: Identificador 8
arcpy.CalculateField_management(arg_poly__16_, "dis", Identificador_400_450, "VB", "")

# Process: Selecionar 450 - 500
arcpy.SelectLayerByAttribute_management(arg_poly__17_, "NEW_SELECTION", v450___500)

# Process: Identificador 9
arcpy.CalculateField_management(arg_poly__18_, "dis", Identificador_450___500, "VB", "")

