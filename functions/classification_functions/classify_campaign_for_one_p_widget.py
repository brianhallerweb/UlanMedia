def classify_campaign_for_one_p_widget(campaign):
    if campaign["clicks"] > 0:
        if (campaign["sales"] > 0) & ((campaign["revenue"] - campaign["cost"]) > 0):
            return "good"
        else:
            if (campaign["leads"]/campaign["clicks"]*100) >= 0.20:
                if campaign["leads"] > 2:
                    return "good" 
                else:
                    return "half good" 
            else:
                if (campaign["cost"] >= 50) | (campaign["clicks"] >= 1000):
                    return "bad"
                elif ((campaign["cost"] >= 30) & (campaign["cost"] <= 50)) & ((campaign["clicks"] >= 700) & (campaign["clicks"] <= 1000)):
                    if campaign["leads"] == 0:
                        return "bad"
                    else: 
                        return "half bad"
                elif ((campaign["cost"] >= 10) & (campaign["cost"] <= 30)) & ((campaign["clicks"] >= 300) & (campaign["clicks"] <= 700)):
                    if campaign["leads"] == 0:
                        return "half bad"
                    else: 
                        return "wait"
                elif (campaign["cost"] <= 10) | (campaign["clicks"] <= 300):
                    return "wait"
                else:
                    return "wait"
    else:
        return "wait"

