import json
import re

def create_p_widgets_for_one_campaign_dataset(vol_id, date_range):
    p_widgets_for_one_campaign = {"metadata": {"mgid_start_date": "",
                                 "mgid_end_date": "",
                                 "vol_start_date": "",
                                 "vol_end_date": ""
                                },
                                 "data": {}
                                } 

    with open(f'/home/bsh/Documents/UlanMedia/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
       json_file = json.load(file)

    metadata = json_file["metadata"]
    data = json_file["data"]
    
    p_widgets_for_one_campaign["metadata"] = metadata

    pattern = re.compile(r'\d*')
    for widget in data:
       parent_widget = pattern.search(widget).group()
       if parent_widget in p_widgets_for_one_campaign["data"]:
           p_widgets_for_one_campaign["data"][parent_widget]["clicks"] += data[widget]["clicks"]
           p_widgets_for_one_campaign["data"][parent_widget]["cost"] += data[widget]["cost"]
           p_widgets_for_one_campaign["data"][parent_widget]["revenue"] += data[widget]["revenue"]
           p_widgets_for_one_campaign["data"][parent_widget]["leads"] += data[widget]["leads"]
           p_widgets_for_one_campaign["data"][parent_widget]["sales"] += data[widget]["sales"]
       else:
           p_widgets_for_one_campaign["data"][parent_widget] = data[widget]
           p_widgets_for_one_campaign["data"][parent_widget]["widget_id"] = parent_widget

    with open(f"../../data/p_widgets_for_one_campaign/{vol_id}_{date_range}_p_widgets_for_one_campaign_dataset.json", "w") as file:
        json.dump(p_widgets_for_one_campaign, file)

    return json.dumps(p_widgets_for_one_campaign)
