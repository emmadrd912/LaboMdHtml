#importation des librairies
import argparse
import markdown2

head = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='utf-8'/>
    <link rel='stylesheet' type='text/css' href='main.css'/>
    <link href='https://fonts.googleapis.com/css?family=Roboto'rel='stylesheet'>
    <style>body {font-family: 'Roboto', sans-serif;}</style></head>
    <body>
    '''
footer = "</body>\n</html>"

#fonction permettant de convertir le .md en .html
def convert(md_fichier, html_fichier):
    input_file = open(md_fichier, "r", encoding="utf-8")
    text = input_file.read()
    html = markdown2.markdown(text)
    output_file = open(html_fichier, "w",encoding="utf-8")
    output_file.write(head + html + footer) 
    output_file.close()
    print('Conversion .md en .html fait avec succès')

#fonction permettant de convertir le .md en .html version allemande
def aide_allemands(md_fichier, html_fichier):
    input_file = open(md_fichier, "r",encoding="utf-8")
    text = input_file.read()
    html = markdown2.markdown(text)
    output_file = open(html_fichier, "w",encoding="utf-8")
    output_file.write(html) 
    output_file.close()
    sansallemands = open(html_fichier, "r",encoding="utf-8")
    text2 = sansallemands.read()
    avecallemands = open(html_fichier, "w",encoding="utf-8")
    aide = text2.replace("ss", "z").replace("s", "z").replace("qu", "k")
    aide = text2.replace("ce", "ze").replace("c", "k").replace("ç", "z")
    aide = text2.replace("ph", "f").replace("pp", "p").replace("gu", "ch")
    aide = text2.replace("g", "ch").replace("j", "k").replace("v", "f")
    aide = text2.replace("s", "").replace("mm","m")
    avecallemands.write(aide)
    avecallemands.close()
    print("Conversion .md en .html version allemande réussite.")

#focntion permettant d'ajouter kikoo
#def kikoo(md_fichier, html_fichier):
#    input_file = open(md_fichier, "r",encoding="utf-8")
#    text = input_file.read()
#    html = markdown2.markdown(text)
#    output_file = open(html_fichier, "w",encoding="utf-8")
#    output_file.write(html) 
#    output_file.close()
#    sanskikoo = open(html_fichier, "r", encoding="utf-8")
#    text2 = sanskikoo.read()
#    aveckikoo = open(html_fichier, "w", encoding="utf-8")
#    ajoutkikoo = html_fichier.append(["<p>Kikoo</p>", "<p>lol</p>", "<p>mdr</p>", "<p>ptdr</p>", "<p>lolilo</p>"])
#    aveckikoo.write(ajoutkikoo)
#    aveckikoo.close()
#    print("ajout de kikoo réussit")


#ajout d'option à l'utilisation du convertisseur
parser = argparse.ArgumentParser()
parser.add_argument("-i", '--input',help='Chemin vers le fichier .md')
parser.add_argument("-o", '--output',help='Chemin vers le fichier .html')
parser.add_argument("-a", '--achtung',help='Convertir texte pour faciliter les allemands', action="store_true")
#parser.add_argument("-k", '--kikoo',help="ajoute 'kikoo', 'lol', 'ptdr'... dans votre page html", action="store_true")
args = parser.parse_args()

#éxecution du convertisseur selon les options choisies
if args.achtung is True:
    print('Convertisseur .md en .html')
    print("Pour plus de renseignement sur l'utilisation du convertisseur, veuillez lire le README")
    aide_allemands(args.input,args.output)
#elif args.kikoo is True :
#    print('Convertisseur .md en .html')
#    print("Pour plus de renseignement sur l'utilisation du convertisseur, veuillez lire le README")
#    kikoo(args.input, args.output)
else:
    print('Convertisseur .md en .html')
    print("Pour plus de renseignement sur l'utilisation du convertisseur, veuillez lire le README")
    convert(args.input,args.output)
