# S04-Demo

Repo pour la démo d'une API REST simple en Flask.  

## Cheatsheet Docker

```bash
# je démarre les conteneurs présents dans mon fichier compose.yaml
# attention : il faut s'être placé dans le répertoire contnenant le fichier
# compose.yaml au préalable. 
# -d: signifie en arrière plan (ne monopolise pas notre terminal courant)
docker compose up -d
# je me "téléporte" dans mon conteneur
docker exec -it s04-demo-pythonapp-1 /bin/bash
# le shell change et m'affiche 
# root@<un identifiant>
# signifiant que l'on est désormais dans le conteneur 
```

Dans le conteneur : 
```bash
cd /rel
pip install -r requirements.txt
flask run

# on peut alors ouvrir un autre terminal, se placer dans le conteneur
# (si VsCode s'entête à vouloir faire du port-forwarding) 
# et lancer la commande suivante pour réaliser une requête HTTP
curl -X GET http://localhost:5000/api/users
# []
curl -X POST http://localhost:5000/api/users -H "Content-Type: application/json" --data '{"username": "superuser"}'
# {"created_at":"2024-10-29T11:07:08.109842","id":1,"updated_at":"2024-10-29T11:07:08.109849","username":"superuser"} 
curl -X GET http://localhost:5000/api/users
# [{"created_at":"2024-10-29T11:07:08.109842","id":1,"updated_at":"2024-10-29T11:07:08.109849","username":"superuser"}]
```

# Corection du challenge *API REST simple en Flask*.

# Getting Started 

```bash
# Je me place dans le répertoire qui contient mon fichier compose.yaml
cd taskmaster/api
# Je lance le conteneur python avec docker compose 
docker compose up -d 
# Une fois mon conteneur démarré, je peux récupérer l'id et le nom avec la commande docker ps 
docker ps 
# J'ouvre un shell dans mon conteneur (je me place dans mon conteneur)
docker exec -it api-pythonapp-1 bash
# Une fois dans mon conteneur : le shell change je vois alors le début de ligne qui commence 
# par quelque chose du style root@3528b55c47d0 
```

**Une fois dans mon conteneur**: 
```bash
# Je me place dans le répertoire qui contient mon code Python
cd /rel
# J'installe les dépendances 
pip install -r requirements.txt
# Je lance mon application 
flask run --host=0.0.0.0

# Dans un terminal, je me place également dans le conteneur
docker exec -it api-pythonapp-1 bash
curl -X GET http://localhost:5000/api/tasks
curl -X POST http://localhost:5000/api/tasks -H "Content-Type: application/json" --data '{"title": "title1", "description": "description1"}'
curl -X POST http://localhost:5000/api/tasks -H "Content-Type: application/json" --data '{"title": "title2", "description": "description2"}'
curl -X GET http://localhost:5000/api/tasks/2
curl -X PUT http://localhost:5000/api/tasks/2 -H "Content-Type: application/json" --data '{"title": "newtitle"}'
curl -X DELETE http://localhost:5000/api/tasks/1
```


 