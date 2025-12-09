#!/bin/bash
#
# Detta script samlar in systeminformation - RECON
#
# Kan användas för följande attacker:
# [Skriv möjliga attacker]
#
# Author: Frans Schartau
# Last Update: 2025-01-01
# För att allt ska sparas i utdata.txt skirv: ./info-script.sh > utdata.txt


echo "Välkommen till RECON script för att kontrollera en Linux-miljö"

echo
echo "=== SYSTEMINFO ==="
echo "=== OS, KERNEL, ARKITEKTUR ==="
uname -a
env
echo

echo
echo "=== AKTUELL ANVÄNDARE ==="
echo $USER
echo

echo
echo "=== ANVÄNDARE MED SHELL ==="
grep "sh$" /etc/passwd
lslogin #Rolig User info :)
echo

echo
echo "=== NÄTVERK ==="
ip a | grep inet
curl https://ipapi.co/json/
echo

echo
echo "=== HÅRDVARA  ==="
lscpu
free -h
echo

