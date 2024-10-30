# Challenge : Système de Gestion de Projets TaskMaster

La startup **TaskMaster** souhaite développer un système de gestion de projets innovant qui s'intègre directement avec Discord. En tant que développeur principal, vous êtes chargé de créer cette application from scratch, en utilisant les technologies modernes et en suivant les meilleures pratiques de développement.

[Cahier des charges](./CDC.md)

## Technologies utilisées

- GitHub
- Python
- Flask
- SQL (PostgreSQL)
- Go
- Discord API

## Énoncés

- [Jour 1 : Introduction à la gestion de projet avec GitHub](./énoncés/J01.md)
- [Jour 2 : Fondamentaux du Backend et Création d'API avec Flask](./énoncés/J02.md)
- [Jour 3 : SQL et psql pour DevOps](./énoncés/J03.md)
- [Jour 4 : Gestion avancée des bases de données et ORM](./énoncés/J04.md)


## Cheatsheet PostgreSQL 

```bash
cd taskmaster/api
docker compose up -d mypgdb
docker exec -it api-mypgdb-1 bash
# je me connecte à la DB de nom taskmgr et l'utilisateur pguser avec la commande psql 
psql -U pguser taskmgr

```

Commandes postgresql intéressantes: 
```
# une fois dans le shell pgsql, on utilise les commandes spécifiques à postgresql
# lister les base de données
\l  
# lister les commandes disponible
\?
# je quitte le shell postgresql proprement
\q


```

```bash
psql -U pguser taskmgr
```

```
# lister les utilisateurs de la base de données 
\du
# liste les infos reative à un utilisateur
\du <user>
\du pguser

# se connecter à un base de données
\c <db>
\c taskmgr
# une fois connecté à une db, on peut lister les tables
\dt 
```

```sql
CREATE TABLE "users" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

```
# on peut lister les informations spécifiques à une table
\d <table>
\d users
```

```sql
INSERT INTO "users" (username) VALUES ('alice');
INSERT INTO "users" (username) VALUES ('bob');
INSERT INTO "users" (username) VALUES ('charlie');
INSERT INTO "users" (username) VALUES ('diana');
INSERT INTO "users" (username) VALUES ('eve');

SELECT * FROM users;

TRUNCATE users;
SELECT * FROM users;

INSERT INTO "users" (username) VALUES ('alice');
INSERT INTO "users" (username) VALUES ('bob');
INSERT INTO "users" (username) VALUES ('charlie');
INSERT INTO "users" (username) VALUES ('diana');
INSERT INTO "users" (username) VALUES ('eve');

SELECT * FROM users;
```

# Correction Exercice 1 Projets:  

```sql
CREATE TABLE "projets" (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    date_debut DATE NOT NULL,
    status VARCHAR(50) NOT NULL,
    
);
\dt
\d projets
INSERT INTO projets (nom, date_debut, status) VALUES ('Faire des cookies pour la promo', '2024-10-20', 'En cours');
INSERT INTO projets (nom, date_debut, status) VALUES ('Cook cookies', '2024-08-10', 'Terminé');
INSERT INTO projets (nom, date_debut, status) VALUES ('zut,Le grand projet pas si grand', '2024-05-03', 'Encours');

SELECT * FROM projets;
SELECT * FROM projets WHERE status = 'En cours';

ALTER TABLE projets ADD COLUMN id_responsable INTEGER;  (## Correction Exercice 2 Projets:)
UPDATE projets SET id_responsable = 1;
UPDATE projets SET id_responsable = 1 WHERE nom = 'Faire des cookies pour la promo';
UPDATE projets SET id_responsable = 1 WHERE id = 2;
UPDATE projets SET id_responsable = 2 WHERE id = 3;
UPDATE projets SET id_responsable = 1 WHERE id = 4;

                                    (## Correction Exercice 2 Projets:)

CREATE TABLE employes (id SERIAL PRIMARY KEY, nom VARCHAR(100) NOT NULL);
\dt
\d employes
INSERT INTO employes (nom) VALUES ('Alice');
INSERT INTO employes (nom) VALUES ('Bob');
INSERT INTO employes (nom) VALUES ('Charlie');
INSERT INTO employes (nom) VALUES ('Delta');
INSERT INTO employes (nom) VALUES ('Echo');
select * from employes;

SELECT projets.nom AS nom_projet, employes.nom AS nom_responsable_projet FROM projets JOIN employes ON projets.id_responsable = employes.id;

                                    (## Correction Exercice  Projets:)

ALTER TABLE employes ADD COLUMN salaire NUMERIC(10,2);
\d employes
UPDATE employes SET salaire = 35000 WHERE nom = 'Alice'; 
UPDATE employes SET salaire = 30000 WHERE nom = 'Bob';
UPDATE employes SET salaire = 45000 WHERE nom = 'Charlie';
UPDATE employes SET salaire = 50000 WHERE nom = 'Delta';
UPDATE employes SET salaire = 80000 WHERE nom = 'Echo';
SELECT * FROM employes;
SELECT * FROM employes WHERE salaire IS NULL;
SELECT * FROM employes WHERE salaire IS NOT NULL;

-- afficher le salaire moyen des employes (exercice 3.1)
SELECT AVG(salaire) AS salaire_moyen FROM employes;
-- nombre de projets par status  (exercice 3.2)
SELECT status, COUNT(*) FROM projets GROUP BY status; 
-- nom du projet le plus récent (exercice 3.3)
SELECT nom AS nom_projet FROM projets WHERE date_debut = (SELECT MAX(date_debut) FROM projets);


-- backup de la base de données de nom taskmgr
pg_dump -U pguser -d taskmgr > backup.sql
-- je me reconnecte a la DB, drop, puis crée une nouvelle qui est vide 
psql -U pguser postgres
DROP DATABASE taksmgr;
CREATE DATABASE taksmgr; 
\q
psql -U pguser -d taskmgr < backup.sql 

psql -U pguser -d taskmgr

```
# Correction exercices 3

On reprends from scratch : 
```bash
docker compose up -d mypgdb
docker ps
docker exec -it api-mypgdb-1 bash
```
Une fois dans le conteneur : 
```
psql -U pguser -d postgres
CREATE DATABASE devops_db;
\c devops_db;
CREATE TABLE applications (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, version VARCHAR(50) NOT NULL, last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
\dt 
\d applications

INSERT INTO applications (name, version) VALUES ('App Calculator 3000', 'v1.0.10');
INSERT INTO applications (name, version) VALUES ('App Machine a Cookie', 'v2.0.1');
INSERT INTO applications (name, version) VALUES ('App Slack', 'v1.5.0');

select * from applications;

select * from applications where version like 'v1%';

```


```bash
echo -e "\\\echo 'Nombre d enregistrements dans la table' \n SELECT COUNT(*) FROM :name; " > count_records.sql
cat count_records.sql

psql -U pguser -d devops_db;
# execute le fichier count_records.sql
\i count_records.sql

\set name 'applications'
\i count_records.sql
```

Exercice 3: 
```bash
# backup de la base de données de nom taskmgr
pg_dump -U pguser -d devops_db > backup_devops_db.sql
# pour afficher le contenu d'un fichier dans le terminal je peux utiliser 
# la commande cat 
cat backup_devops_db.sql
# je me reconnecte a la DB, drop, puis crée une nouvelle qui est vide 
psql -U pguser postgres
DROP DATABASE devops_db;
\l
CREATE DATABASE devops_db; 
\c devops_db;
\dt
\q
# on restore notre base de données 
psql -U pguser -d devops_db < backup_devops_db.sql
# on se reconnecte pour vérifier que c'est bien le cas
psql -U pguser -d devops_db
\dt 
select * from applications;
``` 