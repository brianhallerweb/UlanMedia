import requests
import json
import sys
import os
import re

import pprint
pp=pprint.PrettyPrinter(indent=2)

def create_widget_domain_lookup():
    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/domains_list/mgid_ads_dot_txt.txt', 'r') as file:
        domains = file.read().split("\n")
    
    widget_domain_lookup = {} 

    # domains = []
    domain_pattern = re.compile(r'(.*//)([a-zA-Z0-9.]*)')
    # for full_domain in full_domains:
        # res = domain_pattern.findall(full_domain)
        # if len(res) > 0:
            # domain = res[0]
            # domains.append(domain)

    n = 1
    for domain in domains:
        if len(domain) > 0:
            res = requests.get(domain).text
            lines = res.split("\n")
            for line in lines:
                row = line.split(", ")
                if len(row) >= 2: 
                    traffic_source = row[0]
                    if traffic_source == "mgid.com":
                        widget_id = row[1]
                        res = domain_pattern.findall(domain)
                        if len(res) > 0:
                            res = list(res[0])
                            domain = res[1]
                            widget_domain_lookup[widget_id] = domain

        n += 1
        if n > 50:
            break
            # pp.pprint(widget_domain_lookup)

    with open(f"../../data/widget_domain_lookup/widget_domain_lookup.json", "w") as file:
        json.dump(widget_domain_lookup, file)


