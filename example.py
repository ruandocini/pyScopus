import requests
import pandas as pd
import time
import extractor as ext

query = 'TITLE-ABS-KEY ( temperature  OR  rain*  OR  precipitat*  OR  warm*  OR  summer  OR  winter  OR  spring  OR  autumn  OR  meteorolog*  OR  weather  OR  forecast*  OR  humidit*  OR  wave  OR  wind  OR  tide*  OR  "ocean current"  OR  "maritime current"  OR  "sea current"  OR  season*  OR  climat*  OR  drought  OR  "El Nino"  OR  cooling  OR  heat* )  AND  TITLE-ABS-KEY ( "blue amazon"  OR  ( brazil*  W/3  ( coast*  OR  beach*  OR  "continental margin*"  OR  "exclusive economic zone"  OR  ocean*  OR  sea*  OR  shore  OR  marine*  OR  "atlantic ocean*"  OR  offshore  OR  island*  OR  maritime  OR  bay  OR  marine  OR  archipelago  OR  "continental shelf"  OR  estuar* ) )  OR  ( petrobras  AND  ( coast*  OR  beach*  OR  "continental margin*"  OR  "exclusive economic zone"  OR  ocean*  OR  sea*  OR  shore  OR  marine*  OR  "atlantic ocean*"  OR  offshore  OR  island*  OR  maritime  OR  bay  OR  marine  OR  archipelago  OR  "continental shelf"  OR  estuar* ) ) )  AND  ( LIMIT-TO ( SUBJAREA ,  "EART" )  OR  LIMIT-TO ( SUBJAREA ,  "ENVI" )  OR  LIMIT-TO ( SUBJAREA ,  "ENGI" )  OR  LIMIT-TO ( SUBJAREA ,  "ENER" )  OR  LIMIT-TO ( SUBJAREA ,  "MULT" )  OR  LIMIT-TO ( SUBJAREA ,  "PHYS" )  OR  LIMIT-TO ( SUBJAREA ,  "COMP" )  OR  LIMIT-TO ( SUBJAREA ,  "BUSI" )  OR  LIMIT-TO ( SUBJAREA ,  "MATH" )  OR  LIMIT-TO ( SUBJAREA ,  "ECON" )  OR  LIMIT-TO ( SUBJAREA ,  "DECI" ) )'
subj = '&subj="EART"%2ct%2c"ENVI"%2ct%2c"ENGI"%2ct%2c"ENER"%2ct%2c"MULT"%2ct%2c"PHYS"%2ct%2c"COMP"%2ct%2c"BUSI"%2ct%2c"MATH"%2ct%2c"ECON"%2ct%2c"DECI"%2ct'

ext.get_scopus_id(query,subj)

obj = ext.get_abstract('20044366781')
print(obj)



