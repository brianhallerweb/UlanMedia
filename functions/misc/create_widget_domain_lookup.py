import requests
import json
import sys
import os
import re

import pprint
pp=pprint.PrettyPrinter(indent=2)

def create_widget_domain_lookup():
    
    widget_domain_lookup = {} 

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/vol_widget_domain_list/vol_widget_domain_list.txt', 'r') as file:
        widget_domain_list = file.read().split("\n")
    
    for widget_domain in widget_domain_list:
        if len(widget_domain) > 0:
            widget_id = widget_domain.split(",")[0]
            domain = widget_domain.split(",")[1]
            if widget_id in widget_domain_lookup:
                widget_domain_lookup[widget_id].append(domain)
            else:
                widget_domain_lookup[widget_id] = [domain]

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/ads.txt/ads.txt_list.txt', 'r') as file:
        domains = file.read().split("\n")

    # fake user agent
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    domain_pattern = re.compile(r'(.*//)([a-zA-Z0-9.]*)')
    for domain in domains:
        if len(domain) > 0:
            try:
                res = requests.get(domain, headers=headers).text
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
                                if widget_id in widget_domain_lookup:
                                    widget_domain_lookup[widget_id].append(domain)
                                else:
                                    widget_domain_lookup[widget_id] = [domain]
            except requests.exceptions.RequestException as e:
                print(e)

    with open(f"../../data/widget_domain_lookup/widget_domain_lookup.json", "w") as file:
        json.dump(widget_domain_lookup, file)

#this was my attempt at using the saved ads.txt data
# def create_widget_domain_lookup():

    # widget_domain_lookup = {} 

    # with open(f'{os.environ.get("ULANMEDIAAPP")}/data/vol_widget_domain_list/vol_widget_domain_list.txt', 'r') as file:
        # widget_domain_list = file.read().split("\n")
    
    # for widget_domain in widget_domain_list:
        # if len(widget_domain) > 0:
            # widget_id = widget_domain.split(",")[0]
            # domain = widget_domain.split(",")[1]
            # if widget_id in widget_domain_lookup:
                # widget_domain_lookup[widget_id].append(domain)
            # else:
                # widget_domain_lookup[widget_id] = [domain]

    # with open(f'{os.environ.get("ULANMEDIAAPP")}/data/ads.txt/ads.txt_list.txt', 'r') as file:
        # domains = file.read().split("\n")

    # domain_pattern = re.compile(r'(.*//)([a-zA-Z0-9.]*)')
    # for domain in domains:
        # if len(domain) > 0:
            # try:
                # res = domain_pattern.findall(domain)
                # res = list(res[0])
                # short_domain = res[1]
                # print(short_domain)
                # with open(f'{os.environ.get("ULANMEDIAAPP")}/ads.txt_files/{short_domain}', 'r') as file:
                    # res = file.read().split("\n")
                # lines = res.split("\n") 
                # print(lines)
            # except:
                # print("error")

    # with open(f"../../data/widget_domain_lookup/widget_domain_lookup.json", "w") as file:
        # json.dump(widget_domain_lookup, file)



