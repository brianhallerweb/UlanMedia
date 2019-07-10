## Technologies

Front end: 
* React with React-Router 

Back end:
* Ubuntu Server 18.04 (vpn from digital ocean)
* Cron (daily data updates)
* Nginx (web server - reverse proxy to port 3000 and 5000)
* Pm2 (process management)
* Gunicorn (Running flask server in production)
* Node with MongoDB (Authentication, some list management routes)
* Flask (json data server)
* Python and Pandas (API requests, spreadsheet calculations)

## Authentication

There are two separate systems for authentication: one on the node server
(authentication middleware) and in React Router, the client side router (a created a higher order
component called ProtectedRoute). I have detailed explanations of those approaches
in separate repositories. The repositories are called secure_todos_API and
protected_route. As of 7/07/19, the Flask routes have been left unprotected. 

## The big picture of how data flows

1. Every morning, new data is acquired from a combination of MGID and Voluum.
   That data is stored in json files on the server and is usually named complete_xyz_data
2. Visiting a report page (e.g.
   ulanmedia.brianhaller.net/pwidgetsforallcampaigns) sends two POST requests.
The first processes complete_xyz_data to only include the relavent data (e.g.
summaries of each p widget for all campaigns). The second filters that data
according the checkbox selections.  
3. When filtered data arrives to the front end, it is sometimes further
   processed through "action functions". The results of action functions (e.g.
numbers of campaigns that are both bad and included) are shown in little red
text above the report data. 

## Naming convention for each report

The page names are organized around the the observational type (row
type) of each spreadsheet. For example, p_widgets_for_one_campaign means a
spreadsheet where each row is a p_widget in one particular campaign. 

## Detailed information on each report type

### campaigns for all campaigns

Campaigns for all campaigns is one of the few exceptions to the pattern of
sending two POST requests on every page. It only requires one "report" POST
request because the datasets are preprocessed in CRON. 

1. data_acquisition_scripts/create_campaigns_for_all_campaigns_datasets.py
   is run in CRON.
2. /campaignsforallcampaigns runs a POST request to data_analysis_functions/create_campaigns_for_all_campaigns_report.py

### p widgets for all campaigns

All p widget pages begin with the construction of complete_p_widgets_dataset,
which happens in CRON.

1. Data arrives from MGID and voluum through /data_acquisition_scripts/create_p_and_c_widgets_for_one_campaign_datasets.py. It creates a separate file for each campaign. 
2. /data_adquisition_scripts/create_complete_p_widgets_datasets.py takes the data from p_and_widgets_for_one_campaign and processes into a dictionary of p widgets. All the needed data for each widget is contained there. 

Then /pwidgetsforallcampaigns is easily created with the typical 2 POST request
process

1. /pwidgetsforallcampaigns runs a POST request to data_aquisition_functions/create_p_widgets_for_all_campaigns_dataset.py
2. /pwidgetsforallcampaigns runs a POST request to data_analysis_functions/create_p_widgets_for_all_campaigns_report.py

### campaigns for one p widget

1. /campaignsforonepwidget/pwidgetid runs a POST request to data_aquisition_functions/create_p_widgets_for_all_campaigns_dataset.py
2. /campaignsforonepwidget/pwidgetid runs a POST request to data_analysis_functions/create_p_widgets_for_all_campaigns_report.py
