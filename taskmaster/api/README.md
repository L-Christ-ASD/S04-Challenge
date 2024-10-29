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