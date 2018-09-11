# deptoon-reminder
Telegram bot receiving request from a lambda function

### Instructions
Assuming you have already installed Heroku and created a bot from `BotFather`
```
heroku create <HEROKU_APP_NAME>
heroku config:set TOKEN=<YOUR_TOKEN>
```
With this, you are ready to start your own bot. You can also add environment variables on the dashboard of your app (Settings > Config variables)

#### Adding Postgres :elephant:

```
heroku addons:create heroku-postgresql
```
Enter to [Heroku](www.heroku.com) to get the environment variables you need (Your app > Resources > Heroku Postgres :: Database > Settings > Database credentials)

If you want to access your database, you can do it with the following command:
```
heroku pg:psql
```

#### Docker
```
docker build -t flask-sample-one:latest .
docker run -p 5000:5000 --env-file ./.env -v ~/path/to/app:/app flask-sample-one
```

env file:
```
TOKEN=<YOUR_TOKEN>
DOMAIN=<YOUR_DOMAIN>
GROUP_ID=<YOUR_CHAT_ID>
BASE_URL=<DOMAIN>
```


Project based on [previous one](https://github.com/jicortes2/base_bot) made in collaboration of [Cristián Cortés](https://github.com/criscv94)
