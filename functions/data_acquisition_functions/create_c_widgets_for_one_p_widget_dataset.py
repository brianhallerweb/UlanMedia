import json
import re
import sys

# you are still working on this but it looks good to me.
def create_c_widgets_for_one_p_widget_dataset(campaigns, date_range, p_widget):
    c_widgets_for_one_p_widget = {}

    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'/home/bsh/Documents/UlanMedia/data/p_and_c_widgets_for_one_campaign/{vol_id}_{date_range}_p_and_c_widgets_for_one_campaign_dataset.json', 'r') as file:
            data = json.load(file)

        pattern = re.compile(r'\d*')
        for widget in data:
           extracted_p_widget = pattern.search(widget).group()
           if extracted_p_widget != p_widget:
               break;
           if widget in c_widgets_for_one_p_widget:
               c_widgets_for_one_p_widget[widget]["clicks"] += data[widget]["clicks"]
               c_widgets_for_one_p_widget[widget]["cost"] += data[widget]["cost"]
               c_widgets_for_one_p_widget[widget]["revenue"] += data[widget]["revenue"]
               c_widgets_for_one_p_widget[widget]["leads"] += data[widget]["leads"]
               c_widgets_for_one_p_widget[widget]["sales"] += data[widget]["sales"]
           else:
               c_widgets_for_one_p_widget[widget] = data[widget]

    with open(f"../../data/c_widgets_for_one_p_widget/{date_range}_{p_widget}_c_widgets_for_one_p_widget_dataset.json", "w") as file:
        json.dump(c_widgets_for_one_p_widget, file)
