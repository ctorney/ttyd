
# python script to convert all ttf files in the current directory to woff2 format using fontTools

from fontTools.ttLib import TTFont
import os

for file in os.listdir("."):
    if file.endswith(".ttf"):
        font = TTFont(file)
        font.flavor = "woff2"
        font.save(file[:-4] + ".woff2")
        print("Converted " + file + " to woff2 format")
