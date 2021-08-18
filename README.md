# Koala

Un compagnon à Pandas pour les SVT.

Ce module hérite de pandas.DataFrame et permet de tester facilement et rapidement des régressions linéaires, puissances, et exponentielles.

## Installation

    git clone https://github.com/YannBouyeron/koala
    
    cd koala
    
    sudo python setup.py install
    
## Exemple 1:

On import les modules suivants:

    >>> import pandas as pd
    >>> import numpy as np
    >>> from koala import Koala

On crée 2 séries de données:

    >>> x = np.arange(20)
    >>> y = 2 * x + 8

    >>> x
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
    17, 18, 19])
    
    >>> y
    array([ 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
    42, 44, 46])

On instancie un objet Koala:

    >>> kf = Koala({"abs":x, "ord":y})
    >>>
    >>> kf.head()
       abs  ord
    0    0    8
    1    1   10
    2    2   12
    3    3   14
    4    4   16

On teste une régression linéaire:

    >>> lin = kf.lin("abs", "ord")
    

<p align="center">
  <img src="Images/0D38B61D-9A9B-40F9-AAD2-1E20BC76A06D.png">
</p>


On exploite l'objet Koala (variable lin) pour retrouver les inforamtions de la régression et légender le graphique:

    
    >>> lin
    AttrDict({'a': 1.9999999999999998, 'b': 8.000000000000002, 'r': 1.0, 'equation': 'y = 2.0x + 8.0', 'graph': <module 'matplotlib.pyplot' from '/usr/local/lib/python3.6/site-packages/matplotlib/pyplot.py'>})
    >>>
    >>> lin.a
    1.9999999999999998
    >>> lin.b
    8.000000000000002
    >>> lin.r
    1.0
    >>> lin.equation
    'y = 2.0x + 8.0'
    
    >>> plt.text(7.5, 15, lin.equation, fontsize=8)
    Text(7.5,15,'y = 2.0x + 8.0')
    
    >>> plt.text(7.5, 10, "R = " + str(lin.r), fontsize=8)
    Text(7.5,10,'R = 1.0')
    
    >>> plt.show()


<p align="center">
  <img src="Images/978453B3-A49C-4D0C-9546-5C1758F2DB3E.png">
</p>


On sauvegarde le graphique légendé:

    >>> plt.savefig("linplot.png")


## Exemple 2:

[Etude de la correlation UV mélanomes avec pandas, geopandas et koala](https://gist.github.com/YannBouyeron/5e27cff8568725e71de245e10933bb56)

