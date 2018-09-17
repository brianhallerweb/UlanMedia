import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Home from "../components/Home";
import CampaignByDays from "../components/CampaignByDays";
import RedirectToHome from "../components/RedirectToHome"

const AppRouter = () => (
  <BrowserRouter>
    <div>
      <Switch>
        <Route path="/" exact={true} component={Home} />
        <Route path="/campaign/:id" component={CampaignByDays} />
        <Route component={RedirectToHome} />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;
