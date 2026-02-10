-- Dans PostgresSQL, \i /tmp/table.sql pour exécuter 
-- Il faut préalablement copier le fichier /tmp/villesfrance.csv
--suppression de ville si présente
DROP TABLE IF EXISTS ville;

--Création de la table ville
CREATE TABLE ville(
ID INT PRIMARY KEY,
Dep VARCHAR(3),
Nom VARCHAR(255),
CodePostal VARCHAR(255),
INSEE VARCHAR(10),
Habitants INT,
Densite REAL,
Surface REAL,
Longitude REAL,
Latitude REAL,
Altitude VARCHAR(255)
);

--Copie du csv dans la table ville
COPY ville (ID,
Dep,
Nom,
CodePostal,
INSEE,
Habitants,
Densite,
Surface,
Longitude,
Latitude,
Altitude)
FROM '/tmp/villesfrance.csv' DELIMITER ',' CSV HEADER;