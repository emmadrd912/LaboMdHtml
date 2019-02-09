import argparse
import markdown2
import os
import re


def convert(md_fichier, html_fichier):
    input_file = open(md_fichier, "r")
    text = input_file.read()
    html = markdown2.markdown(text)
    output_file = open(html_fichier, "w")
    output_file.write(html) 


parser = argparse.ArgumentParser()
parser.add_argument("-i", '--input',help='Chemin vers le fichier .md')
parser.add_argument("-o", '--output',help='Chemin vers le fichier .html')
args = parser.parse_args()

print('Conversion fait avec succès')

convert(args.input,args.output)