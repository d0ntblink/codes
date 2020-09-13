#!/bin/bash

folder="~/rhymes"
file="JackAndJill.txt"
save="index.html"
j=USER


cd ~

if [ -d ~/rhymes ]; then
    rm -rf ~/rhymes
    mkdir -p ~/rhymes
    echo "deleted the existing rhymes folder and made a new one."
else
    mkdir ~/rhymes
    echo "no existing rhymes folder, made a new one."
fi

cd ~/rhymes

wget https://raw.githubusercontent.com/chriswiebe/ACIT2420/master/JackAndJill.txt | echo "downloading JackAndJill.txt"

if [[ $# -lt 1 ]]; then
    echo 'this is the help menu cause you messed up and gave me nothing to work with'
    echo './amuseme.sh [OPTION] [ARGUMENT1] [ARGUMENT2]'
    echo 'OPTIONS:'
    echo '-u : custom username for Jill (default is the current username)'
    echo '-x : open the html file in firefox (need to have firefox already installed)'
fi

for (( i=1; i<=$#; i++));
do
    if [[ ${!i} = "-u" ]]; then
        j=$((i+1))
        echo "found option -u, replacing Jill with \"${!j}\"."
        break;
    fi
done

for (( i=1; i<=$#; i++));
do
    if [[ ! ${!i} = "-"* ]] && [[ ! ${!i} = ${!j} ]]; then
        c=$((i))
        break;
    fi
done

for (( i=1; i<=$#; i++));

do
    if [[ ! ${!i} = "-"* ]] && [[ ! ${!i} = ${!j} ]] && [[ ! ${!i} = ${!c} ]]; then
        v=$((i))
        break;
    fi
done

if [ -z "${!c}" ] && [ -z "${!v}" ]; then
    sed "s/Jill/${!j}/g" $file > $save;
elif [ ! -z "${!c}" ] && [ -z "${!v}" ]; then
    sed -e "s/crown,/${!c},/g" -e "s/Jill/${!j}/g" $file > $save;
    echo "replacing crown with \"${!c}\""
else
    sed -e "s/crown,/${!c},/g" -e "s/vinegar/${!v}/g" -e "s/Jill/${!j}/g" $file > $save;
    echo "replacing crown with \"${!c}\" and vinegar with \"${!v}\"."
fi

if [[ $@ = *"-x"* ]]; then
    firefox index.html;
fi