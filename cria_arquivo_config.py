import configparser
config = configparser.ConfigParser()
config['Primaris Intercessor Squad'] = {'role': {"Intercessor":{"M"       :6      ,
                                                                "WS"      :3      ,
                                                                "BS"      :3      ,
                                                                "S"       :4      ,
                                                                "T"       :4      ,
                                                                "W"       :2      ,
                                                                "A"       :2      ,
                                                                "Ld"      :7      ,
                                                                "Save"    :3      ,
                                                                "Ref"     :0
                                                                 }
                                                 ,"Intercessor Sergeant":{"M"       :6      ,
                                                                "WS"      :3      ,
                                                                "BS"      :3      ,
                                                                "S"       :4      ,
                                                                "T"       :4      ,
                                                                "W"       :2      ,
                                                                "A"       :2      ,
                                                                "Ld"      :8      ,
                                                                "Save"    :3      ,
                                                                "Ref"     :0
                                                                 }
                                                 }
                                        }

with open('units.ini', 'w') as configfile:
  config.write(configfile)
