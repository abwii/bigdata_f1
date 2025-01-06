# **Projet Big Data F1 - Analyse des Résultats du Championnat de Formule 1 (1950-2024)**

![F1 Logo](https://upload.wikimedia.org/wikipedia/commons/4/45/F1_logo.svg)

## **Description**

Ce projet vise à analyser les résultats du championnat du monde de Formule 1 depuis 1950 jusqu'en 2024 à l'aide d'une architecture Big Data basée sur **Azure Data Lake**, **Databricks**, et le framework **Delta Lake**.

L'objectif principal est de traiter les données brutes (couche Bronze), de les transformer en données propres (couche Silver), puis d'effectuer des analyses avancées (couche Gold) pour répondre à des questions clés telles que :
- Quels sont les meilleurs pilotes de l'histoire ?
- Quelles équipes ont dominé sur des périodes spécifiques ?
- Quelles tendances peuvent être observées au fil des décennies (temps de course, circuits, météo, etc.) ?

---

## **Architecture du Projet**

Le projet suit l'architecture **Medallion (Bronze-Silver-Gold)** pour le traitement des données :

1. **Couche Bronze :** Collecte des données brutes (CSV) depuis Azure Data Lake sans transformation.
2. **Couche Silver :** Nettoyage et enrichissement des données (gestion des valeurs manquantes, types, etc.).
3. **Couche Gold :** Données prêtes pour les analyses et tableaux de bord.


---

## **Données Utilisées**

Les données proviennent de [Kaggle Dataset - Formula 1 World Championship](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020).

### **Fichiers principaux :**
- **circuits.csv :** Informations sur les circuits.
- **drivers.csv :** Détails sur les pilotes.
- **results.csv :** Résultats des courses.
- **lap_times.csv :** Temps au tour pour chaque pilote.
- **seasons.csv :** Données sur les saisons de F1.
- Et bien d'autres...

---

## **Technologies Utilisées**

- **Azure Data Lake Storage Gen2** : Stockage des données brutes.
- **Databricks** : Environnement d'analyse et de traitement Big Data.
- **Delta Lake** : Stockage des données transformées pour une performance optimale.
- **PySpark** : Framework pour le traitement et l'analyse des données.
- **Python** : Scripts d'analyse et de visualisation.
- **Power BI** (optionnel) : Création de tableaux de bord interactifs.

---

## **Prérequis**

Avant de commencer, assurez-vous d'avoir configuré les éléments suivants :
1. **Compte Azure** : Créez un compte de stockage et un conteneur.
2. **Databricks** : Installez et configurez un cluster Databricks.
3. **Données Kaggle** : Téléchargez les fichiers et uploadez-les dans Azure.

---

## **Étapes de Déploiement**

### **1. Configurer le stockage Azure**
- Créez un conteneur nommé `bronze` dans votre compte Azure.
- Uploadez les fichiers CSV dans ce conteneur.

### **2. Monter Azure Data Lake dans Databricks**
Exécutez le code suivant dans un notebook Databricks pour monter le conteneur Azure :

```python
dbutils.fs.mount(
    source="wasbs://bronze@<nom_du_compte>.blob.core.windows.net/",
    mount_point="/mnt/bronze",
    extra_configs={"fs.azure.account.key.<nom_du_compte>.blob.core.windows.net": "<clé_d'accès>"}
)
