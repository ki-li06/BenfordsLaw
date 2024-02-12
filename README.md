# BenfordsLaw
This code was written for my W-Seminararbeit about the Benford's Law (https://en.wikipedia.org/wiki/Benford%27s_law).
It analyzes the Gemeindeverzeichnis (like a list of all countys in Germany, download the latest Excel-File from https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/_inhalt.html#101366) on its conformity to Benford's Law.
To start this code, you have place first follwing files in directorys or create such directories.

1) ExcelSheets
2) ExcelSheets/Input
3) ExcelSheets/Input/Gemeindeverzeichnis - Vorlage.xlsx
    where you can create this file by
    1) creating a copy of the original Gemeindeverzeichnis file
    2) copying the 2nd sheet
    3) renaming the sheet to "GemeindeverzeichnisGekürzt"
    4) deleting all the cells underneath the 7th line (content of the table)
4) ExcelSheets/Output
5) ExcelSheets/GVZ

Now you have to run Main_ExcelFileGVzCopy.py to copy the "... - Vorlage.xlsx" file to the shortened version (for backup purposes)  "... - Gekürzt.xlsx"

After that, feel free to analyze which column you want. Choose from the following files:
- Main_GVzBevoelkerung.py
- Main_GVzFlaechen.py
- Main_GVzKoordinaten.py
- Main_GVzPLZ.py
