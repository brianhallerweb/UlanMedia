The file naming convention is organized around the the observational type (row
type) of each spreadsheet. For example, widgets_for_one_campaign means a
spreadsheet where each row is a widget in one particular campaign. 

### Web app hierarchy 

`

campaigns_for_all_campaigns
\t    days_for_one_campaign
\t    offers_for_one_campaign
\t    ads_for_one_campaign
\t    widgets_for_one_campaign
\t\t        campaigns_for_one_child_widget (there are 2 routes to this spreadsheet)
\t\t        campaigns_for_one_parent_widget (there are 2 routes to this spreadsheet)
widgets_for_all_campaigns
\t    campaigns_for_one_child_widget (there are 2 routes to this spreadsheet)
\t    campaigns_for_one_parent_widget (there are 2 routes to this spreadsheet)
offers_for_all_campaigns
ads_for_all_campaigns

`
