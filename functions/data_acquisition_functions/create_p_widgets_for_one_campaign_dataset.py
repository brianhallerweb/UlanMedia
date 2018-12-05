import json
import re

def create_p_widgets_for_one_campaign_dataset(vol_id, date_range):
    p_widgets_for_one_campaign = {}

    with open(f'/home/bsh/Documents/UlanMedia/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
       data = json.load(file)

    pattern = re.compile(r'\d*')
    for widget in data:
       parent_widget = pattern.search(widget).group()
       if parent_widget in p_widgets_for_one_campaign:
           p_widgets_for_one_campaign[parent_widget]["clicks"] += data[widget]["clicks"]
           p_widgets_for_one_campaign[parent_widget]["cost"] += data[widget]["cost"]
           p_widgets_for_one_campaign[parent_widget]["revenue"] += data[widget]["revenue"]
           p_widgets_for_one_campaign[parent_widget]["leads"] += data[widget]["leads"]
           p_widgets_for_one_campaign[parent_widget]["sales"] += data[widget]["sales"]
       else:
           p_widgets_for_one_campaign[parent_widget] = data[widget]
           p_widgets_for_one_campaign[parent_widget]["widget_id"] = parent_widget

    with open(f"../../data/p_widgets_for_one_campaign/{vol_id}_{date_range}_p_widgets_for_one_campaign_dataset.json", "w") as file:
        json.dump(p_widgets_for_one_campaign, file)
