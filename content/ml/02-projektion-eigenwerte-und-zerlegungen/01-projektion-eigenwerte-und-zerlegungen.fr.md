---
title: Vue d’ensemble : Projection, valeurs propres et décompositions
kurz: Vue d’ensemble
pfad: Informatique / Apprentissage automatique / Projection, valeurs propres et décompositions
order: 6220100
summary: Points les plus proches, directions naturelles et les briques d’une matrice
tags: 
lang: fr
---

## De quoi il s’agit

Une question est restée ouverte dans la Partie 1. Quatre appartements sont décrits par leur surface et leur nombre de pièces, et leurs prix sont connus. On cherche deux poids tels que la somme pondérée donne exactement chaque prix. De tels poids n’existent pas : quatre équations à deux inconnues se contredisent. Avec des données de mesure, c’est presque toujours ainsi. On dispose de plus de mesures que d’inconnues, chaque mesure est un peu imprécise, et le système d’équations n’a pas de solution. Il faut pourtant des poids, et plus précisément ceux qui se trompent le moins possible.

Ce chapitre examine cette question ainsi que deux autres, qui se révèlent étroitement liées. Existe-t-il des directions dans lesquelles une matrice ne fait qu’allonger ou raccourcir une flèche, sans la faire tourner, et que révèlent ces directions sur la matrice ? Et peut-on décomposer toute matrice en quelques briques simples, classées par ordre d’importance, de sorte que l’on puisse omettre les moins importantes ? À cela s’ajoute une question pratique : de combien le résultat d’un calcul change-t-il lorsque les données sont un peu fausses ?

À quoi cela sert : grâce aux réponses, on ajuste une droite ou une autre règle simple à des valeurs mesurées de sorte que l’erreur soit la plus petite possible. On reconnaît si une fonction de plusieurs variables présente un creux, une crête ou une selle. On approche une image ou un grand tableau avec peu de nombres, en sachant ce que l’on perd au passage. Et l’on peut estimer si l’on peut se fier au résultat d’un calcul. Les outils de ce chapitre reviennent dans presque toutes les parties suivantes de la série.

**Comment travailler avec ce chapitre.** Les sections s’appuient les unes sur les autres, et chaque nouvelle notion a sa propre sous-section avec un exemple. Les encadrés dépliables contiennent le contexte (pourquoi une méthode fonctionne et d’où elle vient), les démonstrations et les preuves ; ils ne sont pas nécessaires pour poursuivre la lecture. Essayez d’abord de résoudre les exercices (de ★ à ★★★) vous-même et exécutez réellement les programmes ; la solution se déplie juste en dessous de chaque exercice.
