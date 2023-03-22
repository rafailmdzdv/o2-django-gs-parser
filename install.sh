WORKDIR=`readlink -f .`

echo Installing poetry dependencies
poetry install

mkdir $WORKDIR/gs_parser/excel
mv $WORKDIR/.env.ex $WORKDIR/.env

echo Installing playwright drivers
poetry run playwright install
