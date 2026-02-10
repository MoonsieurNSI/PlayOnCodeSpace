--CREATE TABLE Joueur(nom VARCHAR(255), PRENOM VARCHAR(255),
--couleurMaillot CHAR(10),salaire NUMERIC(7, 2), tel VARCHAR(20)
--);

-- copier le fichier dans /tmp/...
-- exécuter avec \i /tmp/.... dans 


--CREATE TABLE Eleve ( nom VARCHAR (255) PRIMARY KEY , prenom VARCHAR (255)
--UNIQUE NOT NULL , naissance DATE , age INT , CHECK ( age >= 18) ) ;

-- SELECT espece, nom FROM animal;

-- INSERT INTO Proprietaire
-- VALUES (1, 'DUHEM', 'Aude');

-- INSERT INTO Animal
-- VALUES (3, 'chien', 'F', '2017-04-01', 'Nova', 'Peureuse', 2),
-- (4, 'lapin', 'M', '2020-07-01', 'Jeannot', NULL, 2);

-- SELECT nom, naissance, sexe FROM Animal WHERE sexe='M';

-- SELECT nom, sexe FROM animal WHERE commentaire IS NULL; --au lieu de = pour NULL

-- WHERE UPPER(espece)='LAPIN'
-- chapitre-# AND UPPER(nom) NOT LIKE '%I%';

-- SELECT nom FROM animal
-- WHERE UPPER(espece)='LAPIN'
-- AND UPPER(nom) <> '%I%';

INSERT INTO animal VALUES
(5, 'chien', 'F', '2013-10-10','Pepita', 'Bruyante',2),
(6, 'chat', 'F', '2012-08-23','Lila', 'Peureuse',1),
(7, 'cheval', 'M', '2008-03-14', 'Valentin', 'Rapide',2),
(8,'cheval', 'F', '2008-03-14', 'Valentine', 'Lente',1),
(9, 'poisson', NULL, '2019-10-01', 'Nemo', NULL,2),
(10, 'oiseau', 'M', '2018-12-23', 'Mozart', 'Bruyant',1),
(11, 'chien', 'F', '2015-02-01', 'Windows', 'Gentille',1);


SELECT nom, espece, naissance FROM animal
WHERE proID=1
ORDER BY naissance DESC, nom; 
--pour nommer WINDOWS avant lINUX on ajoute DESC après nom

SELECT nom, espece, naissance FROM animal
WHERE espece='chien'
ORDER BY naissance DESC
LIMIT 2
OFFSET 1;

SELECT DISTINCT naissance FROM animal;

SELECT DISTINCT espece FROM animal;
SELECT DISTINCT espece FROM animal ORDER BY espece;