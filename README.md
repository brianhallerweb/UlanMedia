### Technologies

The front end uses: 
React with React-Router 

The back end uses:
*Ubuntu Server 18.04 (vpn from digital ocean)
*Cron (daily data updates)
*Nginx (web server - reverse proxy to port 3000 and 5000)
*Pm2 (process management)
*Gunicorn (Running flask server in production)
*Node with MongoDB (Authentication, some list management routes)
*Flask (json data server)
*Python and Pandas (API requests, spreadsheet calculations)

### Authentication

There are two separate systems for authentication: one on the node server
(authentication middleware) and in React Router, the client side router (a created a higher order
component called ProtectedRoute). I have detailed explanations of those approaches
in separate repositories. The repositories are called secure_todos_API and
protected_route. As of 7/07/19, the Flask routes have been left unprotected. 

### The big picture of how data flows

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

### Naming convention for each report

The page names are organized around the the observational type (row
type) of each spreadsheet. For example, p_widgets_for_one_campaign means a
spreadsheet where each row is a p_widget in one particular campaign. 

### Terminology 

Campaign
p widget
c widget
p offer
c offer
flow rule
ad
ad image
country

### Detailed information on each report type

#### Campaigns for all campaigns

This is how campaigns for all campaigns works. 
