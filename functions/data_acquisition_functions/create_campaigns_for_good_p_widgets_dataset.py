from config.config import *
import os
import json

def create_campaigns_for_good_p_widgets_dataset(date_range):

    good_widgets = ["5753946", "5763287", "5763288", "5763289", "5763290", "5763291", "5763292", "5763293", "5763294", "5763295", "5763296",
    "5763297", "5763298", "5763299", "5763300", "5763301", "5763302",
    "5763303", "5763304", "5763305", "5763306", "5763307", "5765324",
    "5765326", "5765354", "5765355", "5765358", "5767281"]

    campaigns_for_good_p_widgets = []

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_p_widgets/{date_range}_complete_p_widgets_dataset.json', 'r') as file:
       data = json.load(file)

    for p_widget in data:
        if p_widget not in good_widgets:
            continue
        for campaign in data[p_widget]["for_each_campaign"]:
            campaigns_for_good_p_widgets.append(campaign)

    with open(f"../../data/campaigns_for_good_p_widgets/{date_range}_campaigns_for_good_p_widgets_dataset.json", "w") as file:
        json.dump(campaigns_for_good_p_widgets, file)

    return json.dumps(campaigns_for_good_p_widgets)
