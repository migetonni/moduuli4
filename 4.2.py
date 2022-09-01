

syötä_tuuma = float(input("Syötä tuuma"))
while syötä_tuuma >= -1:
    tuuma = syötä_tuuma * 2.54

    print(f"Muunnos on {tuuma} senttimetreinä ")
    if tuuma != "":
        syötä_tuuma = float(input("Syötä tuuma"))

    elif syötä_tuuma <= -1:
        break


