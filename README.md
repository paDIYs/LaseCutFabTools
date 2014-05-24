LaseCutFabTools
===============

This is the alfa version of laserCut useful tools for Rhinoceros

Requirements:
- McNeel Rhinoceros 5
- Python 2.7

List of Tools:
- Time: Estimate time of laserCut working
- Box maker: this is a parametric notched box generator for laserCut
- Joins maker: given a line generates a notched joins
- Bending wood: this is a parametric Kerf pattern (linear version) generator, for wood bending with a lasercut
  http://www.gedankensuppe.de/kerf-bending-patterns
  
How to install:
You can use this software with Rhino windows and Rhino mac version.
You need to put the .py files in a folder on your pc and add a toolbar and a button for each of one tool.

Advised position of the folder under windows OS  C:\Users\_yourPcName_\AppData\Roaming\McNeel\Rhinoceros\5.0\scripts\LaseCutFabTools
Put in this folder all of the 4 .py files.
Right click on the rhino Toolbar> click on NewTab> NewButton:
  -in Appearance setting you can import a bitmap icon of the button
  -in text fill it with the name of the button
  -in tooltip fill it with the description of the command
  - in command you will need to write: -_RunPythonScript (C:\Users\_nameOfYourUser_\AppData\Roaming\McNeel\Rhinoceros\5.0\scripts\LaserPlug-in\_nameOfPythonFile_)
   example: -_RunPythonScript (C:\Users\stefano\AppData\Roaming\McNeel\Rhinoceros\5.0\scripts\LaserPlug-in\Box_Maker.py)
  -Done!

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licenza Creative Commons" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">LaserCutFabTools</span> di<a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/paDIYs/LaseCutFabTools" property="cc:attributionName" rel="cc:attributionURL">Stefano Paradiso</a> è distribuito con Licenza <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribuzione - Non commerciale - Condividi allo stesso modo 4.0 Internazionale</a>.
