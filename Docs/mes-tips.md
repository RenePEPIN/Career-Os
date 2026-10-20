# Tips de Création (PowerShell vs Linux)

## Créer un dossier
- PS: New-Item -ItemType "Directory" -Path "MonDossier" -Force
- Linux: mkdir -p MonDossier

## Créer un fichier dans un dossier existant
- PS: New-Item -ItemType "File" -Path "MonDossier/Fichier.txt" -Force
- Linux: touch MonDossier/Fichier.txt

## Créer dossier + fichier d'un coup
- PS: New-Item -ItemType "File" -Path "Docs/Vision.md" -Force
- Linux: mkdir -p Docs && touch Docs/Vision.md

## Créer avec du texte
- PS: "Texte" | Out-File -FilePath "Fichier.txt"
- Linux: echo "Texte" > Fichier.txt

*Note : Attention à la casse sous Linux (toujours 'touch' en minuscules !).*
