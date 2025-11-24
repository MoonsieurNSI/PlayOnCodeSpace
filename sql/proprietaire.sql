-- Copier le fichier dans le répertoire /tmp
-- Se connecter à psql
-- \i /tmp/proprietaire.sql

-- Suppression si existe (Pensez à l'ordre ou CASCADE)
DROP TABLE IF EXISTS Animal;
DROP TABLE IF EXISTS Proprietaire;


-- Création
CREATE TABLE Proprietaire (
    ProID SERIAL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL
);

CREATE TABLE Animal (
    AniID SERIAL PRIMARY KEY,
    espece VARCHAR(255) NOT NULL,
    sexe CHAR(1),
    naissance DATE,
    nom VARCHAR(255) NOT NULL,
    commentaire TEXT,
    ProId INT, 
    FOREIGN KEY (ProId) REFERENCES Proprietaire(ProID)
);

--Ajout de lignes
INSERT INTO Proprietaire (nom, prenom)
VALUES
('NICOLAS', 'Patrice'),
('DUHEM', 'Aude');

INSERT INTO Animal (espece, sexe, naissance, nom, commentaire, ProId)
VALUES
('chien', 'M', '2015-02-01', 'Linux', 'Gentil', 1),
('chien', 'F', '2017-04-01', 'Nova', 'Peureuse', 2);

INSERT INTO Animal (espece, naissance, nom, ProId)
VALUES
('chat', '2020-11-01', 'PilePoil', 1);

INSERT INTO Animal (espece, sexe,  naissance, nom, ProId)
VALUES
('lapin', 'M', '2020-07-01', 'Jannot', 2);

-- suite du cours
-- INSERT INTO Animal (espece, naissance, nom, ProId)
-- VALUES
-- ('poisson', '2019-10-01', 'Nemo', 2);

-- INSERT INTO Animal (espece, sexe, naissance, nom, commentaire, ProId)
-- VALUES
-- ('chien', 'F', '2013-10-10', 'Pepita', 'Bruyante',  2),
-- ( 'chat', 'F', '2012-08-23' , 'Lila ' , 'Peureuse' ,1),
-- ( 'cheval', 'M', '2008-03-14' , 'Valentin' , 'Rapide' ,2),
-- ( 'cheval', 'F', '2008-03-14' , 'Valentine' , 'Lente' ,1),
-- ( 'oiseau', 'M', '2018-12-23' , 'Mozart' , 'Bruyant' ,1),
-- ( 'chien', 'F', '2015-02-01' , 'Windows' , 'Gentille' ,1);