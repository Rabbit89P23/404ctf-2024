# Bébé Nageur

- [Bébé Nageur](#bébé-nageur)
  - [Données](#données)
  - [Résolution](#résolution)
  - [Code](#code)

## Données

On connait :

- l'ensemble de caractères (`charset`) utilisé :

`abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!`

- le flag chiffré :

`-4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_`

## Résolution

On a :
- $n = 67$
- $a \in \llbracket 2, 66 \rrbracket$ et $b \in \llbracket 1, 66 \rrbracket$ deux entiers aléatoires

Le flag est chiffré caractère par caractère, de la manière suivante (pour chaque caractère) :
- le caractère est identifié par son emplacement dans l'ensemble de caractères utilisé
- cet entier $x$ est transformé en $y=(a.x + b) \space mod \space n$
- le caractère résultant est celui en position $y$ dans l'ensemble de caractères

Il faut alors remarquer quelque chose de crucial : $n=67$ est un nombre premier. Ainsi, tous les éléments de $\mathbb{Z}/n\mathbb{Z}$ sont inversibles (sauf $0$). On peut donc inverser la fonction de chiffrement :

$$
y=(a.x + b) \space mod \space n \Leftrightarrow x = a^{-1}(y - b) \space mod \space n
$$

Il suffit alors de tester toutes les possibilités de $a$ et $b$, en appliquant le chemin inverse :
- le caractère est identifié par son emplacement dans l'ensemble de caractères utilisé
- cet entier $y$ est transformé en $x = a^{-1}(y - b) \space mod \space n$
- le caractère résultant est celui en position $x$ dans l'ensemble de caractères

Remarques : 
- le bruteforce est ici plus qu'acceptable, étant donné que l'on n'a que $(n - 2)(n - 1) = 65.66 = 4290$ possibilités
- on peut supposer $a \neq 0$, sinon le flag chiffré ne serait qu'une répétition de la lettre en position $b$ du charset, donc $a$ est inversible.

## Code

L'implémentation de la solution est disponible [ici](./main.py).