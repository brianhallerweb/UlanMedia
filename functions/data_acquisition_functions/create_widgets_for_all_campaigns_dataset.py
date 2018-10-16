import json

def create_widgets_for_all_campaigns_dataset(campaigns, date_range):
    widgets_for_all_campaigns = {}

    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'/home/bsh/Documents/UlanMedia/data/widgets_for_one_campaign/{vol_id}_{date_range}_widgets_for_one_campaign_dataset.json', 'r') as file:
            data = json.load(file)
        for widget in data:
           if widget in widgets_for_all_campaigns:
               widgets_for_all_campaigns[widget]["clicks"] += data[widget]["clicks"]
               widgets_for_all_campaigns[widget]["cost"] += data[widget]["cost"]
               widgets_for_all_campaigns[widget]["revenue"] += data[widget]["revenue"]
               widgets_for_all_campaigns[widget]["leads"] += data[widget]["leads"]
               widgets_for_all_campaigns[widget]["sales"] += data[widget]["sales"]
           else:
               widgets_for_all_campaigns[widget] = data[widget]

    with open(f"../../data/widgets_for_all_campaigns/{date_range}_widgets_for_all_campaigns_dataset.json", "w") as file:
        json.dump(widgets_for_all_campaigns, file)
