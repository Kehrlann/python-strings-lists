# python-strings-lists

## Consignes générales

Les chaînes de caractères, et les listes ... en Python!

Vous allez faire 3 exercices. Pour le rendu, remplissez **uniquement les fonctions** dans les fichiers désignés, veillez bien à n'ajouter aucun autre code dans ces fichiers. Évaluez votre note en local de temps en temps (cf ci-dessous).

Pendant que vous préparez vos exercices, vous pouvez travailler dans un notebook, ou dans un fichier `essais.py` si vous le souhaitez, par exemple:

```python
from palindrome import display_palindrome

display_palindrome("coucou")
display_palindrome("kayak")
```

## Rendre votre travail

Quand le résultat pour un des exercices est satisfaisant, git add, git commit, git push:

```shell
$ git add palindrome.py calculatrice.py
$ # ajoutez aussi tout autre fichier que vous voulez committer
$ git commit --message "Palindrome v2, calculatrice v1"
$ git push
```

Rendus **obligatoires**:

- Exercices sur les fichiers
- Palindrome
- Display palindrome
- Calculatrice (nombres entiers)

Rendus facultatifs:

- Calculatrice typée

## Évaluer votre note en local

Vous pouvez évaluer votre note en local, avec:

```shell
$ python grader.py
```

Si les tests ne finissent jamais, appuyez sur `Ctrl + C` pour interrompre.

## Exercice 1 - Le palindrome

Effectuez vos exercies dans le fichier `palindrome.py`.

### Version simple: `palindrome`

Écrivez une fonction qui vérifie si une chaine est un [palindrome](https://fr.wikipedia.org/wiki/Palindrome)

Par exemple:

- `palindrome("kayak")` → `True`
- `palindrome("something")` → `False`
- `palindrome("Eva, Can I Stab Bats In A Cave?")` → `True`
- `palindrome("A Man, A Plan, A Canal-Panama")` → `True`

Indice pour ignorer la ponctuation :

```python
>>> import string
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```

### Un peu moins simple: `display_palindrome`

Même exercice, mais on veut cette fois voir les différences:

par exemple:

- quand le mot est un palindrome

```python
>>> display_palindrome("kayak")
kayak
kayak
OK
```

- quand il n'en est pas un

```python
>>> display_palindrome("follet")
follet
tellof
^^  ^^
```

Pour cette variante, on suppose que le mot ne contient pas de ponctuation.

## License

All exercises below are licensed
_CC BY-NC-ND, Thierry Parmentelat_

- [Palindrome](https://github.com/ue12-p22/python/blob/70e65198dbe5efa84608842c327286b7218f5807/notebooks/2-09-exos.py), added examples
- [Calculatruce]()
