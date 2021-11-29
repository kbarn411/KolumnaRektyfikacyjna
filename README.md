# Kolumna Rektyfikacyjna
 
This repository contains GUI Python app which is my implementation of McCabe–Thiele method of calculating number of theoretical plates in distillation column (chemical engineering). 

## Files
- app.py - source code written in Python 3.8 programming language 
- app.exe - executable which can be run on Windows devices
- dane.txt - file with example of physicochemical data needed to perform calculations
- gui.png - screenshot of GUI interface

## Algorithm
- experimental data from dane.txt (or any other file text with same formatting as dane.txt) are fitted to polynomial
- theoretical minimum parameters for a column are calculated from shape of equilibrium curve
- real parameter of R value and equations describing work of a column are calculated 
- number of theoretical plates are estimated using equilibrium curve and equations mentioned above

## GUI
![GUI interface](https://raw.githubusercontent.com/kbarn411/KolumnaRektyfikacyjna/main/gui.png)
