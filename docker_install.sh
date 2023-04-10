echo Starting docker install...


read -p "Your postgres username from .env.ex?: " postgre_username
read -p "Your postgres password from .env.ex?: " postgre_password
read -p "Your postgres database name from .env.ex?: " postgre_db

sed -i 's/localhost/db/g' .env.ex
sed -i "s/user_template/$postgre_username/1" docker-compose.yml
sed -i "s/password_template/$postgre_password/1" docker-compose.yml
sed -i "s/db_template/$postgre_db/1" docker-compose.yml

docker compose up -d
echo Done.
