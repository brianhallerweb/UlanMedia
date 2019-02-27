def classify_c_widget_for_all_campaigns(c_widget):
    global_status = c_widget["for_all_campaigns"]["global_status"]
    clicks = c_widget["for_all_campaigns"]["clicks"] 
    cost = c_widget["for_all_campaigns"]["cost"]
    revenue = c_widget["for_all_campaigns"]["revenue"]
    leads = c_widget["for_all_campaigns"]["leads"]
    profit = revenue - cost
    good_campaigns_count = c_widget["good_campaigns_count"]
    bad_campaigns_count = c_widget["bad_campaigns_count"]
    wait_campaigns_count = c_widget["wait_campaigns_count"]
    if clicks > 0:
        lead_cvr = c_widget["for_all_campaigns"]["leads"] / clicks
    else:
        lead_cvr = 0

    if (global_status == "c_blacklist") | (global_status == "pc_blacklist"):
        return "black"
    elif (cost < 10) | (clicks < 300):
        if (global_status == "c_whitelist") | (global_status == "pc_whitelist"):
            return "white"
        elif (global_status == "c_greylist") | (global_status == "pc_greylist"):
            return "grey"
        else:
            return "wait"
    else:
        # grey
        if ((global_status == "c_greylist") | (global_status == "pc_greylist")) & (good_campaigns_count > 0):
            return "grey"
        elif (good_campaigns_count > 2) & (bad_campaigns_count > 0):
            return "grey"
        # white
        elif ((global_status == "c_whitelist") | (global_status == "pc_whitelist")) & (bad_campaigns_count == 0):
            return "white"
        elif (good_campaigns_count > 2) & (bad_campaigns_count == 0):
            return "white"
        # black 
        elif (good_campaigns_count == 0) & (bad_campaigns_count > 2):
            return "black"
        elif (good_campaigns_count == 0) & (bad_campaigns_count > 0) & (lead_cvr < .002) & (profit < -60):
            return "black"
        elif (leads == 0) & (clicks > 1000) & (profit < -60):
            return "black"
        # wait
        elif ((good_campaigns_count > 0) & (good_campaigns_count < 2)) | ((bad_campaigns_count > 0) & (bad_campaigns_count < 2)):
            return "wait"
        else:
            return "wait"
