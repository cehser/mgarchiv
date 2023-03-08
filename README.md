# Archiv der Maigesellschaft Derichsweiler

## Installation

### Download
```sh
git clone https://github.com/cehser/mgarchiv.git
```
### Konfiguration
```sh
cp .env.sample .env.prod
# Anschließend .env.prod anpassen!
```

### Build
```sh
docker compose up  --build
```

### Datenbank 
Zuletzt Datenbank db.sqlite3 ins Projekt-Verzeichnis kopieren oder neue Datenbank erzeugen via

```sh
docker compose run web python manage.py migrate
```
