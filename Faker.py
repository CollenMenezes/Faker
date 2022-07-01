#!/bin/python3

import random
import requests
import time
import os

tokens = ["1027|Ilt503Xop3YsrzmKn4sPhp0qgRR8dTcP","1026|QyWHiHrXq2zA0Xr8VX8eiv3iVjdSn2GO","1029|CJsTqd8HPbnKbVMhaBe2BDzaOIkJHqv7","1030|uvi0GjBl1XgoYuxa2ftGPumpQzAfwim9","1031|IJT47bKeNtsEdtiLOC6unqUep4Pj6e0q"]

_TOKEN_ = random.choice(tokens)


def main():
    
    class colors():
        bold = "\u001b[1m"
        green = "\u001b[32;1m"
        rt = "\u001b[0m"
        red = "\u001b[31;1m"

    def limpar():
        os.system("clear")

    def logo_off():
        limpar()
        print (f"{colors.red}{colors.bold}FFFFFFFFFFFFFFFFFFFFFF                  kkkkkkkk")
        print ("F::::::::::::::::::::F                  k::::::k")
        print ("F::::::::::::::::::::F                  k::::::k")
        print ("FF::::::FFFFFFFFF::::F                  k::::::k")
        print ("  F:::::F       FFFFFF  aaaaaaaaaaaaa    k:::::k    kkkkkkk    eeeeeeeeeeee    rrrrr   rrrrrrrrr")
        print ("  F:::::F               a::::::::::::a   k:::::k   k:::::k   ee::::::::::::ee  r::::rrr:::::::::r")
        print ("  F::::::FFFFFFFFFF     aaaaaaaaa:::::a  k:::::k  k:::::k   e::::::eeeee:::::eer:::::::::::::::::r")
        print ("  F:::::::::::::::F              a::::a  k:::::k k:::::k   e::::::e     e:::::err::::::rrrrr::::::r")
        print ("  F:::::::::::::::F       aaaaaaa:::::a  k::::::k:::::k    e:::::::eeeee::::::e r:::::r     r:::::r")
        print ("  F::::::FFFFFFFFFF     aa::::::::::::a  k:::::::::::k     e:::::::::::::::::e  r:::::r     rrrrrrr")
        print ("  F:::::F              a::::aaaa::::::a  k:::::::::::k     e::::::eeeeeeeeeee   r:::::r")
        print ("  F:::::F             a::::a    a:::::a  k::::::k:::::k    e:::::::e            r:::::r")
        print ("FF:::::::FF           a::::a    a:::::a k::::::k k:::::k   e::::::::e           r:::::r")
        print ("F::::::::FF           a:::::aaaa::::::a k::::::k  k:::::k   e::::::::eeeeeeee   r:::::r")
        print ("F::::::::FF            a::::::::::aa:::ak::::::k   k:::::k   ee:::::::::::::e   r:::::r")
        print (f"FFFFFFFFFFF             aaaaaaaaaa  aaaakkkkkkkk    kkkkkkk    eeeeeeeeeeeeee   rrrrrrr{colors.rt}\n")


    def logo():
        limpar()
        print (f"{colors.green}{colors.bold}FFFFFFFFFFFFFFFFFFFFFF                  kkkkkkkk")
        print ("F::::::::::::::::::::F                  k::::::k")
        print ("F::::::::::::::::::::F                  k::::::k")
        print ("FF::::::FFFFFFFFF::::F                  k::::::k")
        print ("  F:::::F       FFFFFF  aaaaaaaaaaaaa    k:::::k    kkkkkkk    eeeeeeeeeeee    rrrrr   rrrrrrrrr")
        print ("  F:::::F               a::::::::::::a   k:::::k   k:::::k   ee::::::::::::ee  r::::rrr:::::::::r")
        print ("  F::::::FFFFFFFFFF     aaaaaaaaa:::::a  k:::::k  k:::::k   e::::::eeeee:::::eer:::::::::::::::::r")
        print ("  F:::::::::::::::F              a::::a  k:::::k k:::::k   e::::::e     e:::::err::::::rrrrr::::::r")
        print ("  F:::::::::::::::F       aaaaaaa:::::a  k::::::k:::::k    e:::::::eeeee::::::e r:::::r     r:::::r")
        print ("  F::::::FFFFFFFFFF     aa::::::::::::a  k:::::::::::k     e:::::::::::::::::e  r:::::r     rrrrrrr")
        print ("  F:::::F              a::::aaaa::::::a  k:::::::::::k     e::::::eeeeeeeeeee   r:::::r")
        print ("  F:::::F             a::::a    a:::::a  k::::::k:::::k    e:::::::e            r:::::r")
        print ("FF:::::::FF           a::::a    a:::::a k::::::k k:::::k   e::::::::e           r:::::r")
        print ("F::::::::FF           a:::::aaaa::::::a k::::::k  k:::::k   e::::::::eeeeeeee   r:::::r")
        print ("F::::::::FF            a::::::::::aa:::ak::::::k   k:::::k   ee:::::::::::::e   r:::::r")
        print (f"FFFFFFFFFFF             aaaaaaaaaa  aaaakkkkkkkk    kkkkkkk    eeeeeeeeeeeeee   rrrrrrr{colors.rt}\n")

    def show_lan():
        logo()
        time.sleep(1)
        print (f"{colors.green}{colors.bold}[01] - RUSSIAN") #ru_RU
        print ("[02] - ENGLISH") #en_US
        print ("[03] - FRENCH") #fr_FR
        print ("[04] - GERMAN") #de_DE
        print ("[05] - SPANISH") #es_ES
        print ("[06] - ITALIAN") #it_IT
        print ("[07] - PORTUGUESE_BR") #pt_BR
        print ("[08] - PORTUGUESE_PT") #pt_T
        print (f"[00] - CLOSE{colors.rt}{colors.bold}")

    show_lan()

    """
    try:
        lang = int (input(f"\nCHOOSE A LANGUAGE: {colors.rt}"))
    except:
        logo()
        print (f"{colors.red}{colors.bold}[-] NUMBERS ONLY!{colors.rt}")
        time.sleep(3)
        main()
    """

    def choose_lang():
        global idioma
        lang = input(f"\nCHOOSE A LANGUAGE: {colors.rt}")

        if lang == "1" or lang == "01":
            idioma = "ru_RU"
        elif lang == "2" or lang == "02":
            idioma = "en_EN"
        elif lang == "3" or lang == "03":
            idioma = "fr_FR"
        elif lang == "4" or lang == "04":
            idioma = "de_DE"
        elif lang == "5" or lang == "05":
            idioma = "es_ES"
        elif lang == "6" or lang == "06":
            idioma = "it_IT"
        elif lang == "7" or lang == "07":
            idioma = "pt_BR"
        elif lang == "8" or lang == "08":
            idioma = "pt_PT"
        elif lang == "0" or lang == "00":
            logo_off()
            time.sleep(1)
            limpar()
            exit()
        else:
            logo_off()
            print (f"{colors.red}{colors.bold}[-] INVALID OPTION!{colors.rt}")
            time.sleep(3)
            main()

    choose_lang()
    
    def req():
        global data
        site = requests.get (f"https://api.invertexto.com/v1/faker?token={_TOKEN_}&locale={idioma}")
        data = site.json()


    def show_name():
        
        logo()
        print (f"{colors.bold}[-] GENERATING...{colors.rt}")
        time.sleep(2)
        req()
        logo()
        time.sleep(1)
        print (f"{colors.green}{colors.bold}[-] NAME SUCCESSFULLY GENERATED!{colors.rt}", data["name"])
        time.sleep(1)
        new_name = input(f"{colors.bold}\n[-] DO YOU WANT TO GENERATE ANOTHER NAME? (Y/N){colors.bold} ")
        if new_name == "y" or new_name == "Y":        
            show_name()
        elif new_name == "n" or new_name == "N":
            main()
        else:

            logo_off()
            time.sleep(1)
            print (f"{colors.red}{colors.bold}[-] INVALID OPTION!{colors.rt}")
            time.sleep (3)
            show_name()

    show_name()
    
main()
