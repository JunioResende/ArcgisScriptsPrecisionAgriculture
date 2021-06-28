#Aluminio
import arcpy

Aluminio_poly = "Aluminio_poly"
Aluminio_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Aluminio.shp"
Aluminio_poly_Dissolve__2_ = Aluminio_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_

arcpy.Dissolve_management(Aluminio_poly, Aluminio_shp, "dis", "Alum_nio_c MEAN", "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Aluminio_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Areia
import arcpy

Areia_poly = "Areia_poly"
Areia_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Areia.shp"
Aluminio_poly_Dissolve__2_ = Areia_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_

arcpy.Dissolve_management(Areia_poly, Areia_shp, "dis", "Areia_g_dm MEAN", "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Areia_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Argila
import arcpy

Argila_poly = "Argila_poly"
Argila_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Argila.shp"
Aluminio_poly_Dissolve__2_ = Argila_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_

arcpy.Dissolve_management(Argila_poly, Argila_shp, "dis", "Argila_g_d MEAN", "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Argila_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Boro
import arcpy

Boro_poly = "Boro_poly"
Boro_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Boro.shp"
Aluminio_poly_Dissolve__2_ = Boro_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_

arcpy.Dissolve_management(Boro_poly, Boro_shp, "dis", "Boro_mg_dm MEAN", "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Boro_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Ca_+_Mg
import arcpy

Ca___Mg_poly = "Ca_+_Mg_poly"
Ca___Mg_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\CaMaisMg.shp"
Aluminio_poly_Dissolve__2_ = Ca___Mg_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_

arcpy.Dissolve_management(Ca___Mg_poly, Ca___Mg_shp, "dis", "Ca_Mg_cmol MEAN", "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Ca___Mg_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Ca_CTC
import arcpy

Ca_CTC_poly = "Ca_CTC_poly"
Ca_CTC_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\CaCTC.shp"
Aluminio_poly_Dissolve__2_ = Ca_CTC_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_

arcpy.Dissolve_management(Ca_CTC_poly, Ca_CTC_shp, "dis", "Ca_CTC___ MEAN", "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Ca_CTC_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#CaK
import arcpy



CaK_poly = "CaK_poly"
CaK_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\CaK.shp"
Aluminio_poly_Dissolve__2_ = CaK_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(CaK_poly, CaK_shp, "dis", "Ca_K__1__ MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(CaK_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Calcio
import arcpy



Calcio_poly = "Calcio_poly"
Calcio_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Calcio.shp"
Aluminio_poly_Dissolve__2_ = Calcio_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Calcio_poly, Calcio_shp, "dis", "Cblcio_cmo MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Calcio_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#CaMg
import arcpy



CaMg_poly = "CaMg_poly"
CaMg_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\CaMg.shp"
Aluminio_poly_Dissolve__2_ = CaMg_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(CaMg_poly, CaMg_shp, "dis", "Ca_Mg__1__ MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(CaMg_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Carbono Organico
import arcpy



Carbono_Organico_poly = "Carbono Organico_poly"
Carbono_Organico_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\CarbonoOrganico.shp"
Aluminio_poly_Dissolve__2_ = Carbono_Organico_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Carbono_Organico_poly, Carbono_Organico_shp, "dis", "Carbono_Or MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Carbono_Organico_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Cobre
import arcpy



Cobre_poly = "Cobre_poly"
Cobre_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Cobre.shp"
Aluminio_poly_Dissolve__2_ = Cobre_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Cobre_poly, Cobre_shp, "dis", "Cobre_mg_d MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Cobre_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#CTC_TOTAL
import arcpy



CTC_Total_poly = "CTC_Total_poly"
CTC_Total_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\CTCTotal.shp"
Aluminio_poly_Dissolve__2_ = CTC_Total_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(CTC_Total_poly, CTC_Total_shp, "dis", "CTC_Total_ MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(CTC_Total_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Enxofre
import arcpy



Enxofre_poly = "Enxofre_poly"
Enxofre_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Enxofre.shp"
Aluminio_poly_Dissolve__2_ = Enxofre_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Enxofre_poly, Enxofre_shp, "dis", "Enxofre_mg MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Enxofre_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Ferro
import arcpy



Ferro_poly = "Ferro_poly"
Ferro_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Ferro.shp"
Aluminio_poly_Dissolve__2_ = Ferro_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Ferro_poly, Ferro_shp, "dis", "Ferro_mg_d MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Ferro_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Fosforo
import arcpy



Fosforo_Mehlich_poly = "Fosforo_Mehlich_poly"
Fosforo_Mehlich_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\FosforoMehlich.shp"
Aluminio_poly_Dissolve__2_ = Fosforo_Mehlich_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Fosforo_Mehlich_poly, Fosforo_Mehlich_shp, "dis", "Fbsforo___ MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Fosforo_Mehlich_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#H_+AL
import arcpy



H__AL_poly = "H_+AL_poly"
H___AL_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\HMaisAL.shp"
Aluminio_poly_Dissolve__2_ = H___AL_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(H__AL_poly, H___AL_shp, "dis", "H_Al_cmol_ MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(H___AL_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#H+AL_CTC
import arcpy



H_AL_CTC_poly = "H+AL_CTC_poly"
H_AL_CTC_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\HMaisALCTC.shp"
Aluminio_poly_Dissolve__2_ = H_AL_CTC_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(H_AL_CTC_poly, H_AL_CTC_shp, "dis", "H_Al_CTC__ MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(H_AL_CTC_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Magnesio_CTC
import arcpy



Magnesio_CTC_poly = "Magnesio_CTC_poly"
Magnesio_CTC_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\MagnesioCTC.shp"
Aluminio_poly_Dissolve__2_ = Magnesio_CTC_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Magnesio_CTC_poly, Magnesio_CTC_shp, "dis", "Mg_CTC___ MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Magnesio_CTC_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Magnesio
import arcpy



Magnesio_poly = "Magnesio_poly"
Magnesio_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Magnesio.shp"
Aluminio_poly_Dissolve__2_ = Magnesio_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Magnesio_poly, Magnesio_shp, "dis", "Magn_sio_c MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Magnesio_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Manganes
import arcpy



Manganes_poly = "Manganes_poly"
Manganes_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Manganes.shp"
Aluminio_poly_Dissolve__2_ = Manganes_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Manganes_poly, Manganes_shp, "dis", "Mangands_m MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Manganes_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Materia_Organica
import arcpy



Materia_Organica_poly = "Materia_Organica_poly"
Materia_Organica_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\MateriaOrganica.shp"
Aluminio_poly_Dissolve__2_ = Materia_Organica_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Materia_Organica_poly, Materia_Organica_shp, "dis", "Mat_ria_Or MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Materia_Organica_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#MgK
import arcpy



MgK_poly = "MgK_poly"
MgK_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\MgK.shp"
Aluminio_poly_Dissolve__2_ = MgK_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(MgK_poly, MgK_shp, "dis", "Mg_K__1__ MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(MgK_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#pH_CaCl
import arcpy



pH_CaCl_poly = "pH_CaCl_poly"
pH_CaCl_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\pHCaCl.shp"
Aluminio_poly_Dissolve__2_ = pH_CaCl_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(pH_CaCl_poly, pH_CaCl_shp, "dis", "pH_CaCl2__ MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(pH_CaCl_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Potassio_CTC
import arcpy



Potassio_CTC_poly = "Potassio_CTC_poly"
Potassio_CTC_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\PotassioCTC.shp"
Aluminio_poly_Dissolve__2_ = Potassio_CTC_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Potassio_CTC_poly, Potassio_CTC_shp, "dis", "K_CTC___ MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Potassio_CTC_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Potassio
import arcpy



Potassio_poly = "Potassio_poly"
Potassio_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Potassio.shp"
Aluminio_poly_Dissolve__2_ = Potassio_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Potassio_poly, Potassio_shp, "dis", "Pot_ssio_c MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Potassio_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Potassio_ppm
import arcpy



Potassio_ppm_poly = "Potassio_ppm_poly"
Potassio_ppm_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Potassioppm.shp"
Aluminio_poly_Dissolve__2_ = Potassio_ppm_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Potassio_ppm_poly, Potassio_ppm_shp, "dis", "Pot_ssio_p MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Potassio_ppm_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Satturacao_de_Bases
import arcpy



Satturacao_de_Bases_poly = "Satturacao_de_Bases_poly"
Saturacao_de_bases_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\SaturacaoDebases.shp"
Aluminio_poly_Dissolve__2_ = Saturacao_de_bases_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Satturacao_de_Bases_poly, Saturacao_de_bases_shp, "dis", "Saturad MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Saturacao_de_bases_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Saturacao_por_Aluminio
import arcpy



Saturacao_por_Aluminio_poly = "Saturacao_por_Aluminio_poly"
Saturacao_por_Aluminio_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\SaturacaoPorAluminio.shp"
Aluminio_poly_Dissolve__2_ = Saturacao_por_Aluminio_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Saturacao_por_Aluminio_poly, Saturacao_por_Aluminio_shp, "dis", "Saturad MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Saturacao_por_Aluminio_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Silte
import arcpy



Silte_poly = "Silte_poly"
Silte_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Silte.shp"
Aluminio_poly_Dissolve__2_ = Silte_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Silte_poly, Silte_shp, "dis", "Silte_g_dm MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Silte_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Sodio
import arcpy



Sodio_poly = "Sodio_poly"
Sodio_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Sodio.shp"
Aluminio_poly_Dissolve__2_ = Sodio_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Sodio_poly, Sodio_shp, "dis", "Sbdio_mg_d MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Sodio_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

#Zinco
import arcpy



Zinco_poly = "Zinco_poly"
Zinco_shp = "C:\\Users\\junio\\Google Drive\\Projetos Geo\\Progeo\\Projetos\\Ernane Cruvinel\\Fazenda Matrinchã 20-40\\Processado\\Shapefiles\\Dissolve\\Zinco.shp"
Aluminio_poly_Dissolve__2_ = Zinco_shp
Aluminio_poly_Dissolve__3_ = Aluminio_poly_Dissolve__2_
Aluminio_poly_Dissolve__4_ = Aluminio_poly_Dissolve__3_
Aluminio_shp__2_ = Aluminio_poly_Dissolve__4_


arcpy.Dissolve_management(Zinco_poly, Zinco_shp, "dis", "Zinco_mg_d MEAN", "MULTI_PART", "DISSOLVE_LINES")


arcpy.AddField_management(Zinco_shp, "area", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__2_, "area", "!shape.area!/10000", "PYTHON_9.3", "")


arcpy.AddField_management(Aluminio_poly_Dissolve__3_, "percent", "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")


arcpy.CalculateField_management(Aluminio_poly_Dissolve__4_, "percent", "( [area] *100)/490.14", "VB", "")

