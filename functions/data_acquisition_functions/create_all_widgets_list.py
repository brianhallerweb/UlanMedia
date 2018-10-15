import json

def create_all_widgets_list(campaigns, date_range):
    all_widgets = set()
    
    for campaign in campaigns:
        vol_id = campaign["vol_id"] 
        with open(f'/home/bsh/Documents/UlanMedia/data/widgets_for_one_campaign/{vol_id}_{date_range}_widgets_for_one_campaign_dataset.json', 'r') as file:
            data = json.load(file)
    
        for widget_id in data:
            all_widgets.add(widget_id)
    return list(all_widgets)

