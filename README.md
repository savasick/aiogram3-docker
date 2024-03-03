# Aiogram3 - telegram bot within docker

<li>
aiogram - 3.3.0
</li>



### install

```bash
cp .env.example .env
```

insert token from <a href="https://telegram.me/BotFather">BotFather</a> to env file\
change .env file, also change create_fixtures.db with credentials


### usage
```bash
docker-compose up -d
```

<a href="http://localhost:8070">Adminer</a> for database managment

#

### insert user new entry to db for user access

```bash
USER=username
ID=1234567890

while IFS== read -r key value; do
    if [[ $key != \#* ]]; then
        export "$key"="$value"
    fi
done < .env 2>/dev/null

docker-compose exec db psql -h ${BOT_DATABASE_HOST} -U ${BOT_DATABASE_USER} -d ${BOT_DATABASE_NAME} -c "\
    INSERT INTO users (username, user_id) VALUES \
    ('${USER}', '${ID}');"
```