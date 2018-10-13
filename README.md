The file naming convention is organized around the the observational type (row
type) of each spreadsheet. For example, widgets_for_one_campaign means a
spreadsheet where each row is a widget in one particular campaign. 

### Web app hierarchy 

campaigns_for_all_campaigns  
&nbsp;&nbsp;&nbsp;&nbsp;days_for_one_campaign
    offers_for_one_campaign
    ads_for_one_campaign
    widgets_for_one_campaign
        campaigns_for_one_child_widget (there are 2 routes to this spreadsheet)
        campaigns_for_one_parent_widget (there are 2 routes to this spreadsheet)
widgets_for_all_campaigns
    campaigns_for_one_child_widget (there are 2 routes to this spreadsheet)
    campaigns_for_one_parent_widget (there are 2 routes to this spreadsheet)
offers_for_all_campaigns
ads_for_all_campaigns

