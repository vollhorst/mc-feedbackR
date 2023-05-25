#!/bin/bash
# 2023-05-25
# quelle(n):
# https://stackoverflow.com/questions/40192725/bash-script-store-cat-output-in-variable-and-then-echo-it
BEFEHL='pipenv run python py/bilderkennung.py'
JETZT=`date +"%Y%m%d"`
BILDER='pics/*.png'
ZIEL='txt'
NR_F='nrnr'
printf "befehl: $BEFEHL\n"
printf "datum: $JETZT\n"
printf "input: $BILDER\n"
printf "output: $ZIEL\n\n"

if [ -f "$NR_F" ]
then 
    NR_INT=$(< $NR_F)
    declare -i NR=$NR_INT
else
    declare -i NR=101
fi

for bild in $BILDER; do
    printf "# $BEFEHL $bild > $ZIEL/e$NR-$JETZT\n"
    $BEFEHL $bild > $ZIEL/e$NR\-$JETZT
    ((NR+=1))
done

echo $NR > $NR_F
printf "\nende.\n"
