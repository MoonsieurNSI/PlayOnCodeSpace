DROP TABLE IF EXISTS show; 
DROP TABLE IF EXISTS artiste;
DROP TABLE IF EXISTS salle;

-------------
CREATE TABLE artiste (
        artiste_id INT PRIMARY KEY,
        nom VARCHAR(255),
        pays VARCHAR(255),
        debut INT,        -- debut n'est pas une date 
        style VARCHAR(255));

-----------

COPY artiste(artiste_id, nom, pays, debut, style)
FROM '/tmp/artiste.csv'
DELIMITER ',' CSV HEADER;

-------------
CREATE TABLE salle (
        salle_id INT PRIMARY KEY,
        nom VARCHAR(255),
        ville VARCHAR(255),
        capacite INT);

---------------

COPY salle(salle_id, nom, ville, capacite)
FROM '/tmp/salle.csv'
DELIMITER ',' CSV HEADER;

----------------

CREATE TABLE show (
        show_id INT PRIMARY KEY,
        artiste_id INT,
        salle_id INT,
        debut DATE,
        fin DATE, 
        FOREIGN KEY(artiste_id) REFERENCES artiste(artiste_id),
        FOREIGN KEY(salle_id) REFERENCES salle(salle_id));

-----------------

COPY show(show_id, artiste_id, salle_id, debut, fin)
FROM '/tmp/show.csv'
DELIMITER ',' CSV HEADER;