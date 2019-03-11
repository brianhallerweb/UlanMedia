def classify_p_widget_for_all_campaigns(p_widget):
    global_status = p_widget["for_all_campaigns"]["global_status"]
    clicks = p_widget["for_all_campaigns"]["clicks"] 
    cost = p_widget["for_all_campaigns"]["cost"]
    revenue = p_widget["for_all_campaigns"]["revenue"]
    leads = p_widget["for_all_campaigns"]["leads"]
    profit = revenue - cost
    good_campaigns_count = p_widget["good_campaigns_count"]
    bad_campaigns_count = p_widget["bad_campaigns_count"]
    not_yet_campaigns_count = p_widget["not_yet_campaigns_count"]
    if clicks > 0:
        lead_cvr = p_widget["for_all_campaigns"]["leads"] / clicks
    else:
        lead_cvr = 0

    ########################

    if global_status == "p_blacklist":
        return "black"
    elif (cost < 10) | (clicks < 300):
        if global_status == "p_whitelist":
            return "white"
        elif global_status == "p_greylist":
            return "grey"
        else:
            return "not yet"
    else:
        # grey
        if (global_status == "p_greylist") & (good_campaigns_count > 0):
            return "grey"
        elif (global_status == "p_greylist") & (bad_campaigns_count < 3):
            return "grey"
        elif (good_campaigns_count > 2) & (bad_campaigns_count > 0):
            return "grey"
        # white
        elif (global_status == "p_whitelist") & (bad_campaigns_count < 1):
            return "white"
        elif (good_campaigns_count > 2) & (bad_campaigns_count == 0):
            return "white"
        # black 
        elif (good_campaigns_count == 0) & (bad_campaigns_count > 2):
            return "black"
        elif (leads == 0) & (clicks > 2000) & (profit < -100):
            return "black"
        # not yet
        elif ((good_campaigns_count > 0) & (good_campaigns_count < 2)) | ((bad_campaigns_count > 0) & (bad_campaigns_count < 2)):
            return "not yet"
        else:
            return "not yet"
