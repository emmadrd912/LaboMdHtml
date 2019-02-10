## LaboMdHtml ##

### Utilisation du convertisseur ###

#### 1 : Copier le labo sur l'ordinateur ####

- Pour utiliser le labo vous pouvez choisir entre deux manières :

    - 1 : Cloner le labo git sur l'ordinateur.

    - 2 : Télécharger le fichier .zip et l'extraire sur votre ordinateur. 

#### 2 : Présentation des options et mise en marche ####

- Pour utiliser le convertisseur : 

    - Ouvrir une invite de commande (CMD, powershell, terminal ...) et se placer dans le chemin du labo où est placé le fichier index.py(le convertisseur).

    - Le convertisseur utilise des options pour convertir le md, pour les voir, il suffit d'éxecuter la commande:

    ```
    python index.py -h ou python index.py --help
    ```

    - On obtient les options suivantes :

    ```
    usage: index.py [-h] [-i INPUT] [-o OUTPUT]

    optional arguments:
    -h, --help            show this help message and exit
    -i INPUT, --input INPUT
                            Chemin vers le fichier .md
    -o OUTPUT, --output OUTPUT
                            Chemin vers le fichier .html
    -a, --achtung          Convertir texte pour faciliter les allemands
    ```

- Pour l'option -i ou --input : 
    - Il doit être suivi du fichier .md que l'on convertir en html ou le chemin vers le fichier.

- Pour l'option -o ou --output : 
    - Si vous avez crée un fichier .html dans le dossier où est placé index.py(le convertisseur) :
        - l'option -o ou --output doit être suivi du nom du fichier .html ou le chemin vers le fichier.
    - Si vous n'avez pas crée de fichier html, il suffit après le -o ou --output de mettre le nom du fichier html que vous souhaitez créer suivi de l'extension .html. En lançant la conversion, le fichier .html va se créer tous seul dans le dossier où est placé index.py.

- Pour l'option -a ou --achtung : 
    - Il suffit juste d'écrire -a ou --achtung pour traduire les textes en allemand. 

- Exemple d'utilisation : 

- Avec nom de fichier :  

```
$python index.py -i fichier.md -o fichier.html -a
Conversion fait avec succès
```

- Avec le chemin du fichier :

```
$python index.py -i ./mondossier/monfichier.md -o ./mondossier/monfichier.html -a
```


