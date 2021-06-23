# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# SaturacaoDeBases.py
# Created on: 2021-06-22 16:30:53.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: SaturacaoDeBases <Satturacao_de_Bases_poly> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Satturacao_de_Bases_poly = arcpy.GetParameterAsText(0)
if Satturacao_de_Bases_poly == '#' or not Satturacao_de_Bases_poly:
    Satturacao_de_Bases_poly = "Satturacao_de_Bases_poly" # provide a default value if unspecified

# Local variables:
arg_poly__2_ = Satturacao_de_Bases_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Saturad\" >=20 AND \"Saturad\" <25"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Saturad\" >=25 AND \"Saturad\" <30"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Saturad\" >=30 AND \"Saturad\" <35"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Saturad\" >=35 AND \"Saturad\" <40"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Saturad\" >=40 AND \"Saturad\" <45"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Saturad\" >=45 AND \"Saturad\" <50"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"
arg_poly__14_ = arg_poly__13_
v350_400 = "\"Saturad\" >=50 AND \"Saturad\" <55"
arg_poly__15_ = arg_poly__14_
Identificador_350___400 = "7"
arg_poly__16_ = arg_poly__15_
v400___450 = "\"Saturad\" >=55 AND \"Saturad\" <60"
arg_poly__17_ = arg_poly__16_
Identificador_400_450 = "8"
arg_poly__18_ = arg_poly__17_
v450___500 = "\"Saturad\" >=60 AND \"Saturad\" <70"
arg_poly__19_ = arg_poly__18_
Identificador_450___500 = "9"

# Process: Adicionar campo dis
arcpy.AddField_management(Satturacao_de_Bases_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")

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

# Process: Selecionar 400 - 450
arcpy.SelectLayerByAttribute_management(arg_poly__15_, "NEW_SELECTION", v400___450)

# Process: Identificador 8
arcpy.CalculateField_management(arg_poly__16_, "dis", Identificador_400_450, "VB", "")

# Process: Selecionar 450 - 500
arcpy.SelectLayerByAttribute_management(arg_poly__17_, "NEW_SELECTION", v450___500)

# Process: Identificador 9
arcpy.CalculateField_management(arg_poly__18_, "dis", Identificador_450___500, "VB", "")
