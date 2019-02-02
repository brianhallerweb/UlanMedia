def classify_p_widget_for_all_campaigns(p_widget):
    if p_widget["for_all_campaigns"]["global_status"] == "blacklist":
        return "black"
    elif (p_widget["for_all_campaigns"]["cost"] >= 10) | (p_widget["for_all_campaigns"]["clicks"] >= 300):
        #now I am adding new things
        # grey
        if (p_widget["for_all_campaigns"]["global_status"] == "greylist") & (p_widget["good_campaigns_count"] > 0):
            return "grey"
        elif (p_widget["good_campaigns_count"] > 2) & (p_widget["bad_campaigns_count"] > 0):
            return "grey"
        # white
        elif (p_widget["for_all_campaigns"]["global_status"] == "whitelist") & (p_widget["bad_campaigns_count"] == 0):
            return "white"
        elif (p_widget["good_campaigns_count"] > 2) & (p_widget["bad_campaigns_count"] == 0):
            return "white"
        # black 
        elif (p_widget["good_campaigns_count"] == 0) & (p_widget["bad_campaigns_count"] > 2):
            return "black"
        elif (p_widget["good_campaigns_count"] == 0) & (p_widget["bad_campaigns_count"] > 0) & (p_widget["for_all_campaigns"]["revenue"] - p_widget["for_all_campaigns"]["cost"] < -60):
            return "black"
        # wait
        elif ((p_widget["good_campaigns_count"] > 0) & (p_widget["good_campaigns_count"] < 2)) | ((p_widget["bad_campaigns_count"] > 0) & (p_widget["bad_campaigns_count"] < 2)):
            return "wait"
        else:
            return "wait"
    else:
        if p_widget["for_all_campaigns"]["global_status"] == "whitelist":
            return "white"
        elif p_widget["for_all_campaigns"]["global_status"] == "greylist":
            return "grey"
        else:
            return "wait"

