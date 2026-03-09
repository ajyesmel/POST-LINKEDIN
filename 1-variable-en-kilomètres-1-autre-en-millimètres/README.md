📊 **Impact du Feature Scaling sur les algorithmes de Machine Learning**

🎯 **Objectif**

Dans de nombreux projets de Machine Learning, les variables peuvent avoir des échelles très différentes.

Exemple :

Revenu annuel : 0 à 10 000 000

Âge : 18 à 65

Score : 1 à 5

Cette différence d’échelle peut influencer le comportement de certains algorithmes.

L'objectif de ce projet est de montrer l’impact du feature scaling sur la performance de plusieurs modèles de Machine Learning.


🧠 **Algorithmes étudiés**

Dans ce notebook, nous comparons plusieurs modèles :

K-Nearest Neighbors (KNN)

Régression Logistique

Support Vector Machine (SVM)

Arbre de décision

Les algorithmes basés sur la distance (comme KNN ou SVM) sont généralement plus sensibles à l’échelle des variables.


⚙️ **Méthodologie**

Les étapes de l'expérience sont les suivantes :

Génération d’un dataset synthétique

Séparation des données (train / test)

Entraînement des modèles sans transformation des variables

Entraînement des modèles avec standardisation (StandardScaler)

Comparaison des performances


📊 **Résultat principal**

Les résultats montrent que :

Les algorithmes basés sur la distance peuvent être fortement impactés par l’échelle des variables

La standardisation améliore souvent les performances et la stabilité des modèles

Les arbres de décision sont peu sensibles au scaling

🛠 **Technologies utilisées**

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn

Jupyter Notebook


💡 **Conclusion**

Le feature scaling est une étape essentielle du preprocessing en Machine Learning.

Comprendre quand et pourquoi l'utiliser permet de construire des modèles plus robustes et plus fiables.