The file naming convention is organized around the the observational type (row
type) of each spreadsheet. For example, widgets_for_one_campaign means a
spreadsheet where each row is a widget in one particular campaign. 

### Web app hierarchy 

campaigns_for_all_campaigns  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;days_for_one_campaign  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offers_for_one_campaign  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ads_for_one_campaign  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;widgets_for_one_campaign  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;campaigns_for_one_child_widget (there are 2 routes to this spreadsheet)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;campaigns_for_one_parent_widget (there are 2 routes to this spreadsheet)  
widgets_for_all_campaigns  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;campaigns_for_one_child_widget (there are 2 routes to this spreadsheet)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;campaigns_for_one_parent_widget (there are 2 routes to this spreadsheet)  
offers_for_all_campaigns  
ads_for_all_campaigns  

### Authentication

There are two separate systems for authentication: one on the server
(authentication middleware) and on in React Router, the client side router (a created a higher order
component called ProtectedRoute). I have detailed explanations of those approaches
in separate repositories. The repositories are called secure_todos_API and
protected_route. 
