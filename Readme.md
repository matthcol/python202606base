# Python

## Executer code Python

```
python --version
python hello.py
python # mode interactif
```

## Notebooks
Pour VSCode, installer l'extension Notebook Jupyter.

Ajouter jupyterlab dans l'environnement python.

Avec conda (extra numpy + matplotlib):
```
conda install jupyterlab numpy matplotlib
```

Avec pip:
```
pip install jupyterlab numpy matplotlib
```

En mode web:
```
jupyter lab
```

## Gestion des dépendances
Gestionnaire : pip, conda, mamba, poetry.

Ajouter une dépendance:
```
conda install pytest
pip install pytest
```

Avec un fichier requirements.txt
```
conda install --file requirements.txt
pip install -r requirements.txt
```

## Tests avec pytest
En mode CLI:
```
pytest
pytest -v
```
