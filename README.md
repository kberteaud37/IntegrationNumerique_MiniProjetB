# IntegrationNumerique_MiniProjetB

Ce projet a été réalisé dans le cadre d’un mini-projet universitaire portant sur l’intégration numérique. Il permet de comparer différentes méthodes d’approximation de l’aire sous une courbe, en utilisant un polynôme de degré 3 défini par l’utilisateur.

## Objectif
L’objectif est de mettre en pratique plusieurs méthodes d’intégration numérique et de voir comment elles se comportent lorsqu’on les applique à un polynôme du 3e ordre. Le projet met aussi en évidence les différences de précision entre les approches selon le nombre de segments utilisés pour effectuer l’approximation.

## Ce que fait le programme
Lorsqu’on exécute le programme, l’utilisateur est invité à :

1. Saisir les coefficients d’un polynôme de degré 3, c’est-à-dire 4 coefficients correspondant à l’expression :
a + b·x + c·x² + d·x³.

2. Indiquer les bornes de l’intervalle sur lequel il souhaite intégrer la fonction.

3. Choisir le nombre de segments à utiliser pour le calcul.

Une fois ces informations données, le programme calcule l’aire sous la courbe à l’aide de trois méthodes d’intégration numérique :

- Méthode des rectangles

- Méthode des trapèzes

- Méthode de Simpson

Chaque méthode est exécutée deux fois : d’abord avec une implémentation "maison" (sans bibliothèque), puis avec une version qui utilise les fonctions intégrées de NumPy.

À la fin, les résultats sont affichés pour chaque méthode, avec une comparaison par rapport à la valeur exacte de l’intégrale (calculée directement à partir du polynôme).

## Ce que montre ce projet
Ce projet permet d’illustrer plusieurs idées simples :

- Plus le nombre de segments est élevé, plus l’approximation est précise.

- Certaines méthodes sont naturellement plus précises que d’autres.

- L’utilisation de bibliothèques comme NumPy peut faciliter ou fiabiliser les calculs.

- Le comportement des méthodes peut être observé facilement à travers un cas concret : l’intégration d’un polynôme du 3e ordre.

## Auteurs
Kilian Berteaud

MalAlphaDominant

EnzoV-lab
