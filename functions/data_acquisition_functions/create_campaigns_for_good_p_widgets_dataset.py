from config.config import *
import os
import json

def create_campaigns_for_good_p_widgets_dataset(date_range, max_rec_bid, default_coeff):
    max_rec_bid = float(max_rec_bid)
    default_coeff = float(default_coeff)

    good_widgets = ["34427", "5555245", "5577109", "5653511", "5662654", "5676558",
        "57009653", "57009654", "5718588", "5753116", "5753130", "5753946",
        "5763287", "5763288", "5763289", "5763290", "5763291", "5763292",
        "5763293", "5763294", "5763295", "5763296", "5763297", "5763298",
        "5763299", "5763300", "5763301", "5763302", "5763303", "5763304",
        "5763305", "5763306", "5763307", "5765324", "5765326", "5765354",
        "5765355", "5765358", "5767281"]

    campaigns_for_good_p_widgets = []

    with open(f'{os.environ.get("ULANMEDIAAPP")}/data/complete_p_widgets/{date_range}_complete_p_widgets_dataset.json', 'r') as file:
       data = json.load(file)

    for p_widget in data:
        if p_widget not in good_widgets:
            continue
        for campaign in data[p_widget]["for_each_campaign"]:
            campaign["global_status"] = data[p_widget]["for_all_campaigns"]["global_status"]
            campaign["domain"] = data[p_widget]["for_all_campaigns"]["domain"]
            campaigns_for_good_p_widgets.append(campaign)

    for campaign in campaigns_for_good_p_widgets:
        sales = campaign["sales"]
        mpl = campaign["mpl"]
        if campaign["leads"] > 0:
            cpl = campaign["cost"]/campaign["leads"]
        if campaign["clicks"] > 0:
            epc = campaign["revenue"]/campaign["clicks"]
        c_bid = campaign["c_bid"]
        w_bid = campaign["w_bid"]
        coeff = campaign["coeff"]

        if sales > 0:
            campaign["rec_w_bid"] = epc - epc * .3
        elif campaign["leads"] > 0:
            campaign["rec_w_bid"] = c_bid * mpl / cpl / 2
        else:
            campaign["rec_w_bid"] = c_bid * default_coeff

        if campaign["rec_w_bid"] > max_rec_bid:
            campaign["rec_w_bid"] = max_rec_bid

        campaign["rec_coeff"] = campaign["rec_w_bid"] / c_bid
        
        rec_w_bid = campaign["rec_w_bid"]
        rec_coeff = campaign["rec_coeff"]

        if w_bid != rec_w_bid:
            campaign["mismatch_w_bid_and_rec_w_bid"] = True
        else:
            campaign["mismatch_w_bid_and_rec_w_bid"] = False

        if coeff != rec_coeff:
            campaign["mismatch_coeff_and_rec_coeff"] = True
        else:
            campaign["mismatch_coeff_and_rec_coeff"] = False

        
    with open(f"../../data/campaigns_for_good_p_widgets/{date_range}_campaigns_for_good_p_widgets_dataset.json", "w") as file:
        json.dump(campaigns_for_good_p_widgets, file)

    return json.dumps(campaigns_for_good_p_widgets)
