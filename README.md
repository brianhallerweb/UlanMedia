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

## Starting the development environment

The development environment includes a react dev server (port 8080), a node server (port 3000) with a mongo database, and a
flask dev server (port 5000). The webpack configuration within the react dev
server includes proxy information for the node and flask servers. 

The development environment is easily started with 3 scripts -
startulanmediafrontendserver, startulanmediabackendserver,
startulanmediajsonserver.

## Starting the production environment

All reactequests to the server go through an nginx reverse proxy. That is how requests to
brianhaller.net on port 80 (or the other port for https request) get to the
node server running on port 3000.

Pm2 is used to start the node and flask servers in production. It works very
simply - "pm2 start servername" is the command. However, the flask server is
more complicated because of the need to use a python virtual environment and
the need to run the python server with gunicorn. I wrote a script called
start_json_server that deals with gunicorn and the virtual environment so, in
the end, you just need to run "pm2 start start_json_server"

# Detailed information on each report type

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
2. /data_adquisition_scripts/create_complete_p_widgets_datasets.py takes the data from p_and_c_widgets_for_one_campaign and processes into a dictionary of p widgets. All the needed data for each widget is contained there. 

Then /pwidgetsforallcampaigns is easily created with the typical 2 POST request
process

1. /pwidgetsforallcampaigns runs a POST request to data_aquisition_functions/create_p_widgets_for_all_campaigns_dataset.py
2. /pwidgetsforallcampaigns runs a POST request to data_analysis_functions/create_p_widgets_for_all_campaigns_report.py

### campaigns for one p widget

1. /campaignsforonepwidget/pwidgetid runs a POST request to data_aquisition_functions/create_campaigns_for_one_p_widget_dataset.py
2. /campaignsforonepwidget/pwidgetid runs a POST request to data_analysis_functions/create_campaigns_for_one_p_widget_report.py

### p widgets for one campaign

1. /pwidgetsforonecampaign/campaignid runs a POST request to data_aquisition_functions/create_campaigns_for_all_p_widgets_dataset.py
2. /pwidgetsforonecampaign/campaignid runs a POST request to data_analysis_functions/create_campaigns_for_all_p_widgets_report.py

### p widgets for one domain for all campaigns

1. /pwidgetsforonedomainforallcampaigns/domain runs a POST request to data_aquisition_functions/create_p_widgets_for_one_domain_for_all_campaigns_dataset.py
2. /pwidgetsforonedomainforallcampaigns/domain runs a POST request to data_analysis_functions/create_p_widgets_for_one_domain_for_all_campaigns_report.py

### c widgets for all campaigns

All c widget pages begin with the construction of complete_c_widgets_dataset,
which happens in CRON.

1. Data arrives from MGID and voluum through /data_acquisition_scripts/create_p_and_c_widgets_for_one_campaign_datasets.py. It creates a separate file for each campaign. 
2. /data_adquisition_scripts/create_complete_c_widgets_datasets.py takes the data from p_and_c_widgets_for_one_campaign and processes into a dictionary of c widgets. All the needed data for each widget is contained there. 

Then /cwidgetsforallcampaigns is easily created with the typical 2 POST request
process

1. /cwidgetsforallcampaigns runs a POST request to data_aquisition_functions/create_c_widgets_for_all_campaigns_dataset.py
2. /cwidgetsforallcampaigns runs a POST request to data_analysis_functions/create_c_widgets_for_all_campaigns_report.py

### campaigns for one c widget

1. /campaignsforonecwidget/cwidgetid runs a POST request to data_aquisition_functions/create_campaigns_for_one_c_widget_dataset.py
2. /campaignsforonecwidget/cwidgetid runs a POST request to data_analysis_functions/create_campaigns_for_one_c_widget_report.py

### c widgets for one campaign

1. /cwidgetsforonecampaign/campaignid runs a POST request to data_aquisition_functions/create_campaigns_for_all_c_widgets_dataset.py
2. /cwidgetsforonecampaign/campaignid runs a POST request to data_analysis_functions/create_campaigns_for_all_c_widgets_report.py

### c widgets for one p widget

1. /cwidgetsforonepwidget/pwidgetid runs a POST request to data_aquisition_functions/create_c_widgets_for_one_p_widget_dataset.py
2. /cwidgetsforonepwidget/pwidgetid runs a POST request to data_analysis_functions/create_c_widgets_for_one_p_widget_report.py

### c widgets for one p widget for one campaign

1. /cwidgetsforonepwidgetforonecampaign/campaignid/pwidgetid/campaignname runs a POST request to data_aquisition_functions/create_c_widgets_for_one_p_widget_for_one_campaign_dataset.py
2. /cwidgetsforonepwidgetforonecampaign/campaignid/pwidgetid/campaignname runs a POST request to data_analysis_functions/create_c_widgets_for_one_p_widget_for_one_campaign_dataset.py

### ads for all campaigns

All ads pages begin with the construction of complete_ads_dataset,
which happens in CRON.

1. Data arrives from MGID and voluum at /data_acquisition_scripts/create_ads_datasets.py. The script uses /data_acquisition_functions/get_mgid_ads_data.py and /data_acquisition_functions/get_vol_ads_data.py to get data from mgid and volume. That data is combined in /data_acquisition_scripts/combine_mgid_vol_ads_data. 
2. /data_acquisition_scripts/create_complete_ads_datasets.py takes the data created in step 1 and creates a complete dictionary of ads. All the needed data for each ad is contained there. 

Then /adsforallcampaigns is easily created with the typical 2 POST request
process

1. /adsforallcampaigns runs a POST request to data_aquisition_functions/create_ads_for_all_campaigns_dataset.py
2. /adsforallcampaigns runs a POST request to data_analysis_functions/create_ads_for_all_campaigns_report.py

### campaigns for one ad

1. /campaignsforonead/adimage runs a POST request to data_aquisition_functions/create_campaigns_for_one_ad_dataset.py
2. /campaignsforonead/adimage runs a POST request to data_analysis_functions/create_campaigns_for_one_ad_report.py

### ads for one campaign

1. /adsforonecampaign/campaignid runs a POST request to data_aquisition_functions/create_ads_for_one_campaign_dataset.py
2. /adsforonecampaign/campaignid runs a POST request to data_analysis_functions/create_ads_for_one_campaign_report.py

### offers for all campaigns

All offers pages begin with 2 different datasets - offers for each flow rule
and offers for each campaign. These are created in CRON from
/data_acquisition_scripts/create_offers_for_each_flow_rule_datasets.py and /data_acquisition_scripts/create_offers_for_each_campaign_datasets.py

Then /offersforallcampaigns is easily created with the typical 2 POST request
process

1. /offersforallcampaigns runs a POST request to data_aquisition_functions/create_offerss_for_all_campaigns_dataset.py
2. /offersforallcampaigns runs a POST request to data_analysis_functions/create_offers_for_all_campaigns_report.py

### campaigns for one offers

1. /campaignsforoneoffers/offerid/offername runs a POST request to data_aquisition_functions/create_campaigns_for_one_offer_dataset.py
2. /campaignsforoneoffers/offerid/offername runs a POST request to data_analysis_functions/create_campaigns_for_one_offer_report.py

### offers for one campaign

1. /offersforonecampaign/campaignid/campaignname runs a POST request to data_aquisition_functions/create_offers_for_one_campaign_dataset.py
2. /offerssforonecampaign/campaignid/campaignname runs a POST request to data_analysis_functions/create_offers_for_one_campaign_report.py

### offers for one flow rule

1. /offersforoneflowrule/flowrule runs a POST request to data_aquisition_functions/create_offers_for_one_flow_rule_dataset.py
2. /offerssforoneflowrule/flowrule runs a POST request to data_analysis_functions/create_offers_for_one_flow_rule_report.py

### countries for all campaigns

All countries pages begin with the construction of complete_countries_dataset,
which happens in CRON.

1. Data arrives from Voluum at /data_acquisition_scripts/create_countries_datasets.py. 
2. /data_acquisition_scripts/create_complete_countries_datasets.py takes the data created in step 1 and creates a complete dictionary of countriess. All the needed data for each country is contained there. 

Then /countriesforallcampaigns is created with the typical 2 POST request
process

1. /countriesforallcampaigns runs a POST request to data_aquisition_functions/create_countries_for_all_campaigns_dataset.py
2. /countriesforallcampaigns runs a POST request to data_analysis_functions/create_countries_for_all_campaigns_report.py

### campaigns for one country 

1. /campaignsforonecountry/countryname runs a POST request to data_aquisition_functions/create_campaigns_for_one_country_dataset.py
2. /campaignsforonecountry/countryname runs a POST request to data_analysis_functions/create_campaigns_for_one_country_report.py

### countries for one campaign

1. /countriesforonecampaign/campaignid runs a POST request to data_aquisition_functions/create_countries_for_one_campaign_dataset.py
2. /countriesforonecampaign/campaignid runs a POST request to data_analysis_functions/create_countries_for_one_campaign_report.py

### languages for all campaigns

All countries pages begin with the construction of complete_languages_dataset,
which happens in CRON.

1. Data arrives from Voluum at /data_acquisition_scripts/create_languages_datasets.py. 
2. /data_acquisition_scripts/create_complete_languages_datasets.py takes the data created in step 1 and creates a complete dictionary of languages. All the needed data for each language is contained there. 

Then /languagessforallcampaigns is created with the typical 2 POST request
process

1. /languagesforallcampaigns runs a POST request to data_aquisition_functions/create_languages_for_all_campaigns_dataset.py
2. /languagesforallcampaigns runs a POST request to data_analysis_functions/create_languages_for_all_campaigns_report.py

### campaigns for one language 

1. /campaignsforonecountry/countryname runs a POST request to data_aquisition_functions/create_campaigns_for_one_country_dataset.py
2. /campaignsforonecountry/countryname runs a POST request to data_analysis_functions/create_campaigns_for_one_country_report.py

### languages for one campaign

1. /languagesforonecampaign/campaignid runs a POST request to data_aquisition_functions/create_languages_for_one_campaign_dataset.py
2. /languagesforonecampaign/campaignid runs a POST request to data_analysis_functions/create_languages_for_one_campaign_report.py
