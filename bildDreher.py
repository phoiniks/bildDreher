#!/usr/bin/python

# agrell@havi.de, 2014

##########################################################
# Dieses Skript dreht spiegelverkehrte, auf dem Kopf     #
# stehende JPEGs richtig herum.                          #
# Ob es bei entsprechender Anpassung auch mit TIFFs      #
# oder anderen Formaten funktioniert, habe ich nicht     #
# getestet.                                              #
# Unter Verwendung des Python-Moduls multiprocessing     #
# wäre auch eine hochperformante Ausführung, also mit    #
# großen Mengen Bildmaterials denkbar. (Ich habe es mit  #
# mehreren Tausend JPEGs getestet.                       #
##########################################################

import Image
from os.path import splitext
from glob import glob

images = glob("*.jpg")

for i in images:
    print("Now processing %s." %i)
    img = Image.open(i)
    head, tail = splitext(i)
    convert = img.transpose(Image.FLIP_TOP_BOTTOM)
    out = head + "_out" + tail
    convert.save(out)
