import requests
import pandas as pd
import time

def query_search(query:str,n_records=10,subj=''):
    """

    This function executes a query on scoopus database and return it's result.

    Args:
        query (string]): query that will be made on scoopus database.
        n_records (int, optional): How many records will be searched by page. Defaults to 10.
        subj (str, optional): The subject filter for the query. Defaults to ''.

    Returns:
        [json]: query return
    """

    base_url = 'https://api.elsevier.com/content/search/scopus?query='
    final_url = base_url + query
    final_url += subj
    final_url += f'&apiKey={API_KEY}&count={n_records}&httpAccept=application/json&cursor=*'
    data = requests.get(final_url).json()
    return data

def get_scopus_id(query:str,n_records:int=10):
    """
    Responsible for getting the ids of the N papers returned by a query search

    Args:
        query (str): query
        n_records How many records will be searched by page. Defaults to 10.
    """

    data = query_search(query,n_records)
    print(data["search-results"]['opensearch:totalResults'])
    next_page = data["search-results"]["link"][2]["@href"]

    while next_page:
        scoopus_id = [id["dc:identifier"] for id in data["search-results"]["entry"]]
        next_page = data["search-results"]["link"][2]["@href"]
        scoopus_id_clean = [
            str(id).replace('SCOPUS_ID:','') 
            for id in scoopus_id
        ]
        with open('ids.csv', "a") as id_frame:
            for id in scoopus_id_clean:
                id_frame.write(f'{id},\n')

        data = requests.get(next_page).json()
        print('Making progress ----->')

def get_abstract(id:str):
    """[summary]

    Args:
        id (str): id of the desired paper

    Returns:
        [json]: returns the infomations about the paper
    """
    url = f'https://api.elsevier.com/content/abstract/scopus_id/{id}?httpAccept=application/json&apiKey={API_KEY}'
    data = requests.get(url).json()
    return data

query = 'TITLE-ABS-KEY ( temperature  OR  rain*  OR  precipitat*  OR  warm*  OR  summer  OR  winter  OR  spring  OR  autumn  OR  meteorolog*  OR  weather  OR  forecast*  OR  humidit*  OR  wave  OR  wind  OR  tide*  OR  "ocean current"  OR  "maritime current"  OR  "sea current"  OR  season*  OR  climat*  OR  drought  OR  "El Nino"  OR  cooling  OR  heat* )  AND  TITLE-ABS-KEY ( "blue amazon"  OR  ( brazil*  W/3  ( coast*  OR  beach*  OR  "continental margin*"  OR  "exclusive economic zone"  OR  ocean*  OR  sea*  OR  shore  OR  marine*  OR  "atlantic ocean*"  OR  offshore  OR  island*  OR  maritime  OR  bay  OR  marine  OR  archipelago  OR  "continental shelf"  OR  estuar* ) )  OR  ( petrobras  AND  ( coast*  OR  beach*  OR  "continental margin*"  OR  "exclusive economic zone"  OR  ocean*  OR  sea*  OR  shore  OR  marine*  OR  "atlantic ocean*"  OR  offshore  OR  island*  OR  maritime  OR  bay  OR  marine  OR  archipelago  OR  "continental shelf"  OR  estuar* ) ) )  AND  ( LIMIT-TO ( SUBJAREA ,  "EART" )  OR  LIMIT-TO ( SUBJAREA ,  "ENVI" )  OR  LIMIT-TO ( SUBJAREA ,  "ENGI" )  OR  LIMIT-TO ( SUBJAREA ,  "ENER" )  OR  LIMIT-TO ( SUBJAREA ,  "MULT" )  OR  LIMIT-TO ( SUBJAREA ,  "PHYS" )  OR  LIMIT-TO ( SUBJAREA ,  "COMP" )  OR  LIMIT-TO ( SUBJAREA ,  "BUSI" )  OR  LIMIT-TO ( SUBJAREA ,  "MATH" )  OR  LIMIT-TO ( SUBJAREA ,  "ECON" )  OR  LIMIT-TO ( SUBJAREA ,  "DECI" ) )'
subj = '&subj="EART"%2ct%2c"ENVI"%2ct%2c"ENGI"%2ct%2c"ENER"%2ct%2c"MULT"%2ct%2c"PHYS"%2ct%2c"COMP"%2ct%2c"BUSI"%2ct%2c"MATH"%2ct%2c"ECON"%2ct%2c"DECI"%2ct'

get_scopus_id(query,subj)

obj = get_abstract('20044366781')
print(obj)



