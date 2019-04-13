def classify_p_or_c_widget_for_one_campaign(p_or_c_widget, p_or_c_widget_total_sales):
    #################
    # define variables
    clicks = p_or_c_widget["clicks"] 
    cost = p_or_c_widget["cost"] 
    leads = p_or_c_widget["leads"] 
    sales = p_or_c_widget["sales"] 
    revenue = p_or_c_widget["revenue"] 
    profit = revenue - cost 
    mpl = p_or_c_widget["mpl"]
    mps = p_or_c_widget["mps"]
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
                if p_or_c_widget_total_sales == 0:
                    if cost >= (4 * mpl):
                        return "bad"
                    elif cost >= (2.5 * mpl):
                        if clicks < 1000:
                            return "half bad"
                        else:
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
                    if p_or_c_widget_total_sales == 0:
                        if cost > (4 * mpl):
                            if lead_cpa > (3 * mpl):
                                return "bad"
                            elif lead_cpa > (2 * mpl):
                                return "half bad"
                            else:
                                return "not yet"
                        elif cost > (3 * mpl):
                            if lead_cpa > (3.5 * mpl):
                                return "bad"
                            elif lead_cpa > (2.5 * mpl):
                                return "half bad"
                            else:
                                return "not yet"
                        elif cost > (2 * mpl):
                            if lead_cpa > (4 * mpl):
                                return "bad"
                            elif lead_cpa > (3 * mpl):
                                return "half bad"
                            else:
                                return "not yet"
                        else:
                            return "not yet"
                    else:
                        if cost > (5 * mpl):
                            if lead_cpa > (3 * mpl):
                                return "bad"
                            elif lead_cpa > (2 * mpl):
                                return "half bad"
                            else:
                                return "not yet"
                        elif cost > (4 * mpl):
                            if lead_cpa > (3.5 * mpl):
                                return "bad"
                            elif lead_cpa > (2.5 * mpl):
                                return "half bad"
                            else:
                                return "not yet"
                        elif cost > (3 * mpl):
                            if lead_cpa > (4 * mpl):
                                return "bad"
                            elif lead_cpa > (3 * mpl):
                                return "half bad"
                            else:
                                return "not yet"
                        else:
                            return "not yet"
            else:
                if leads >= 3:
                    return "good"
                elif leads == 2:
                    return "half good"
                else:
                    return "not yet"


                


