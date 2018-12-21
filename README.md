The file naming convention is organized around the the observational type (row
type) of each spreadsheet. For example, widgets_for_one_campaign means a
spreadsheet where each row is a widget in one particular campaign. 

### Web app map 

![Alt text](/ulanmediadashboard.jpg)

### How the reports are generated

write the general process of acquiring the data and creating reports

### Authentication

There are two separate systems for authentication: one on the server
(authentication middleware) and on in React Router, the client side router (a created a higher order
component called ProtectedRoute). I have detailed explanations of those approaches
in separate repositories. The repositories are called secure_todos_API and
protected_route. 
