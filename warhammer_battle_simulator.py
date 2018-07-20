
for p in range(1):
    print("Partida", p)

    unidades = [{
        "unidade1": {
            "name": 'Primaris Intercessor Squad',
            'role': {
                "Intercessor": {
                    "M": 6,
                    "WS": 3,
                    "BS": 3,
                    "S": 4,
                    "T": 4,
                    "W": 2,
                    "A": 2,
                    "Ld": 7,
                    "Save": 3,
                    "Ref": 0,
                    "Qtd": 4,
                    "DamagePriority": 2,
                    "Weapons": {
                        "Bolt rifle": {
                            "Name": "Bolt rifle",
                            "Range": 30,
                            "Type": "Rapid Fire",
                            "S": 4,
                            "AP": -1,
                            "D": 1,
                            "Abilities": "",
                            "Ref": ""
                        }
                    }
                },
                "Intercessor Sergeant": {
                    "M": 6,
                    "WS": 3,
                    "BS": 3,
                    "S": 4,
                    "T": 4,
                    "W": 2,
                    "A": 2,
                    "Ld": 8,
                    "Save": 3,
                    "Ref": 0,
                    "Qtd": 1,
                    "DamagePriority": 1,
                    "Weapons": {
                        "Bolt rifle": {
                            "Name": "Bolt rifle",
                            "Range": 30,
                            "Type": "Rapid Fire",
                            "S": 4,
                            "AP": -1,
                            "D": 1,
                            "Abilities": "",
                            "Ref": ""
                        }
                    }
                }
            }
        },
        "unidade2": {
            "name": 'Oponente',
            'role': {
                "Oponente soldado": {
                    "M": 6,
                    "WS": 4,
                    "BS": 4,
                    "S": 4,
                    "T": 4,
                    "W": 2,
                    "A": 2,
                    "Ld": 7,
                    "Save": 3,
                    "Ref": 0,
                    "Qtd": 4,
                    "DamagePriority": 2,
                    "Weapons": {
                        "Bolt rifle": {
                            "Name": "Bolt rifle",
                            "Range": 30,
                            "Type": "Rapid Fire",
                            "S": 4,
                            "AP": -1,
                            "D": 1,
                            "Abilities": "",
                            "Ref": ""
                        }
                    }
                },
                "Oponente Sergeant": {
                    "M": 6,
                    "WS": 4,
                    "BS": 4,
                    "S": 4,
                    "T": 4,
                    "W": 2,
                    "A": 2,
                    "Ld": 8,
                    "Save": 3,
                    "Ref": 0,
                    "Qtd": 1,
                    "DamagePriority": 1,
                    "Weapons": {
                        "Bolt rifle": {
                            "Name": "Bolt rifle",
                            "Range": 30,
                            "Type": "Rapid Fire",
                            "S": 4,
                            "AP": -1,
                            "D": 1,
                            "Abilities": "",
                            "Ref": ""
                        }
                    }
                }
            }
        }

    }]
    unidade1 = unidades[0]["unidade1"]["role"]
    unidade2 = unidades[0]["unidade2"]["role"]

    for turno in range (6):
        print("\tTurno", turno)


        print("listando armas de ",  unidade1.keys())

        for i in unidade1:
            print(unidade1[i]["Weapons"])
                
        # pegar a maior liderança do grupo
        ld1 = max(int(i['Ld']) for i in unidade1.values())

        # pegar a maior DamagePriority
        pri1 = max(int(i['DamagePriority']) for i in unidade1.values() if i["Qtd"] > 0)
        #aplica baixas
        for i in unidade1:
            if unidade1[i]["DamagePriority"]==pri1:
                print(unidade1)
                unidade1[i]["Qtd"] -=1


        #print(unidades[0]["unidade1"],"liderança", ld )





    #somar
    #sum(int(i['Qtd']) for i in unidades[0]["unidade1"]["role"].values())

""" 
M
WS
BS
S
T
W
A
Ld
Save
Ref"""