import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import campaigns_for_all_campaignsHome from "../components/campaigns_for_all_campaigns/Home";
import widgets_for_all_campaignsHome from "../components/widgets_for_all_campaigns/Home";
import ads_for_all_campaignsHome from "../components/ads_for_all_campaigns/Home";
import offers_for_all_campaignsHome from "../components/offers_for_all_campaigns/Home";
import ads_for_one_campaignHome from "../components/ads_for_one_campaign/Home";
import offers_for_one_campaignHome from "../components/offers_for_one_campaign/Home";
import days_for_one_campaignHome from "../components/days_for_one_campaign/Home";
import widgets_for_one_campaignHome from '../components/widgets_for_one_campaign/Home';
import campaigns_for_one_parent_widgetHome from '../components/campaigns_for_one_parent_widget/Home';
import campaigns_for_one_child_widgetHome from '../components/campaigns_for_one_child_widget/Home';
import RedirectToHome from "../components/RedirectToCampaignsHome"

const AppRouter = () => (
  <BrowserRouter>
    <div>
      <Switch>
        <Route path="/campaigns" exact={true} component={campaigns_for_all_campaignsHome} />
        <Route path="/widgets" exact={true} component={widgets_for_all_campaignsHome} />
        <Route path="/ads" exact={true} component={ads_for_all_campaignsHome} />
        <Route path="/offers" exact={true} component={offers_for_all_campaignsHome} />
        <Route path="/campaign/days/:volid" component={days_for_one_campaignHome} />
        <Route path="/campaign/offers/:volid" component={offers_for_one_campaignHome} />
        <Route path="/campaign/ads/:volid" component={ads_for_one_campaignHome} />
        <Route path="/campaign/widgets/:volid/:mgidid/:max_lead_cpa/:name" component={widgets_for_one_campaignHome} />
        <Route path="/widgets/parent/:widgetID" component={campaigns_for_one_parent_widgetHome} />
        <Route path="/widgets/child/:widgetID" component={campaigns_for_one_child_widgetHome} />
        <Route component={RedirectToHome} />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;
