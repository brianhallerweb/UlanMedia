import json
import re
import sys
from functions.misc.get_campaign_sets import get_campaign_sets 

def create_c_widgets_for_one_p_widget_dataset(p_widget, date_range):
    c_widgets_for_one_p_widget = {"metadata": {"mgid_start_date": "",
                                 "mgid_end_date": "",
                                 "vol_start_date": "",
                                 "vol_end_date": ""
                                },
                                 "data": {}
                                } 

    campaigns = get_campaign_sets()
    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'/home/bsh/Documents/UlanMedia/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            json_file = json.load(file)

        metadata = json_file["metadata"]
        data = json_file["data"]
    
        if not c_widgets_for_one_p_widget["metadata"]["mgid_start_date"]:
            c_widgets_for_one_p_widget["metadata"]["mgid_start_date"] = metadata["mgid_start_date"]
        if not c_widgets_for_one_p_widget["metadata"]["mgid_end_date"]:
            c_widgets_for_one_p_widget["metadata"]["mgid_end_date"] = metadata["mgid_end_date"]
        if not c_widgets_for_one_p_widget["metadata"]["vol_start_date"]:
           c_widgets_for_one_p_widget["metadata"]["vol_start_date"] = metadata["vol_start_date"]
        if not c_widgets_for_one_p_widget["metadata"]["vol_end_date"]:
           c_widgets_for_one_p_widget["metadata"]["vol_end_date"] = metadata["vol_end_date"]


        pattern = re.compile(r'\d*')
        for widget in data:
           extracted_p_widget = pattern.search(widget).group()
           if extracted_p_widget != p_widget:
               continue;
           if widget in c_widgets_for_one_p_widget:
               c_widgets_for_one_p_widget["data"][widget]["clicks"] += data[widget]["clicks"]
               c_widgets_for_one_p_widget["data"][widget]["cost"] += data[widget]["cost"]
               c_widgets_for_one_p_widget["data"][widget]["revenue"] += data[widget]["revenue"]
               c_widgets_for_one_p_widget["data"][widget]["leads"] += data[widget]["leads"]
               c_widgets_for_one_p_widget["data"][widget]["sales"] += data[widget]["sales"]
           else:
               c_widgets_for_one_p_widget["data"][widget] = data[widget]
               c_widgets_for_one_p_widget["data"][widget]["vol_id"] = metadata["vol_id"]
               c_widgets_for_one_p_widget["data"][widget]["mgid_id"] = metadata["vol_id"]
               c_widgets_for_one_p_widget["data"][widget]["max_lead_cpa"] = metadata["max_lead_cpa"]
               c_widgets_for_one_p_widget["data"][widget]["max_sale_cpa"] = metadata["max_sale_cpa"]

    with open(f"../../data/c_widgets_for_one_p_widget/{p_widget}_{date_range}_c_widgets_for_one_p_widget_dataset.json", "w") as file:
        json.dump(c_widgets_for_one_p_widget, file)
    
    print(json.dumps(c_widgets_for_one_p_widget))

