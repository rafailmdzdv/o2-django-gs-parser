WORKDIR=`readlink -f .`

echo Installing poetry dependencies
poetry install

mkdir $WORKDIR/gs_parser/excel
mv $WORKDIR/.env.ex $WORKDIR/.env

echo Installing playwright drivers
poetry run playwright install

poetry run python3.11 $WORKDIR/gs_parser/manage.py makemigrations
poetry run python3.11 $WORKDIR/gs_parser/manage.py migrate
