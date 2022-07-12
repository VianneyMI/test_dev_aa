# Test technique Aramis Auto

## Présentation

Le test a été réalisé en partie dimanche après-midi puis Lundi. Faute de temps, certaines questions n'ont pas été traités on ne l'ont été que partiellement.
Ce repo contient une API demo contenu dans le dossier backend qui peut être tester en suivant les instructions de la section suivante, un fichier (legacy.py) qui reprend le code source exemple fourni en capture d'écran. Un fichier sql_exercice.sql qui contient les réponses aux questions SQL.
Les autres réponses aux questions sont dans le fichier answers.md

## Instructions pour lancer l'API démo

- Créer un environnement virtuel dans le dossier backend via la commande python -m venv venv
- Activer l'environnement virtuel, la commande dépendant du système d'exploitation https://docs.python.org/fr/3/tutorial/venv.html
- Installer les requirements avec la commande pip install -r requirements.txt
- Lancer le server avec la commande uvicorn app.main:app --reload
- Exécuter la commande pytest pour lancer les tests.

## Environnement utilisé

- python 3.10.4
- Windows 11 21H2
- VSCode

## Configuration VS Code utilisé

    {
        "python.languageServer": "Pylance",
        "python.analysis.autoImportCompletions": false,
        "python.linting.pylintEnabled": true,
        "python.linting.pylintArgs": [
            "--extension-pkg-whitelist=pydantic",
            "--disable=too-few-public-methods, no-member, invalid-name",
            "--max-line-length=150",
            "--notes=FIXME, WARNING, TODO, NOTE"
        ],

        "python.linting.mypyEnabled": true,
        "python.linting.mypyCategorySeverity.error":"Warning",
        "python.linting.mypyArgs": [
            "--show-error-codes",
            "--ignore-missing-imports",
            "--show-column-numbers",
            "--no-implicit-optional",
            "--disallow-untyped-defs",
            "--disallow-untyped-calls"
        ],


        "python.analysis.diagnosticSeverityOverrides": {
            "reportUnboundVariable": "none",
            "reportGeneralTypeIssues" : "none",
            "reportOptionalCall": "none",
            "reportOptionalIterable":"none",
            "reportOptionalSubscript": "none",
            "reportOptionalMemberAccess": "none",
            "reportMissingRequiredArgument": "none",
            "reportRedundantArgument": "none",
            "reportImportCycles" : "none",
            "reportPropertyTypeMismatch" : "none",
            "reportMissingTypeStubs" : "none"

        },

        "files.exclude": {
            "**/.git": true,
            "**/.svn": true,
            "**/.hg": true,
            "**/CVS": true,
            "**/.DS_Store": true,
            "**/*.pyc": {"when": "$(basename).py"},
            "**/__pycache__": true
        },

        "files.eol": "\n",
    }

