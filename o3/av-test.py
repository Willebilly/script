#!/usr/bin/env python3
import time
import platform
system = platform.system()

if system == "Windows":
    # Fortsätt med Windows-specifik kod
    print("Windows discovered. The script will continue..")
    directory_path = "C:/Users/willi/Documents/Wild virus/"
    the_file = "AV-TEST-NOT-DANGEROUS.txt"
    file_path = directory_path + the_file
    eicar_str = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
    try:
        with open(file_path, "a") as f:
            f.write(eicar_str) # EICA innehållet är helt ofarligt och kommer inte att skada systemet.
        time.sleep(3)          # Väntar några sekunder på AV/EDR respons.
        with open(file_path, "r") as f:
            file_content = f.read()
            if file_content == eicar_str: # Kontrollerar att innehåll matchar EICAR-signaturen.
                # LALALA
                print("Everything went accordingly!")
    except Exception as e:
        # Om ett fel uppstår här pga att filen har tagits bort eller flyttats
        print("[!!!] File could not be read!")
        print("[!!!] AV has removed/quarantined the file.")
        print("[---] Your AV/EDR-solution  is functional and gaurds against known virus-signatures.")

elif system == "Linux":
    print("Linux discovered. This script is meant for Windows.")
    exit

elif system == "Darwin":
    print("macOS discovered. This script is meant for Windows.")
    exit

else:
    print(f"Unknown OS ({system}) discovered. This script is meant for Windows.. Aborting.")
    exit
