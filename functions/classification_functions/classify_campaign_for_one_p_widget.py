def classify_campaign_for_one_p_widget(campaign):
    if campaign["clicks"] == 0:
        return "wait"
    elif campaign["leads"]/campaign["clicks"]*100 >= 0.20: 
        if campaign["sales"] >= 1:
            return "good"
        else:
            if campaign["leads"] >= 3:
                return "good" 
            else:
                return "half good" 
    else:
        if (campaign["cost"] > 30) | (campaign["clicks"] > 700):
            return "bad"
        elif ((campaign["cost"] > 10) & (campaign["cost"] <= 30)) & ((campaign["clicks"] > 300) & (campaign["clicks"] <= 700)):
            if campaign["leads"] == 0:
                return "half bad" 
            else:
                return "wait" 
        elif ((campaign["cost"] < 10) | (campaign["clicks"] < 300)):
            return "wait" 

