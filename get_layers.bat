@echo off
echo Starting python script for finding source data in mxd file.
echo Dialog window will open shortly.
REM prvi argument je pot do python executabla potrebno uporabit 
REM python iz ArcGISa. Pot je odvisna od verzije ArcGIS-a (trenutno deluje za ArcGis 10.4)
REM python datoteka list_mxd_sources mora biti v enakem direktoriju ko ta .bat datoteka

C:\Python27\ArcGIS10.4\python.exe %~dp0getLayers.py
pause