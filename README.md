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

- Calculatrice typée (pas de tests auto)

## Évaluer votre note en local

Vous pouvez évaluer votre note en local, avec:

```shell
$ python grader.py
```

Si les tests ne finissent jamais, appuyez sur `Ctrl + C` pour interrompre.

## Exercice 1 - Le palindrome

(Rendez votre exercice en complétant le fichier `palindrome.py`.)

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

## Exercice 2 - Fichiers et calcul du nombre de lignes, de mots et de caractères

(Rendez votre exercice en complétant le fichier `comptage.py`.)

On se propose d'écrire une _moulinette_ qui annote un fichier avec des nombres de lignes, de mots et de caractères.

Le but de l'exercice est d'écrire une fonction `comptage` :

- qui prenne en argument un nom de fichier d'entrée (on suppose qu'il existe) et un nom de fichier de sortie (on suppose qu'on a le droit de l'écrire) ;
- le fichier d'entrée est supposé encodé en UTF-8 ;
- le fichier d'entrée est laissé intact ;
- pour chaque ligne en entrée, le fichier de sortie comporte une ligne qui donne le numéro de ligne, le nombre de mots (**séparés par des espaces**), le nombre de caractères (y compris la fin de ligne), et la ligne d'origine.

```python
def comptage(in_filename, out_filename):
   # votre code ici
```

Exemple, avec `comptage("romeo_juliet.txt", "romeo_juliet_comptage.txt")`, dans le fichier `romeo_juliet.txt`:

```
Two households, both alike in dignity,
In fair Verona, where we lay our scene,
From ancient grudge break to new mutiny,
Where civil blood makes civil hands unclean.
```

et dans le fichier `romeo_juliet_comptage.txt`:

```
1:6:39:Two households, both alike in dignity,
2:8:40:In fair Verona, where we lay our scene,
3:7:41:From ancient grudge break to new mutiny,
4:7:45:Where civil blood makes civil hands unclean.
```

**N'oubliez pas de vérifier** que vous ajoutez bien les **fins de ligne**, car la vérification automatique est pointilleuse (elle utilise l'opérateur `==`), et rejettera votre code si vous ne produisez pas une sortie rigoureusement similaire à ce qui est attendu.

Le fichier [romeo_juliet.txt](romeo_juliet.txt) est accessible dans le repo pour tests.

**indice :** Pour compter le numéro de ligne, utilisez la fonction "enumerate":

```python
>>> names = ["aline", "bobby", "chisara"]
>>> for i, name in enumerate(names):
>>>   print(i, name)
0 "aline"
1 "bobby"
2 "chisara"
```

## Exercice 3 - Calculatrice polonaise inversée (postfix)

(Rendez votre exercice en complétant le fichier `calculatrice.py`)

### Sur les nombres entiers

Une fonction `postfix_eval` prend en entrée une chaîne qui décrit une opération à faire sur des entiers, en utilisant **la notation polonaise postfixée**, où on écrit par exemple `10 20 +` pour ajouter 10 et 20 ; cette notation est aussi appelée la **notation polonaise inverse**.

Les opérandes sont tous des entiers ; on demande de supporter les 4 opérations `+` `-` `*` et `/` (division entière), la calculatrice ne manipule donc que des entiers.

Lorsque la chaine est mal formée, vous devez renvoyer une des trois chaines suivantes :

- `error-syntax` si on ne peut pas comprendre l'entrée,
- `error-empty-stack`, si on essaie de faire une opération mais que l'on n'a pas les deux opérandes nécessaires,
- `error-unfinished`, si on détecte des opérandes non utilisés.

Exemples:

- `20 40 + 10 *` → `600`
- `20 6 6 + /` → `1`
- `10 -3 /` → `-4`
- `10 +` → `"error-empty-stack"`
- `10 20 30 +` → `"error-unfinished"`
- `10 20 30 oops` → `"error-syntax"`

### Calculatrice "typée"

Un peu plus difficile.

Écrire une variante de `postfix_eval` qui accepte en deuxième argument un type de nombre parmi `int`, `float`, ou `Fraction`, de sorte que la calculette utilise ce type pour faire ses calculs.

Pour les fractions:

```python
from fractions import Fraction
```

Exemples:

- `postfix_eval_typed("20 40 + 10 *", int)` → `600`
- `postfix_eval_typed("20 40 + 10 *", float)` → `600.0`
- `postfix_eval_typed("1 2 /", Fraction)` → `Fraction(1, 2)`

**indice :** attention au cas de la division, qui doit se comporter selon le type comme une division entière (comme dans `postfix_eval`), ou comme une division usuelle si le type le permet.

## License

All exercises above are licensed _CC BY-NC-ND, Thierry Parmentelat_

- [Palindrome](https://github.com/ue12-p22/python/blob/70e65198dbe5efa84608842c327286b7218f5807/notebooks/2-09-exos.py) (added examples)
- [Comptage dans un fichier](https://github.com/flotpython/course/blob/71e4a51e4832cc5e070b9a26bd3deedf576138a0/w3/w3-s2-x1-comptage.md) (trimmed examples)
- [Calculatruce](https://github.com/flotpython/course/blob/71e4a51e4832cc5e070b9a26bd3deedf576138a0/w6/w6-s9-x1b-postfix.md) (added examples)
