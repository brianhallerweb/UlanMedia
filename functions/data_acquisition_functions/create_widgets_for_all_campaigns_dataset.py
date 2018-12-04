import json
import re
import sys

# old function from when widgets for all campaigns included parents and
# children
# def create_widgets_for_all_campaigns_dataset(campaigns, date_range):
    # widgets_for_all_campaigns = {}

    # for campaign in campaigns:
        # vol_id = campaign["vol_id"] 
        # with open(f'/home/bsh/Documents/UlanMedia/data/widgets_for_one_campaign/{vol_id}_{date_range}_widgets_for_one_campaign_dataset.json', 'r') as file:
            # data = json.load(file)

        # for widget in data:
           # if widget in widgets_for_all_campaigns:
               # widgets_for_all_campaigns[widget]["clicks"] += data[widget]["clicks"]
               # widgets_for_all_campaigns[widget]["cost"] += data[widget]["cost"]
               # widgets_for_all_campaigns[widget]["revenue"] += data[widget]["revenue"]
               # widgets_for_all_campaigns[widget]["leads"] += data[widget]["leads"]
               # widgets_for_all_campaigns[widget]["sales"] += data[widget]["sales"]
           # else:
               # widgets_for_all_campaigns[widget] = data[widget]
        # sys.exit()

    # with open(f"../../data/widgets_for_all_campaigns/{date_range}_widgets_for_all_campaigns_dataset.json", "w") as file:
        # json.dump(widgets_for_all_campaigns, file)

def create_widgets_for_all_campaigns_dataset(campaigns, date_range):
    widgets_for_all_campaigns = {}

    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'/home/bsh/Documents/UlanMedia/data/widgets_for_one_campaign/{vol_id}_{date_range}_widgets_for_one_campaign_dataset.json', 'r') as file:
            data = json.load(file)

        pattern = re.compile(r'\d*')
        for widget in data:
           parent_widget = pattern.search(widget).group()
           if parent_widget in widgets_for_all_campaigns:
               widgets_for_all_campaigns[parent_widget]["clicks"] += data[widget]["clicks"]
               widgets_for_all_campaigns[parent_widget]["cost"] += data[widget]["cost"]
               widgets_for_all_campaigns[parent_widget]["revenue"] += data[widget]["revenue"]
               widgets_for_all_campaigns[parent_widget]["leads"] += data[widget]["leads"]
               widgets_for_all_campaigns[parent_widget]["sales"] += data[widget]["sales"]
           else:
               widgets_for_all_campaigns[parent_widget] = data[widget]
               widgets_for_all_campaigns[parent_widget]["widget_id"] = parent_widget

    with open(f"../../data/widgets_for_all_campaigns/{date_range}_widgets_for_all_campaigns_dataset.json", "w") as file:
        json.dump(widgets_for_all_campaigns, file)
