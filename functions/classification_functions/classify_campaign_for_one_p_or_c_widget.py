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
    if sales > 0:
        if (cost/sales) <= mps:
            return "good"
        elif (cost/(sales + 1)) <= mps:
            return "half good"
        elif (cost/(sales + 2)) > mps:
            return "bad"
        elif (cost/(sales + 1)) > mps:
            return "half bad"
    else:
        if leads == 0:
            if clicks < 600:
                return "not yet"
            else:
                if sales == 0:
                    if cost >= (3 * mpl):
                        return "bad"
                    elif cost >= (2 * mpl):
                        return "half bad"
                    else:
                        return "not yet"
                else:
                    if cost >= (4 * mpl):
                        return "bad"
                    elif cost >= (3 * mpl):
                        return "half bad"
                    else:
                        return "not yet"
        else:
            if lead_cpa >= mpl:
                if clicks < 600:
                    return "not yet"
                else:
                    if sales == 0:
                        if cost > (5 * mpl):
                            if lead_cpa < (2 * mpl):
                                return "half bad"
                            else:
                                return "bad"
                        elif cost > (3 * mpl):
                            if lead_cpa < (2.5 * mpl):
                                return "half bad"
                            else:
                                return "bad"
                        elif cost > (2 * mpl):
                            if lead_cpa < (3 * mpl):
                                return "not yet"
                            else:
                                return "half bad"
                        else:
                            return "not yet"
                    else:
                        if cost > (8 * mpl):
                            if lead_cpa < (3 * mpl):
                                return "not yet"
                            else:
                                return "bad"
                        elif cost > (5 * mpl):
                            if lead_cpa < (3.5 * mpl):
                                return "half bad"
                            else:
                                return "bad"
                        elif cost > (3 * mpl):
                            if lead_cpa < (4 * mpl):
                                return "not yet"
                            else:
                                return "half bad"
                        else:
                            return "half bad"
            else:
                if leads >= 3:
                    return "good"
                elif leads == 2:
                    return "half good"
                else:
                    return "not yet"


                



    ########### old flow chart #################3
    # if clicks == 0:
        # return "not yet"
    # else:
        # if (sales > 0) & (profit > 0):
            # return "good"
        # else:
            # if (leads >= 3) & (lead_cpa < mpl):
                # return "good"
            # elif (leads == 2) & (lead_cpa < mpl):
                # return "half good"
            # else:
                # if  p_or_c_widget_total_sales == 0:
                    # if (cost > (5 * mpl)) & (clicks > 600):
                        # if (leads > 0) & (lead_cpa < (2 * mpl)):
                            # return "half bad"
                        # else:
                            # return "bad"
                    # elif (cost > (3 * mpl)) & (clicks > 600):
                        # if (leads > 0) & (lead_cpa < (2.5 * mpl)):
                            # return "half bad"
                        # else:
                            # return "bad"
                    # elif (cost > (2 * mpl)) & (clicks > 600):
                        # if (leads > 0) & (lead_cpa < (3 * mpl)):
                            # return "not yet"
                        # else:
                            # return "half bad"
                    # else:
                        # return "not yet"
                # else:
                    # if cost > (1 * mps):
                        # if (sales > 0) & (sale_cpa < (2 * mps)):
                            # return "not yet"
                        # else:
                            # return "bad"
                    # elif cost > (6 * mpl):
                        # if (leads > 0) & (lead_cpa < (3 * mpl)):
                            # return "half bad"
                        # else:
                            # return "bad"
                    # elif cost > (3 * mpl):
                        # if (leads > 0) & (lead_cpa < (6 * mpl)):
                            # return "not yet"
                        # else:
                            # return "half bad"
                    # else:
                        # return "not yet"


