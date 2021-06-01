# sendMailApp
Envoie automatisé de mails, avec pièces jointes, et à plusieurs adresses mails.

#
## Fichier config.json
Créer un fichier `config.json` à la racine et y mettre : 
```
{
    "mail" : "adresseMail@gmail.com",
    "pw" : "motDepPasse",
    "subject" : "Sujet du mail à envoyer",
    "files" : "chemin/du/fichier1.txt, chemin/du/fichier2.json, chemin/du/fichier3.csv"
}
```
/!\ Pour la liste des fichiers à envoyer, il faut les séparé par ",", et indiquer le bon chemin (le plus simple étant de les mettre à la racine).

/!\ L'adresse mail doit être une adresse mail d'un compte google, et doit être désécurisé
Pour se faire, il faut : 
- Retirer la double authentification. (désactivé par défaut).
- Activer l'accès moins sécurisé au compte.
#
## Fichier body.txt
Créer un fichier `body.txt` à la racine, pour y mettre le message à envoyer par mail.
#
## Fichier not_send.txt
Créer un fichier `not_send.txt` à la racine, pour y mettre toutes les adresses mails à qui envoyer le mail.
Ex : 
```
adresse1@gmail.com
adresse2@hotmail.com
adresse3@free.fr
```
#
## Fichier already_send.txt
Créer un fichier `already_send.txt` à la racine. Ce fichier va se remplir automatiquement pour y mettre les adresses mails à qui un mail a déjà été envoyé.

#
## Prérequis
Il faut avoir installé python3 : 
- Linux : `sudo apt install python3.9`
- w10 : 
    * Télécharger la version ici : https://www.python.org/downloads/windows/
    * /!\ Lors de l'installation, cliquer sur "Add to Path".

#
## Lancer le projet
- Linux : `python3 main.py` à la racine du projet.
- W10 : `python.exe .\main.py` à la racine du projet.

#