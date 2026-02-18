--1
SELECT nom FROM ville ORDER BY nom;

--2
SELECT code, nom FROM ville WHERE UPPER(nom) LIKE '%Z%' or UPPER(nom) LIKE 'T%';

--3
SELECT DISTINCT categorie FROM evolution ORDER BY categorie;

--4
SELECT code FROM ville WHERE nom = 'Caullery';
--SELECT code FROM ville WHERE nom LIKE 'Caullery';

--5
SELECT nom FROM ville WHERE nom LIKE '_____';

--6
SELECT * FROM evolution WHERE code = 59140 ORDER BY effectif;
--SELECT * FROM evolution WHERE code = 59140 ORDER BY effectif ASC;

--7
INSERT INTO ville VALUES (35000, 'Rennes', 50.291048, 2.7772211);
--INSERT INTO ville(code, nom, latitude, longitude) VALUES (35000, 'Rennes', 50.291048, 2.7772211);

--8
UPDATE ville SET nom = 'New-York' WHERE code = 35000;

--9
ALTER TABLE ville RENAME COLUMN nom TO nomVille;

--10
DELETE FROM evolution WHERE code IN (SELECT code FROM ville WHERE nomville = 'New-York' OR nomville = 'Lille');
--DELETE FROM ville WHERE nomville = 'New-York' OR nomville = 'Lille';

-- On supprime d'abord dans la table évolution car elle contient la clé étrangère
-- qui fait référence à la table ville. Si on supprime dans l'ordre inverse alors
-- la colonne code de la table evolution "pointerait" vers deux codes qui n'existe pas.
-- (violation de la contrainte de référence).

-- il existe la clause ON DELETE CASCADE qui peut être écrite au moment de la création 
-- Dans ce cas, on peut supprimer uniquement les enregistrments de la table ville
-- et les lignes de la table évoltion seront automatiquement supprimées.