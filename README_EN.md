## LaboMdHtml ##

### Using the converter ###

/// READ requirements.txt /// This necessary are surrounded by a star. ///

#### 1 : Copier le labo sur l'ordinateur ####

- Pour utiliser le labo vous pouvez choisir entre deux manières :

    - 1: Copy the lab to the computer

    - 2: Download the .zip file and extract it to your computer.

#### 2: Presentation of options and startup ####

- To use the converter:

    - Open a command prompt (CMD, powershell, terminal ...) and place yourself in the path of the lab where the index.py file (the converter) is placed.

    - The converter uses options to convert the md, to see them, just execute the command:

    ```
    python index.py -h ou python index.py --help
    ```

    - We obtain the following options:

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

- For the -i or --input option:
    - It must be followed by the .md file that one wants to convert to html or must be followed by the path leading to the file.

- For the -o or --output option:
    - If you have created a .html file in the folder where index.py (the converter) is placed:
        - the -o or --output option must be followed by the name of the .html file or must be followed by the path to the file.
    - If you have not created a html file, just after the -o or --output to put the name of the html file you want to create followed by the extension .html. By launching the conversion, the .html file will be created all alone in the folder where you are placed.

- For the -a or --achtung option:
    - Just write -a or --achtung to translate the texts into German.

- Example of use :

- With file name: 

```
$python index.py -i file.md -o file.html 
```
    or 
    
```
$python index.py -i file.md -o file.html -a
```

- With the file path:

```
$python index.py -i ./myfilepath/myfile.md -o ./myfilepath/myfile.html -a
```


