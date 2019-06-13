import requests
import json
import sys
import os
import re

# import pprint
# pp=pprint.PrettyPrinter(indent=2)

def create_widget_domain_lookup():
    
    widget_domain_lookup = {} 

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/widget_domain_list/widget_domain_list.txt', 'r') as file:
        widget_domain_list = file.read().split("\n")
    
    for widget_domain in widget_domain_list:
        if len(widget_domain) > 0:
            widget_id = widget_domain.split(",")[0]
            domain = widget_domain.split(",")[1]
            if widget_id in widget_domain_lookup:
                widget_domain_lookup[widget_id].append(domain)
            else:
                widget_domain_lookup[widget_id] = [domain]

    with open(f"../../data/widget_domain_lookup/widget_domain_lookup.json", "w") as file:
        json.dump(widget_domain_lookup, file)




