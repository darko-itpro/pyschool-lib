# Installation de la dépendance

## Récupérez la dernière version

Récupérez (téléchargez) le fichier `.whl` de la dernière release sur 
[la page des releases](https://github.com/darko-itpro/pyschool-lib/releases).

Pour plus de facilité pour la suite, déplacez le fichier au niveau du projet

## Installez la dépendance

L'installation se fera par l'invite de commande (Terminal, Dos, PowerShell).

Assurez vous si nécessaire que le virtual env  est activé

=== "Méthode standard"

    La commande à exécuter doit ressembler à :
    ```
    pip install pyflix-0.8.0-py3-none-any.whl
    ```

    Adaptez avec le nom du fichier qui contient le numéro de version.

=== "Avec uv"

    Si vous utilisez uv, vous pouvez installer la dépendance avec :
    ```
    uv add pyflix-0.8.0-py3-none-any.whl
    ```

    Adaptez avec le nom du fichier qui contient le numéro de version.

