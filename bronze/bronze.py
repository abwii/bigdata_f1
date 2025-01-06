# Configuration et Montage d'un Point d'Accès Azure Data Lake
# Définir les variables nécessaires pour connecter Azure et Databricks

# Nom du compte Azure Storage
storage_name = "efreif1"
# Nom du conteneur dans Azure Storage
container_name = "bronze"
# Clé d'accès au compte Azure Storage
access_key = ""
# Point de montage Databricks
mount_point_name = "/mnt/bronze"

# Montage du conteneur Azure
dbutils.fs.mount(
    source=f"wasbs://{container_name}@{storage_name}.blob.core.windows.net/",
    mount_point=mount_point_name,
    extra_configs={f"fs.azure.account.key.{storage_name}.blob.core.windows.net": access_key}
)

# Vérifier si le conteneur est monté correctement
dbutils.fs.ls(mount_point_name)


# Chemins des fichiers CSV dans le conteneur monté
bronze_circuits = "/mnt/bronze/circuits.csv"
bronze_drivers = "/mnt/bronze/drivers.csv"
bronze_results = "/mnt/bronze/results.csv"

# Charger les fichiers dans des DataFrames Spark
df_bronze_circuits = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(bronze_circuits)

df_bronze_drivers = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(bronze_drivers)

df_bronze_results = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(bronze_results)

# Afficher les premières lignes pour validation
df_bronze_circuits.show(5)
df_bronze_drivers.show(5)
df_bronze_results.show(5)


# Sauvegarder les DataFrames dans la couche Bronze au format Delta

df_bronze_circuits.write.format("delta").mode("overwrite").save("/mnt/bronze/delta/circuits")
df_bronze_drivers.write.format("delta").mode("overwrite").save("/mnt/bronze/delta/drivers")
df_bronze_results.write.format("delta").mode("overwrite").save("/mnt/bronze/delta/results")

# Vérifier les fichiers sauvegardés
dbutils.fs.ls("/mnt/bronze/delta/")


# Charger et afficher les données sauvegardées
df_circuits_delta = spark.read.format("delta").load("/mnt/bronze/delta/circuits")
df_circuits_delta.show()

df_drivers_delta = spark.read.format("delta").load("/mnt/bronze/delta/drivers")
df_drivers_delta.show()
