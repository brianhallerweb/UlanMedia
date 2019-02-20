def classify_campaign_for_one_p_or_c_widget(campaign, p_or_c_widget_total_sales):
    #################
    # define variables
    clicks = campaign["clicks"] 
    cost = campaign["cost"] 
    leads = campaign["leads"] 
    sales = campaign["sales"] 
    revenue = campaign["revenue"] 
    profit = revenue - cost 
    mpl = campaign["mpl"]
    mps = campaign["mps"]
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
            if (leads >= 3) & (lead_cpa < mpl):
                return "good"
            elif (leads == 1 | leads == 2) & (lead_cpa < mpl):
                return "half good"
            else:
                if  p_or_c_widget_total_sales ==0:
                    if cost > (5 * mpl):
                        if (leads > 0) & (lead_cpa < (1.5 * mpl)):
                            return "half bad"
                        else:
                            return "bad"
                    elif cost > (3 * mpl):
                        if (leads > 0) & (lead_cpa < (2 * mpl)):
                            return "half bad"
                        else:
                            return "bad"
                    elif cost > (2 * mpl):
                        if (leads > 0) & (lead_cpa < (3 * mpl)):
                            return "wait"
                        else:
                            return "half bad"
                    else:
                        return "wait"
                else:
                    if cost > (1 * mps):
                        if (sales > 0) & (sale_cpa < (2 * mps)):
                            return "wait"
                        else:
                            return "bad"
                    elif cost > (6 * mpl):
                        if (leads > 0) & (lead_cpa < (3 * mpl)):
                            return "half bad"
                        else:
                            return "bad"
                    elif cost > (3 * mpl):
                        if (leads > 0) & (lead_cpa < (6 * mpl)):
                            return "wait"
                        else:
                            return "half bad"
                    else:
                        return "wait"


