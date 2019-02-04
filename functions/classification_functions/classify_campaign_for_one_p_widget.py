def classify_campaign_for_one_p_widget(campaign):
    clicks = campaign["clicks"] 
    cost = campaign["cost"] 
    leads = campaign["leads"] 
    sales = campaign["sales"] 
    revenue = campaign["revenue"] 
    profit = revenue - cost 
    max_lead_cpa = campaign["max_lead_cpa"]
    if clicks == 0:
        cvr = 0
    else:
        cvr = leads / clicks * 100
    if leads == 0:
        lead_cpa = 0
    else:
        lead_cpa = cost / leads


    if clicks == 0:
        return "wait"
    else:
        if (sales > 0) & (profit > 0):
            return "good"
        else:
            if (leads >= 3) & (lead_cpa < max_lead_cpa):
                return "good"
            elif (leads == 1 | leads == 2) & (lead_cpa < max_lead_cpa):
                return "half good"
            else:
                if cost > (4 * max_lead_cpa):
                    return "bad"
                elif cost > (3 * max_lead_cpa):
                    if leads > 0:
                        return "half bad"
                    else:
                        return "bad"
                elif cost > (2 * max_lead_cpa):
                    if leads > 0:
                        return "wait"
                    else:
                        return "half bad"
                else:
                    return "wait"


