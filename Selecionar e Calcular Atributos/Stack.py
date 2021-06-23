
import arcpy


Aluminio_poly = arcpy.GetParameterAsText(0)
if Aluminio_poly == '#' or not Aluminio_poly:
    Aluminio_poly = "Aluminio_poly" 


arg_poly__2_ = Aluminio_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Alum_nio_c\" >=0 AND \"Alum_nio_c\" <0.2"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Alum_nio_c\" >=0.2 AND \"Alum_nio_c\" <0.5"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Alum_nio_c\" >=0.5 AND \"Alum_nio_c\" <0.6"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Alum_nio_c\" >=0.6 AND \"Alum_nio_c\" <1"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"


arcpy.AddField_management(Aluminio_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


import arcpy


Areia_poly = arcpy.GetParameterAsText(0)
if Areia_poly == '#' or not Areia_poly:
    Areia_poly = "Areia_poly" 


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


arcpy.AddField_management(Areia_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_350)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_350, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v350___400_)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_350___400_, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v400___450_)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_400___450_, "VB", "")

# Process: Selecionar 450 - 500!
arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v450___500_)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_450___500_, "VB", "")

# Process: Selecionar 500 - 550!
arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v500___550)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_500___550, "VB", "")

# Process: Selecionar 550 - 600!
arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v550___600_)


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


import arcpy


Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "Argila_poly" 


arg_poly__2_ = Entrada
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Argila_g_d\" >=100 AND \"Argila_g_d\" <120"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Argila_g_d\" >=120 AND \"Argila_g_d\" <180"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Argila_g_d\" >=180 AND \"Argila_g_d\" <220"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Argila_g_d\" >=220 AND \"Argila_g_d\" <250"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Argila_g_d\" >=250 AND \"Argila_g_d\" <300"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Argila_g_d\" >=300 AND \"Argila_g_d\" <350"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"
arg_poly__14_ = arg_poly__13_
v350_400 = "\"Argila_g_d\" >=350 AND \"Argila_g_d\" <400"
arg_poly__15_ = arg_poly__14_
Identificador_350___400 = "7"
arg_poly__16_ = arg_poly__15_
v400___450 = "\"Argila_g_d\" >=400 AND \"Argila_g_d\" <450"
arg_poly__17_ = arg_poly__16_
Identificador_400_450 = "8"
arg_poly__18_ = arg_poly__17_
v450___500 = "\"Argila_g_d\" >=450 AND \"Argila_g_d\" <500"
arg_poly__19_ = arg_poly__18_
Identificador_450___500 = "9"
Output_Layer_Name__2_ = arg_poly__19_
v500___600 = "\"Argila_g_d\" >=500 AND \"Argila_g_d\" <600"
arg_poly__20_ = Output_Layer_Name__2_
Identificador_500___600 = "10"
arg_poly__21_ = arg_poly__20_
Acima_de_600 = "\"Argila_g_d\" >=600 AND \"Argila_g_d\" <700"
arg_poly__22_ = arg_poly__21_
Identificador_Acima_de_600 = "1"


arcpy.AddField_management(Entrada, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


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

# Process: Selecionar 500 - 600
arcpy.SelectLayerByAttribute_management(arg_poly__19_, "NEW_SELECTION", v500___600)

0
arcpy.CalculateField_management(Output_Layer_Name__2_, "dis", Identificador_500___600, "VB", "")

# Process: Selecionar Acima de 600
arcpy.SelectLayerByAttribute_management(arg_poly__20_, "NEW_SELECTION", Acima_de_600)

1
arcpy.CalculateField_management(arg_poly__21_, "dis", Identificador_Acima_de_600, "VB", "")


import arcpy


Boro_poly = arcpy.GetParameterAsText(0)
if Boro_poly == '#' or not Boro_poly:
    Boro_poly = "Boro_poly" 


arg_poly__2_ = Boro_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Boro_mg_dm\" >=0.10 AND \"Boro_mg_dm\" <0.15"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Boro_mg_dm\" >=0.15 AND \"Boro_mg_dm\" <0.35"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Boro_mg_dm\" >=0.35 AND \"Boro_mg_dm\" <0.60"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Boro_mg_dm\" >=0.60 AND \"Boro_mg_dm\" <0.90"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Boro_mg_dm\" >=0.90 AND \"Boro_mg_dm\" <1"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"


arcpy.AddField_management(Boro_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


import arcpy


Ca___Mg_poly = arcpy.GetParameterAsText(0)
if Ca___Mg_poly == '#' or not Ca___Mg_poly:
    Ca___Mg_poly = "Ca_+_Mg_poly" 


arg_poly__2_ = Ca___Mg_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Ca_Mg_cmol\" >=1.7 AND \"Ca_Mg_cmol\" <4.3"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Ca_Mg_cmol\" >=4.3 AND \"Ca_Mg_cmol\" <4.7"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Ca_Mg_cmol\" >=4.7 AND \"Ca_Mg_cmol\" <5.0"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Ca_Mg_cmol\" >=5.0 AND \"Ca_Mg_cmol\" <5.5"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Ca_Mg_cmol\" >=5.5 AND \"Ca_Mg_cmol\" <7.0"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Ca_Mg_cmol\" >=7.0 AND \"Ca_Mg_cmol\" <16.3"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"


arcpy.AddField_management(Ca___Mg_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


import arcpy


Ca_CTC_poly = arcpy.GetParameterAsText(0)
if Ca_CTC_poly == '#' or not Ca_CTC_poly:
    Ca_CTC_poly = "Ca_CTC_poly" 


arg_poly__2_ = Ca_CTC_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Ca_CTC___\" >=10 AND \"Ca_CTC___\" <15"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Ca_CTC___\" >=15 AND \"Ca_CTC___\" <20"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Ca_CTC___\" >=20 AND \"Ca_CTC___\" <25"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Ca_CTC___\" >=25 AND \"Ca_CTC___\" <30"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Ca_CTC___\" >=30 AND \"Ca_CTC___\" <40"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Ca_CTC___\" >=40 AND \"Ca_CTC___\" <50"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"
arg_poly__14_ = arg_poly__13_
v350_400 = "\"Ca_CTC___\" >=50 AND \"Ca_CTC___\" <60"
arg_poly__15_ = arg_poly__14_
Identificador_350___400 = "7"
arg_poly__16_ = arg_poly__15_
v400___450 = "\"Ca_CTC___\" >=60 AND \"Ca_CTC___\" <70"
arg_poly__17_ = arg_poly__16_
Identificador_400_450 = "8"
arg_poly__18_ = arg_poly__17_
v450___500 = "\"Ca_CTC___\" >=70 AND \"Ca_CTC___\" <80"
arg_poly__19_ = arg_poly__18_
Identificador_450___500 = "9"


arcpy.AddField_management(Ca_CTC_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


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


import arcpy


CaK_poly = arcpy.GetParameterAsText(0)
if CaK_poly == '#' or not CaK_poly:
    CaK_poly = "CaK_poly" 


arg_poly__2_ = CaK_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Ca_K__1__\" >=1 AND \"Ca_K__1__\" <7"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Ca_K__1__\" >=7 AND \"Ca_K__1__\" <9"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Ca_K__1__\" >=9 AND \"Ca_K__1__\" <12"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Ca_K__1__\" >=12 AND \"Ca_K__1__\" <14.9"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Ca_K__1__\" >=14.9 AND \"Ca_K__1__\" <15"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Ca_K__1__\" >=15 AND \"Ca_K__1__\" <16"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"


arcpy.AddField_management(CaK_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


import arcpy


Calcio_poly = arcpy.GetParameterAsText(0)
if Calcio_poly == '#' or not Calcio_poly:
    Calcio_poly = "Calcio_poly" 


arg_poly__2_ = Calcio_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Cblcio_cmo\" >=0.1 AND \"Cblcio_cmo\" <0.4"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Cblcio_cmo\" >=0.4 AND \"Cblcio_cmo\" <1.2"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Cblcio_cmo\" >=1.2 AND \"Cblcio_cmo\" <2.4"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Cblcio_cmo\" >=2.4 AND \"Cblcio_cmo\" <4.0"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Cblcio_cmo\" >=4.0 AND \"Cblcio_cmo\" <5.0"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Cblcio_cmo\" >=5.0 AND \"Cblcio_cmo\" <7.0"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"
arg_poly__14_ = arg_poly__13_
v350_400 = "\"Cblcio_cmo\" >=7.0 AND \"Cblcio_cmo\" <10.0"
arg_poly__15_ = arg_poly__14_
Identificador_350___400 = "7"
arg_poly__16_ = arg_poly__15_
v400___450 = "\"Cblcio_cmo\" >=10.0 AND \"Cblcio_cmo\" <15.0"
arg_poly__17_ = arg_poly__16_
Identificador_400_450 = "8"
arg_poly__18_ = arg_poly__17_
v450___500 = "\"Cblcio_cmo\" >=15.0 AND \"Cblcio_cmo\" <16.0"
arg_poly__19_ = arg_poly__18_
Identificador_450___500 = "9"


arcpy.AddField_management(Calcio_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


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


import arcpy


CaMg_poly = arcpy.GetParameterAsText(0)
if CaMg_poly == '#' or not CaMg_poly:
    CaMg_poly = "CaMg_poly" 


arg_poly__2_ = CaMg_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Ca_Mg__1__\" >=1 AND \"Ca_Mg__1__\" <1.1"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Ca_Mg__1__\" >=1.1 AND \"Ca_Mg__1__\" <2"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Ca_Mg__1__\" >=2 AND \"Ca_Mg__1__\" <3"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Ca_Mg__1__\" >=3 AND \"Ca_Mg__1__\" <4"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Ca_Mg__1__\" >=4 AND \"Ca_Mg__1__\" <5"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Ca_Mg__1__\" >=5 AND \"Ca_Mg__1__\" <6"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"


arcpy.AddField_management(CaMg_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


import arcpy


Carbono_Organico_poly = arcpy.GetParameterAsText(0)
if Carbono_Organico_poly == '#' or not Carbono_Organico_poly:
    Carbono_Organico_poly = "Carbono Organico_poly" 


arg_poly__2_ = Carbono_Organico_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Carbono_Or\" >=4.6 AND \"Carbono_Or\" <7.4"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Carbono_Or\" >=7.4 AND \"Carbono_Or\" <10.1"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Carbono_Or\" >=10.1 AND \"Carbono_Or\" <12.9"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Carbono_Or\" >=12.9 AND \"Carbono_Or\" <15.6"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Carbono_Or\" >=15.6 AND \"Carbono_Or\" <18.4"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Carbono_Or\" >=18.4 AND \"Carbono_Or\" <21.2"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"


arcpy.AddField_management(Carbono_Organico_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


import arcpy


Cobre_poly = arcpy.GetParameterAsText(0)
if Cobre_poly == '#' or not Cobre_poly:
    Cobre_poly = "Cobre_poly" 


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


arcpy.AddField_management(Cobre_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


import arcpy


CTC_Total_poly = arcpy.GetParameterAsText(0)
if CTC_Total_poly == '#' or not CTC_Total_poly:
    CTC_Total_poly = "CTC_Total_poly" 


arg_poly__2_ = CTC_Total_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"CTC_Total_\" >=1.00 AND \"CTC_Total_\" <1.60"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"CTC_Total_\" >=1.60 AND \"CTC_Total_\" <4.50"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"CTC_Total_\" >=4.50 AND \"CTC_Total_\" <8.50"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"CTC_Total_\" >=8.50 AND \"CTC_Total_\" <10.00"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"CTC_Total_\" >=10.00 AND \"CTC_Total_\" <15.00"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"CTC_Total_\" >=15.00 AND \"CTC_Total_\" <16.00"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"


arcpy.AddField_management(CTC_Total_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


import arcpy


Enxofre_poly = arcpy.GetParameterAsText(0)
if Enxofre_poly == '#' or not Enxofre_poly:
    Enxofre_poly = "Enxofre_poly" 


arg_poly__2_ = Enxofre_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Enxofre_mg\" >=1 AND \"Enxofre_mg\" <2.5"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Enxofre_mg\" >=2.5 AND \"Enxofre_mg\" <4.9"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Enxofre_mg\" >=4.9 AND \"Enxofre_mg\" <9.0"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Enxofre_mg\" >=9.0 AND \"Enxofre_mg\" <10.0"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Enxofre_mg\" >=10.0 AND \"Enxofre_mg\" <18.0"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"


arcpy.AddField_management(Enxofre_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


import arcpy


Ferro_poly = arcpy.GetParameterAsText(0)
if Ferro_poly == '#' or not Ferro_poly:
    Ferro_poly = "Ferro_poly" 


arg_poly__2_ = Ferro_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Ferro_mg_d\" >=1 AND \"Ferro_mg_d\" <20"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Ferro_mg_d\" >=20 AND \"Ferro_mg_d\" <31"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Ferro_mg_d\" >=31 AND \"Ferro_mg_d\" <200"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Ferro_mg_d\" >=200 AND \"Ferro_mg_d\" <220"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Ferro_mg_d\" >=220 AND \"Ferro_mg_d\" <225"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"


arcpy.AddField_management(Ferro_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


import arcpy


Fosforo_Mehlich_poly = arcpy.GetParameterAsText(0)
if Fosforo_Mehlich_poly == '#' or not Fosforo_Mehlich_poly:
    Fosforo_Mehlich_poly = "Fosforo_Mehlich_poly" 


arg_poly__2_ = Fosforo_Mehlich_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Fbsforo___\" >=0 AND \"Fbsforo___\" <5"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Fbsforo___\" >=5 AND \"Fbsforo___\" <10"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Fbsforo___\" >=10 AND \"Fbsforo___\" <14"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v180___220__2_ = "\"Fbsforo___\" >=14 AND \"Fbsforo___\" <16"
arg_poly__9_ = arg_poly__7_
Identificador_180__220__2_ = "4"


arcpy.AddField_management(Fosforo_Mehlich_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v180___220__2_)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_180__220__2_, "VB", "")


import arcpy


H__AL_poly = arcpy.GetParameterAsText(0)
if H__AL_poly == '#' or not H__AL_poly:
    H__AL_poly = "H_+AL_poly" 


arg_poly__2_ = H__AL_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"H_Al_cmol_\" >=1 AND \"H_Al_cmol_\" <2"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"H_Al_cmol_\" >=2 AND \"H_Al_cmol_\" <3"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"H_Al_cmol_\" >=3 AND \"H_Al_cmol_\" <4"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"H_Al_cmol_\" >=4 AND \"H_Al_cmol_\" <5"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"H_Al_cmol_\" >=5 AND \"H_Al_cmol_\" <6"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"H_Al_cmol_\" >=6 AND \"H_Al_cmol_\" <7"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"


arcpy.AddField_management(H__AL_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


import arcpy


H_AL_CTC_poly = arcpy.GetParameterAsText(0)
if H_AL_CTC_poly == '#' or not H_AL_CTC_poly:
    H_AL_CTC_poly = "H+AL_CTC_poly" 


arg_poly__2_ = H_AL_CTC_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"H_Al_CTC__\" >=6 AND \"H_Al_CTC__\" <25"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"H_Al_CTC__\" >=25 AND \"H_Al_CTC__\" <33"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"H_Al_CTC__\" >=33 AND \"H_Al_CTC__\" <36"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"H_Al_CTC__\" >=36 AND \"H_Al_CTC__\" <40"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"H_Al_CTC__\" >=40 AND \"H_Al_CTC__\" <60"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"H_Al_CTC__\" >=60 AND \"H_Al_CTC__\" <70"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"


arcpy.AddField_management(H_AL_CTC_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


import arcpy


Potassio_CTC_poly = arcpy.GetParameterAsText(0)
if Potassio_CTC_poly == '#' or not Potassio_CTC_poly:
    Potassio_CTC_poly = "Potassio_CTC_poly" 


arg_poly__2_ = Potassio_CTC_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"K_CTC___\" >=0 AND \"K_CTC___\" <1"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"K_CTC___\" >=1 AND \"K_CTC___\" <2"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"K_CTC___\" >=2 AND \"K_CTC___\" <3"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"K_CTC___\" >=3 AND \"K_CTC___\" <5"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"K_CTC___\" >=5 AND \"K_CTC___\" <6"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"K_CTC___\" >=6 AND \"K_CTC___\" <7"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"


arcpy.AddField_management(Potassio_CTC_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


import arcpy


Identificador_180__220 = arcpy.GetParameterAsText(0)
if Identificador_180__220 == '#' or not Identificador_180__220:
    Identificador_180__220 = "3" 

Magnesio_poly = arcpy.GetParameterAsText(1)
if Magnesio_poly == '#' or not Magnesio_poly:
    Magnesio_poly = "Magnesio_poly" 


arg_poly__2_ = Magnesio_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Magn_sio_c\" >=0.10 AND \"Magn_sio_c\" <0.50"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Magn_sio_c\" >=0.50 AND \"Magn_sio_c\" <0.90"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Magn_sio_c\" >=0.90 AND \"Magn_sio_c\" <1.00"
arg_poly__8_ = arg_poly__3_
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Magn_sio_c\" >=1.00 AND \"Magn_sio_c\" <3.00"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"


arcpy.AddField_management(Magnesio_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


import arcpy


Manganes_poly = arcpy.GetParameterAsText(0)
if Manganes_poly == '#' or not Manganes_poly:
    Manganes_poly = "Manganes_poly" 


arg_poly__2_ = Manganes_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Mangands_m\" >=5 AND \"Mangands_m\" <6"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Mangands_m\" >=6 AND \"Mangands_m\" <12"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Mangands_m\" >=12 AND \"Mangands_m\" <130"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Mangands_m\" >=130 AND \"Mangands_m\" <131"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"


arcpy.AddField_management(Manganes_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


import arcpy



Materia_Organica_poly = "Materia_Organica_poly"
arg_poly__2_ = Materia_Organica_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Mat_ria_Or\" >=10 AND \"Mat_ria_Or\" <17"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Mat_ria_Or\" >=17 AND \"Mat_ria_Or\" <20"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Mat_ria_Or\" >=20 AND \"Mat_ria_Or\" <22"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Mat_ria_Or\" >=22 AND \"Mat_ria_Or\" <25"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Mat_ria_Or\" >=25 AND \"Mat_ria_Or\" <28"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Mat_ria_Or\" >=28 AND \"Mat_ria_Or\" <33"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"
arg_poly__14_ = arg_poly__13_
v350_400 = "\"Mat_ria_Or\" >=33 AND \"Mat_ria_Or\" <35"
arg_poly__15_ = arg_poly__14_
Identificador_350___400 = "7"
arg_poly__16_ = arg_poly__15_
v400___450 = "\"Mat_ria_Or\" >=35 AND \"Mat_ria_Or\" <38"
arg_poly__17_ = arg_poly__16_
Identificador_400_450 = "8"
arg_poly__18_ = arg_poly__17_
v450___500 = "\"Mat_ria_Or\" >=38 AND \"Mat_ria_Or\" <43"
arg_poly__19_ = arg_poly__18_
Identificador_450___500 = "9"


arcpy.AddField_management(Materia_Organica_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__13_, "NEW_SELECTION", v350_400)


arcpy.CalculateField_management(arg_poly__14_, "dis", Identificador_350___400, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__15_, "NEW_SELECTION", v400___450)


arcpy.CalculateField_management(arg_poly__16_, "dis", Identificador_400_450, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__17_, "NEW_SELECTION", v450___500)


arcpy.CalculateField_management(arg_poly__18_, "dis", Identificador_450___500, "VB", "")


import arcpy


Magnesio_CTC_poly = arcpy.GetParameterAsText(0)
if Magnesio_CTC_poly == '#' or not Magnesio_CTC_poly:
    Magnesio_CTC_poly = "Magnesio_CTC_poly" 


arg_poly__2_ = Magnesio_CTC_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Mg_CTC___\" >=5 AND \"Mg_CTC___\" <7"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Mg_CTC___\" >=7 AND \"Mg_CTC___\" <10"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Mg_CTC___\" >=10 AND \"Mg_CTC___\" <15"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Mg_CTC___\" >=15 AND \"Mg_CTC___\" <20"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Mg_CTC___\" >=20 AND \"Mg_CTC___\" <21"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"


arcpy.AddField_management(Magnesio_CTC_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


import arcpy


MgK_poly = arcpy.GetParameterAsText(0)
if MgK_poly == '#' or not MgK_poly:
    MgK_poly = "MgK_poly" 


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


arcpy.AddField_management(MgK_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__13_, "NEW_SELECTION", v350_400)


arcpy.CalculateField_management(arg_poly__14_, "dis", Identificador_350___400, "VB", "")


import arcpy


pH_CaCl_poly = arcpy.GetParameterAsText(0)
if pH_CaCl_poly == '#' or not pH_CaCl_poly:
    pH_CaCl_poly = "pH_CaCl_poly" 


arg_poly__2_ = pH_CaCl_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"pH_CaCl2__\" >=4.00 AND \"pH_CaCl2__\" <4.50"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"pH_CaCl2__\" >=4.50 AND \"pH_CaCl2__\" <5.00"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"pH_CaCl2__\" >=5.00 AND \"pH_CaCl2__\" <5.40"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"pH_CaCl2__\" >=5.40 AND \"pH_CaCl2__\" <6.00"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"pH_CaCl2__\" >=6.00 AND \"pH_CaCl2__\" <6.40"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"pH_CaCl2__\" >=6.40 AND \"pH_CaCl2__\" <7.40"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"


arcpy.AddField_management(pH_CaCl_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


import arcpy


Potassio_poly = arcpy.GetParameterAsText(0)
if Potassio_poly == '#' or not Potassio_poly:
    Potassio_poly = "Potassio_poly" 


arg_poly__2_ = Potassio_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Pot_ssio_c\" >=0.03 AND \"Pot_ssio_c\" <0.13"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Pot_ssio_c\" >=0.13 AND \"Pot_ssio_c\" <0.14"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Pot_ssio_c\" >=0.14 AND \"Pot_ssio_c\" <0.17"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Pot_ssio_c\" >=0.17 AND \"Pot_ssio_c\" <0.21"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Pot_ssio_c\" >=0.21 AND \"Pot_ssio_c\" <0.24"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Pot_ssio_c\" >=0.24 AND \"Pot_ssio_c\" <0.28"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"
arg_poly__14_ = arg_poly__13_
v350_400 = "\"Pot_ssio_c\" >=0.28 AND \"Pot_ssio_c\" <0.44"
arg_poly__15_ = arg_poly__14_
Identificador_350___400 = "7"


arcpy.AddField_management(Potassio_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__13_, "NEW_SELECTION", v350_400)


arcpy.CalculateField_management(arg_poly__14_, "dis", Identificador_350___400, "VB", "")


import arcpy


Potassio_ppm_poly = arcpy.GetParameterAsText(0)
if Potassio_ppm_poly == '#' or not Potassio_ppm_poly:
    Potassio_ppm_poly = "Potassio_ppm_poly" 


arg_poly__2_ = Potassio_ppm_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Pot_ssio_p\" >=10 AND \"Pot_ssio_p\" <26"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Pot_ssio_p\" >=26 AND \"Pot_ssio_p\" <51"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Pot_ssio_p\" >=51 AND \"Pot_ssio_p\" <81"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Pot_ssio_p\" >=81 AND \"Pot_ssio_p\" <85"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Pot_ssio_p\" >=85 AND \"Pot_ssio_p\" <100"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Pot_ssio_p\" >=100 AND \"Pot_ssio_p\" <150"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"
arg_poly__14_ = arg_poly__13_
v350_400 = "\"Pot_ssio_p\" >=150 AND \"Pot_ssio_p\" <180"
arg_poly__15_ = arg_poly__14_
Identificador_350___400 = "7"
arg_poly__16_ = arg_poly__15_
v400___450 = "\"Pot_ssio_p\" >=180 AND \"Pot_ssio_p\" <200"
arg_poly__17_ = arg_poly__16_
Identificador_400_450 = "8"


arcpy.AddField_management(Potassio_ppm_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__13_, "NEW_SELECTION", v350_400)


arcpy.CalculateField_management(arg_poly__14_, "dis", Identificador_350___400, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__15_, "NEW_SELECTION", v400___450)


arcpy.CalculateField_management(arg_poly__16_, "dis", Identificador_400_450, "VB", "")


import arcpy


Satturacao_de_Bases_poly = arcpy.GetParameterAsText(0)
if Satturacao_de_Bases_poly == '#' or not Satturacao_de_Bases_poly:
    Satturacao_de_Bases_poly = "Satturacao_de_Bases_poly" 


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


arcpy.AddField_management(Satturacao_de_Bases_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__13_, "NEW_SELECTION", v350_400)


arcpy.CalculateField_management(arg_poly__14_, "dis", Identificador_350___400, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__15_, "NEW_SELECTION", v400___450)


arcpy.CalculateField_management(arg_poly__16_, "dis", Identificador_400_450, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__17_, "NEW_SELECTION", v450___500)


arcpy.CalculateField_management(arg_poly__18_, "dis", Identificador_450___500, "VB", "")


import arcpy


Saturacao_por_Aluminio_poly = arcpy.GetParameterAsText(0)
if Saturacao_por_Aluminio_poly == '#' or not Saturacao_por_Aluminio_poly:
    Saturacao_por_Aluminio_poly = "Saturacao_por_Aluminio_poly" 


arg_poly__2_ = Saturacao_por_Aluminio_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Saturad\" >=1 AND \"Saturad\" <2"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Saturad\" >=2 AND \"Saturad\" <4"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Saturad\" >=4 AND \"Saturad\" <6"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Saturad\" >=6 AND \"Saturad\" <8"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"


arcpy.AddField_management(Saturacao_por_Aluminio_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


import arcpy



Silte_poly = "Silte_poly"
arg_poly__2_ = Silte_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Silte_g_dm\" >=25 AND \"Silte_g_dm\" <50"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Silte_g_dm\" >=50 AND \"Silte_g_dm\" <100"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Silte_g_dm\" >=100 AND \"Silte_g_dm\" <150"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Silte_g_dm\" >=150 AND \"Silte_g_dm\" <200"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Silte_g_dm\" >=200 AND \"Silte_g_dm\" <250"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Silte_g_dm\" >=250 AND \"Silte_g_dm\" <300"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"


arcpy.AddField_management(Silte_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


import arcpy


Sodio_poly = arcpy.GetParameterAsText(0)
if Sodio_poly == '#' or not Sodio_poly:
    Sodio_poly = "Sodio_poly" 


arg_poly__2_ = Sodio_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Sbdio_mg_d\" >=0 AND \"Sbdio_mg_d\" <1.91"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Sbdio_mg_d\" >=1.91 AND \"Sbdio_mg_d\" <2.22"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Sbdio_mg_d\" >=2.22 AND \"Sbdio_mg_d\" <2.55"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Sbdio_mg_d\" >=2.55 AND \"Sbdio_mg_d\" <2.95"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"
arg_poly__10_ = arg_poly__9_
v250___300 = "\"Sbdio_mg_d\" >=2.95 AND \"Sbdio_mg_d\" <4.40"
arg_poly__11_ = arg_poly__10_
Identificador_250___300 = "5"
arg_poly__12_ = arg_poly__11_
v300___350 = "\"Sbdio_mg_d\" >=4.40 AND \"Sbdio_mg_d\" <6"
arg_poly__13_ = arg_poly__12_
Identificador_300___350 = "6"
arg_poly__14_ = arg_poly__13_
v350_400 = "\"Sbdio_mg_d\" >=6 AND \"Sbdio_mg_d\" <20"
arg_poly__15_ = arg_poly__14_
Identificador_350___400 = "7"


arcpy.AddField_management(Sodio_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__9_, "NEW_SELECTION", v250___300)


arcpy.CalculateField_management(arg_poly__10_, "dis", Identificador_250___300, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__11_, "NEW_SELECTION", v300___350)


arcpy.CalculateField_management(arg_poly__12_, "dis", Identificador_300___350, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__13_, "NEW_SELECTION", v350_400)


arcpy.CalculateField_management(arg_poly__14_, "dis", Identificador_350___400, "VB", "")




import arcpy


Zinco_poly = arcpy.GetParameterAsText(0)
if Zinco_poly == '#' or not Zinco_poly:
    Zinco_poly = "Zinco_poly" 


arg_poly__2_ = Zinco_poly
arg_poly__4_ = arg_poly__2_
Abaixo_de_120 = "\"Zinco_mg_d\" >=0.5 AND \"Zinco_mg_d\" <1"
arg_poly__5_ = arg_poly__4_
Identificador_Abaixo_de_120 = "1"
arg_poly = arg_poly__5_
v120___180 = "\"Zinco_mg_d\" >=1 AND \"Zinco_mg_d\" <1.6"
arg_poly__6_ = arg_poly
Identificador_120___180 = "2"
arg_poly__3_ = arg_poly__6_
v180___220 = "\"Zinco_mg_d\" >=1.6 AND \"Zinco_mg_d\" <5"
arg_poly__8_ = arg_poly__3_
Identificador_180__220 = "3"
arg_poly__7_ = arg_poly__8_
v220___250 = "\"Zinco_mg_d\" >=5 AND \"Zinco_mg_d\" <7"
arg_poly__9_ = arg_poly__7_
Identificador_220___250 = "4"


arcpy.AddField_management(Zinco_poly, "dis", "SHORT", "2", "", "2", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.SelectLayerByAttribute_management(arg_poly__2_, "NEW_SELECTION", Abaixo_de_120)


arcpy.CalculateField_management(arg_poly__4_, "dis", Identificador_Abaixo_de_120, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__5_, "NEW_SELECTION", v120___180)


arcpy.CalculateField_management(arg_poly, "dis", Identificador_120___180, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__6_, "NEW_SELECTION", v180___220)


arcpy.CalculateField_management(arg_poly__3_, "dis", Identificador_180__220, "VB", "")


arcpy.SelectLayerByAttribute_management(arg_poly__8_, "NEW_SELECTION", v220___250)


arcpy.CalculateField_management(arg_poly__7_, "dis", Identificador_220___250, "VB", "")

