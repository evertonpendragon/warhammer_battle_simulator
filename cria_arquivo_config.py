import configparser
config = configparser.ConfigParser()
config['Primaris Intercessor Squad'] = {'role': {"Intercessor":{"M"       :6,
                                                                "WS"      :3,
                                                                "BS"      :3,
                                                                "S"       :4,
                                                                "T"       :4,
                                                                "W"       :2,
                                                                "A"       :2,
                                                                "Ld"      :7,
                                                                "Save"    :3,
                                                                "Ref"     :0,
                                                                "Qtd"     :4,
                                                                "Prioridade":2
                                                                 }
                                                 ,"Intercessor Sergeant":{  "M"       :6,
                                                                            "WS"      :3,
                                                                            "BS"      :3,
                                                                            "S"       :4,
                                                                            "T"       :4,
                                                                            "W"       :2,
                                                                            "A"       :2,
                                                                            "Ld"      :8,
                                                                            "Save"    :3,
                                                                            "Ref"     :0,
                                                                            "Qtd"     :1,
                                                                            "Prioridade":1
                                                                             }
                                                 }
                                        }

with open('units.ini', 'w') as configfile:
  config.write(configfile)

