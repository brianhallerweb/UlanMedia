### Naming convention 

The page names are organized around the the observational type (row
type) of each spreadsheet. For example, widgets_for_one_campaign means a
spreadsheet where each row is a widget in one particular campaign. 

### Web app map 

![Alt text](/full_dashboard_map.jpg)

### How the reports are generated

In most cases, reports are generated in 3 stages. 
1. Get all data in through a CRON job and save it to a json file. 
2. Refine the data to with a "data acquisition step". That usually involves
   filtering the data by some condition (e.g. widgets for one campaign) and
saving to another json file. This step is done on-demand with a python child process
in the web app. 
3. Further refine the data to to include only what will be visually displayed
   as a report in the web app. This step is done on-demand with a pandas child
process. The data is immediately displayed as html by React - no json file is
saved. 

### Authentication

There are two separate systems for authentication: one on the server
(authentication middleware) and on in React Router, the client side router (a created a higher order
component called ProtectedRoute). I have detailed explanations of those approaches
in separate repositories. The repositories are called secure_todos_API and
protected_route. 
