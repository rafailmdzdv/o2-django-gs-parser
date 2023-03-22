WORKDIR=`readlink -f .`


echo Starting parser. After finish I will sleep for 10 seconds to start scheduler and API.
poetry run python3.11 $WORKDIR/gs_parser/manage.py startparser

echo Sleeping 10 seconds
sleep 10

echo Starting scheduler and API.
poetry run python3.11 $WORKDIR/gs_parser/manage.py runserver & poetry run python3.11 $WORKDIR/gs_parser/manage.py startschedule
