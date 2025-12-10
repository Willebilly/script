
Jag har lärt mig om hash och hur MD5 fungerar för att kryptera lösenord. 
Att om lösenordet bara ex är siffror och inte tillräckligt lång så är
det lätt att käcka med rainbow tables som crackstation.

Jag har pilat med en kod för att generera samt hasha lösenord.
Jag har pilat med en kod för att cracka hashade lösenord.

Det var kul! :D

md5-hasher.py används för att generera 10st lösenord med, (9), siffror mellan 0-9 som sedan hashas med MD5.
md5-hascat.sh används för att knäcka de 10 hashen och genererar vad de ursprungligen var.
