def classify_campaign_for_one_p_widget(campaign, p_widget_total_sales):
    #################
    # define variables
    clicks = campaign["clicks"] 
    cost = campaign["cost"] 
    leads = campaign["leads"] 
    sales = campaign["sales"] 
    revenue = campaign["revenue"] 
    profit = revenue - cost 
    max_lead_cpa = campaign["max_lead_cpa"]
    max_sale_cpa = campaign["max_sale_cpa"]
    if clicks == 0:
        cvr = 0
    else:
        cvr = leads / clicks * 100
    if leads == 0:
        lead_cpa = 0
    else:
        lead_cpa = cost / leads
    if sales == 0:
        sale_cpa = 0
    else:
        sale_cpa = cost / sales

    #######################
    #######################
    # return classification

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
                # here

                if  p_widget_total_sales ==0:
                    if cost > (5 * max_lead_cpa):
                        if (leads > 0) & (lead_cpa < (1.5 * max_lead_cpa)):
                            return "half bad"
                        else:
                            return "bad"


                    elif cost > (3 * max_lead_cpa):
                        if (leads > 0) & (lead_cpa < (2 * max_lead_cpa)):
                            return "half bad"
                        else:
                            return "bad"
                    elif cost > (2 * max_lead_cpa):
                        if (leads > 0) & (lead_cpa < (3 * max_lead_cpa)):
                            return "wait"
                        else:
                            return "half bad"
                    else:
                        return "wait"
                else:
                    if cost > (1 * max_sale_cpa):
                        if (sales > 0) & (sale_cpa < (2 * max_sale_cpa)):
                            return "wait"
                        else:
                            return "bad"
                    elif cost > (6 * max_lead_cpa):
                        if (leads > 0) & (lead_cpa < (3 * max_lead_cpa)):
                            return "half bad"
                        else:
                            return "bad"
                    elif cost > (3 * max_lead_cpa):
                        if (leads > 0) & (lead_cpa < (6 * max_lead_cpa)):
                            return "wait"
                        else:
                            return "half bad"
                    else:
                        return "wait"


