import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import CampaignsHome from "../components/CampaignsHome";
import CampaignByDaysRecords from "../components/CampaignByDaysRecords";
import CampaignByWidgetsHome from '../components/CampaignByWidgetsHome';
import WidgetsHome from '../components/WidgetsHome';
import RedirectToHome from "../components/RedirectToCampaignsHome"

const AppRouter = () => (
  <BrowserRouter>
    <div>
      <Switch>
        <Route path="/" exact={true} component={CampaignsHome} />
        <Route path="/campaign/days/:volid" component={CampaignByDaysRecords} />
        <Route path="/campaign/widgets/:volid/:mgidid/:name" component={CampaignByWidgetsHome} />
        <Route path="/widgets/:widgetType/:widgetID" component={WidgetsHome} />
        <Route component={RedirectToHome} />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;
