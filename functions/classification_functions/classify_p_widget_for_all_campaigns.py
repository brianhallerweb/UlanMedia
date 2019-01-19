def classify_p_widget_for_all_campaigns(p_widget):
    if p_widget["for_all_campaigns"]["global_status"] == "blacklist":
        return "black"
    else:
        if (p_widget["for_all_campaigns"]["cost"] >= 10) | (p_widget["for_all_campaigns"]["clicks"] >= 300):
            if (p_widget["good_campaigns_count"] >= 3) & (p_widget["bad_campaigns_count"] == 0 &
            p_widget["bad_campaigns_included_count"] == 0):
                return "white"
            elif (p_widget["good_campaigns_count"] == 0) & ((p_widget["bad_campaigns_count"] +
                p_widget["bad_campaigns_included_count"]) >= 1) & (p_widget["for_all_campaigns"]["revenue"] - p_widget["for_all_campaigns"]["cost"] < -60):
                return "black"
            elif (p_widget["good_campaigns_count"] >= 3) & ((p_widget["bad_campaigns_count"] +
                p_widget["bad_campaigns_included_count"]) >= 3):
                return "grey"
            elif (p_widget["good_campaigns_count"] == 0) & ((p_widget["bad_campaigns_count"] +
                p_widget["bad_campaigns_included_count"]) >= 3):
                return "black"
            else:
                return "wait"
        else:
            if p_widget["for_all_campaigns"]["global_status"] == "not yet listed":
                return "wait"
            elif p_widget["for_all_campaigns"]["global_status"] == "whitelist":
                return "white"
            elif p_widget["for_all_campaigns"]["global_status"] == "greylist":
                return "grey"
            else:
                return "wait"

