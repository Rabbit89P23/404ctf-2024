# Plongeon Rapide Super Artistique

- [Plongeon Rapide Super Artistique](#plongeon-rapide-super-artistique)
  - [Données](#données)
  - [Résolution](#résolution)
  - [Code](#code)


## Données

On a les données suivantes :
- $N$, le produit des deux polynômes $P$ et $Q$

```
15193992477728078349*x^14 + 20849951573235599290*x^13 + 31626787439292941810*x^12 + 41606030540518542243*x^11 + 51135239778172914618*x^10 + 54839205054373601768*x^9 + 61504808736544546256*x^8 + 69077638236743212818*x^7 + 53980744540731499013*x^6 + 48344582546079800218*x^5 + 37874750456914975063*x^4 + 28415628763501783372*x^3 + 19286832846769454663*x^2 + 13073046561885731511*x + 7807279729190335309
```

- $n$, qui est le résultat de l'évaluation du polynôme $N$ en $r$ (on ne connaît pas r)

```
108467639697839662757675119579277149084242308356218922071090918908615374948181781274150380885272044494446721088127180898926333391217444363867805503733024234462862873998737363236748030712385045260063783565046555205958369142785754700441856622886319553247371639123221105096296162808152357323029673800985543
```

- $c$, qui est le flag chiffré (avec RSA) :

```
88755015861533943167974559872713361696099145214213848793491838241022886852405120609704167406295045592769591587483471982775519184576012814288576845480957257644075924651736974849836538134802852128574442137122106558275855261092222278387967861419587133198657052818619203674183040801840364877770834201106835
``` 

- l'exposant public utilisé pour RSA :

```
65537
```

## Résolution

On a :

$$
N = P.Q\\
n = N(r)
$$

On peut utiliser `sagemath` pour factoriser $N$. On trouve $P$ et $Q$ deux polynômes tel que $N=P.Q$.

On remarque que $P$ et $Q$ ne peuvent pas être factorisés davantage. 

En effet, les polynômes $P$ et $Q$ sont construits pour respecter deux propriétés :
-  $P \wedge Q = 1$
-  ils ne sont (tous les deux) pas factorisables dans $\mathbf{Q}[X]$

On connaît dorénavant $P$ et $Q$ tel que $N=P.Q$ (de manière unique à symétrie près sur $P$ et $Q$).

On peut donc définir le polynôme suivant :

$$
R = P.Q - n
$$

On remarque qu'il vérifie $R(r)=0$, où $r$ est défini par $n=N(r)$.

On peut donc lister les racines de $R$, et il n'y en n'a qu'une.

On a donc dorénavant $r$ tel que $n=N(r)=P(r).Q(r)$

On peut donc calculer :

$$
p = P(r)\\
q = Q(r)
$$

On peut ensuite calculer l'exposant privé $d$ en utilisant l'exposant public dans le chiffrement RSA ($65537$). En notant $\phi$ l'indicatrice d'Euler, comme $p$ et $q$ sont premiers (par construction), on a :

$$
\phi (n) = (p-1)(q-1)\\
d = 65537^{-1} \space mod \space \phi(n)
$$

Il nous suffit ensuite de déchiffrer le flag :

$$
flag=c^d \space mod \space n
$$

Après une conversion vers une chaîne de caractères, on a le résultat.

## Code

L'implémentation de la solution est disponible [ici](./main.sage) (utilisation : `sage main.sage`).