from config.config import *
import os
import json

def create_campaigns_for_good_p_widgets_dataset(date_range, max_recommended_bid, default_coefficient):
    max_recommended_bid = float(max_recommended_bid)
    default_coefficient = float(default_coefficient)

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
            campaign["global_status"] = data[p_widget]["for_all_campaigns"]["global_status"]
            # 5/31/19 campaign bid isn't supposed to be mpc but it is for now.
            # Mike hasn't decided how to calculate mpc properly.
            campaign["campaign_bid"] = campaign["mpc"]
            campaign["widget_bid"] = round(campaign["campaign_bid"] * campaign["bid_coefficient"], 2)
            campaigns_for_good_p_widgets.append(campaign)

    for campaign in campaigns_for_good_p_widgets:
        sales = campaign["sales"]
        mpl = campaign["mpl"]
        if campaign["leads"] > 0:
            cpl = campaign["cost"]/campaign["leads"]
        epc = campaign["revenue"]/campaign["clicks"]
        campaign_bid = campaign["campaign_bid"]
        widget_bid = campaign["widget_bid"]
        bid_coefficient = campaign["bid_coefficient"]

        if sales > 0:
            campaign["recommended_widget_bid"] = round(epc - epc * .3, 2)
        elif campaign["leads"] > 0:
            campaign["recommended_widget_bid"] = round(campaign_bid * mpl / cpl /
                    2, 2)
        else:
            campaign["recommended_widget_bid"] = round(campaign_bid * default_coefficient, 2)

        if campaign["recommended_widget_bid"] > max_recommended_bid:
            campaign["recommended_widget_bid"] = max_recommended_bid

        campaign["recommended_coefficient"] = round(campaign["recommended_widget_bid"] / campaign_bid, 0)

    for campaign in campaigns_for_good_p_widgets:
        widget_bid = campaign["widget_bid"]
        bid_coefficient = campaign["bid_coefficient"]
        recommended_widget_bid = campaign["recommended_widget_bid"]
        recommended_coefficient = campaign["recommended_coefficient"]

        if widget_bid != recommended_widget_bid:
            campaign["mismatch_bid_and_rec_bid"] = True
        else:
            campaign["mismatch_bid_and_rec_bid"] = False

        if bid_coefficient != recommended_coefficient:
            campaign["mismatch_coeff_and_rec_coeff"] = True
        else:
            campaign["mismatch_coeff_and_rec_coeff"] = False
        
    with open(f"../../data/campaigns_for_good_p_widgets/{date_range}_campaigns_for_good_p_widgets_dataset.json", "w") as file:
        json.dump(campaigns_for_good_p_widgets, file)

    return json.dumps(campaigns_for_good_p_widgets)
