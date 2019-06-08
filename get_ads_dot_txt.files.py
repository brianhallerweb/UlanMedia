import requests
import json
import sys
import os
import re

import pprint
pp=pprint.PrettyPrinter(indent=2)

def get_ads_dot_txt_files():
    
    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/ads.txt/ads.txt_list.txt', 'r') as file:
        domains = file.read().split("\n")


    domain_pattern = re.compile(r'(.*//)([a-zA-Z0-9.]*)')
    for domain in domains:
        if len(domain) > 0:
            try:
                res = requests.get(domain).text
                short_domain = domain_pattern.findall(domain)
                short_domain = list(short_domain[0])
                short_domain = short_domain[1]
                with open(f"./ads.txt_files/{short_domain}", "w") as file:
                   json.dump(res, file)
            except requests.exceptions.RequestException as e:
                print(e)


get_ads_dot_txt_files()


