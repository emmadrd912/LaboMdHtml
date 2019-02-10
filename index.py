import argparse
import markdown2
import os


def convert(md_fichier, html_fichier):
    input_file = open(md_fichier, "r")
    text = input_file.read()
    html = markdown2.markdown(text)
    output_file = open(html_fichier, "w")
    output_file.write(html) 
    output_file.close()
    print('Conversion fait avec succès')


def aide_allemands(md_fichier, html_fichier):
    input_file = open(md_fichier, "r")
    text = input_file.read()
    html = markdown2.markdown(text)
    output_file = open(html_fichier, "w")
    output_file.write(html) 
    output_file.close()
    sansallemands = open(html_fichier, "r")
    text2 = sansallemands.read()
    avecallemands = open(html_fichier, "w")
    aide = text2.replace("ss", "z").replace("s", "z").replace("qu", "k").replace("ce", "ze").replace("c", "k").replace("ç", "z").replace("ph", "f").replace("pp", "p").replace("gu", "ch").replace("g", "ch").replace("j", "k").replace("v", "f").replace("s", "")
    avecallemands.write(aide)
    avecallemands.close()

print('Convertisseur .md en .html')
print("Pour plus de renseignement sur l'utilisation du convertisseur, veuillez lire le README")

parser = argparse.ArgumentParser()
parser.add_argument("-i", '--input',help='Chemin vers le fichier .md')
parser.add_argument("-o", '--output',help='Chemin vers le fichier .html')
parser.add_argument("-a", '--achtung',help='Aide les allemands à lire nos écrits', action="store_true")
args = parser.parse_args()

if args.achtung is True:
    aide_allemands(args.input,args.output)
else:
    convert(args.input,args.output)
