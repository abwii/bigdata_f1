# Analyse des performances aux championnats du monde de Formule 1

## État actuel

### Sujet et objectifs
- **Sujet :** Analyser les performances des pilotes, des écuries et des voitures en Formule 1 de 1950 à 2024.
- **Objectifs :**
  - Comprendre les tendances historiques.
  - Identifier des relations et anomalies.
  - Proposer des prédictions basées sur les données historiques.

### Jeux de données
- **Dataset :** Formula 1 World Championship 1950-2024.
- Les tables du dataset sont reliées selon un MCD (Modèle Conceptuel des Données) à clarifier.

### Architecture et traitements
- **Stockage :** Envisagé dans Azure Synapse Analytics.
- **Traitements :**
  - Nettoyage et transformation des données.
  - Ajout de champs calculés.
  - Utilisation de régression linéaire pour des prédictions.

---

## Étapes recommandées pour la suite

### 1. Clarifier le MCD et les relations entre tables
- Documenter clairement les relations entre les entités du dataset (pilotes, écuries, courses, circuits, chronos, etc.).
- Identifier les clés primaires et étrangères.

### 2. Nettoyage et préparation des données
- Identifier les colonnes clés et les données manquantes.
- Supprimer ou imputer les valeurs manquantes.
- Traiter les anomalies (temps aberrants, valeurs en doublon).
- Ajouter des champs calculés (ex. écart moyen par tour, ratio victoires/podiums).

### 3. Analyse exploratoire des données (EDA)
- Étudier les distributions des variables clés (temps de course, classement, etc.).
- Identifier les tendances (amélioration des chronos par saison, performances des écuries, etc.).
- Comparer les performances sur différents circuits ou sous différentes conditions météorologiques.

### 4. Modélisation des données
- **Régression linéaire :**
  - Prédire les performances (temps de course, écarts entre pilotes) avec des variables explicatives comme le circuit, les conditions météorologiques, et la saison.
- Tester des modèles non linéaires ou d’autres algorithmes de machine learning si les performances sont insuffisantes.

### 5. Visualisation des données
- Créer un tableau de bord Power BI ou Apache Superset avec des visualisations dynamiques :
  - Évolution des performances des pilotes et des écuries au fil des saisons.
  - Répartition des victoires par circuit et par pays.
  - Analyse des écarts entre pilotes pour une même course.
  - KPI clés comme le nombre de victoires, podiums, ou points par pilote/écurie.

### 6. Structuration des livrables
- **Rapport PDF :**
  - Présentation des objectifs.
  - Description du dataset et de la méthode.
  - Résultats de l’analyse exploratoire et modélisation.
  - Conclusions et recommandations.
- **Data Pipeline :**
  - Décrire en détail les étapes de la collecte, nettoyage, transformation, et analyse.
- **Code :**
  - Publier les scripts sur un dépôt (GitHub/GitLab).

### 7. Améliorations futures
- Incorporer d’autres datasets (ex. météo, innovations technologiques).
- Tester d’autres architectures de calcul (Dremio, Apache Iceberg).
- Intégrer une analyse en streaming pour suivre les courses en temps réel (Kafka ou Redpanda).
