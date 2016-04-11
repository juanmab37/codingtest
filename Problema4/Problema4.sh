#!/bin/bash 

#Baruffaldi Juan Manuel

#Se requiere esta libreria
sudo apt-get install whois

#Transformamos la lista de nombres segun las condiciones dadas
awk '{ if(length($1) <= 6){ print $1} }' NamesAll.txt > NamesAll_reduc.txt

#La 1er linea esta codificada con DES
./crackdes.sh ox ox45K6RsEUfmQ NamesAll_reduc.txt
#Decrypted password is: fido

#La 2da linea esta codificada con md5
./crackmd5.sh 42dJ1xYh MfrRke8/Ej3h5.vMtNEhC. Colours.txt
#Decrypted password is: white

#La 3er linea esta codificada con SHA512
python Problem4.py equipos.txt shadow.txt
#Found password: knicks
