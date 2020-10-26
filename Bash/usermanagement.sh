#!/bin/bash

for (( i=1; i<=$#; i++));
do
    if [[ ${!i} = "-r" ]]; then
        userdel -f EngGod420
        userdel -f EngMan420
        userdel -f EngWoman420
        userdel -f ISGod420
        userdel -f ISMan420
        userdel -f ISWoman420
        userdel -f SalesGod420
        userdel -f SalesMan420
        userdel -f SalesWoman420
        groupdel -f Sales
        groupdel -f Engineering
        groupdel -f IS
        echo "he be ressetiing it doe \*blushes"
        break;
    fi
done

cd /

groupadd -f IS
groupadd -f Sales
groupadd -f Engineering

if [ -d /IS ]; then
    rm -rf /IS
    mkdir -p /IS
    echo "deleted the existing IS folder and made a new one."
else
    mkdir /IS
    echo "no existing IS folder, made a new one."
fi


if [ -d /Sales ]; then
    rm -rf /Sales
    mkdir -p /Sales
    echo "deleted the existing Sales folder and made a new one."
else
    mkdir /Sales
    echo "no existing Sales folder, made a new one."
fi


if [ -d /Engineering ]; then
    rm -rf /Engineering
    mkdir -p /Engineering
    echo "deleted the existing Engineering folder and made a new one."
else
    mkdir /Engineering
    echo "no existing Engineering folder, made a new one."
fi

useradd EngGod420 -b /Engineering -g Engineering -G adm -s /bin/bash
if [ $? -eq 0 ]; then echo  "made group admin EngGod420"; fi
useradd ISGod420 -b /IS -g IS -G adm -s /bin/bash
if [ $? -eq 0 ]; then echo  "made group admin ISGod420"; fi
useradd SalesGod420 -b /Sales -g Sales -G adm -s /bin/bash
if [ $? -eq 0 ]; then echo  "made group admin SalesGod420"; fi

useradd EngMan420 -b /Engineering -g Engineering -s /bin/bash
if [ $? -eq 0 ]; then echo  "made user EngMan420"; fi
useradd EngWoman420 -b /Engineering -g Engineering -s /bin/bash
if [ $? -eq 0 ]; then echo  "made user EngWoman420"; fi


useradd ISMan420 -b /IS -g IS -s /bin/bash
if [ $? -eq 0 ]; then echo  "made user ISMan420"; fi
useradd ISWoman420 -b /IS -g IS -s /bin/bash
if [ $? -eq 0 ]; then echo  "made user ISWoman420"; fi

useradd SalesMan420 -b /Sales -g Sales -s /bin/bash
if [ $? -eq 0 ]; then echo  "made user SalesMan420"; fi
useradd SalesWoman420 -b /Sales -g Sales -s /bin/bash
if [ $? -eq 0 ]; then echo  "made user SalesWoman420"; fi



echo “This file contains confidential information for the department.” > /IS/Policy.txt
echo “This file contains confidential information for the department.” > /Engineering/Policy.txt
echo “This file contains confidential information for the department.” > /Sales/Policy.txt

echo "policies created"

chown -R ISGod420:IS /IS
chown -R EngGod420:Engineering /Engineering
chown -R SalesGod420:Sales /Sales
chmod -R 1770 /IS
chmod -R 1770 /Engineering
chmod -R 1770 /Sales

echo "proper ownership modified"