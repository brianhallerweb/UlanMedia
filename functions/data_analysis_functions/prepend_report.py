def prepend_report(report):

    with open(f'../../dashboard/reports/{report}.html', 'r') as original: data = original.read()

    c1 = "c1 = profit < - max_sale_cpa"
    c2 = "c2 = clicks > 1000 AND leads = 0"
    c3 = "c3 = cost > 0.3*maxSaleCPA AND leadCPA > 2*maxLeadCPA"
    c4 = "c4 = cost > 0.5*maxSaleCPA AND leadCPA > 1.5*maxLeadCPA"    
    c5 = "c5 = cost > 2*maxSaleCPA AND leadCPA > maxLeadCPA"

    with open(f'../../dashboard/reports/{report}.html', 'w') as modified:
        modified.write(f"<p>{c1}</p><p>{c2}</p><p>{c3}</p><p>{c4}</p><p>{c5}</p>" + data)


