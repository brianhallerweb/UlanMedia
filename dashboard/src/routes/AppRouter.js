//@format
import React from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import PrivateRoute from './PrivateRoute.js';
import Login from '../components/Login.js';
import campaigns_for_all_campaignsHome from '../components/campaigns_for_all_campaigns/Home';
import widgets_for_all_campaignsHome from '../components/widgets_for_all_campaigns/Home';
import ads_for_all_campaignsHome from '../components/ads_for_all_campaigns/Home';
import offers_for_all_campaignsHome from '../components/offers_for_all_campaigns/Home';
import ads_for_one_campaignHome from '../components/ads_for_one_campaign/Home';
import offers_for_one_campaignHome from '../components/offers_for_one_campaign/Home';
import days_for_one_campaignHome from '../components/days_for_one_campaign/Home';
import widgets_for_one_campaignHome from '../components/widgets_for_one_campaign/Home';
import campaigns_for_one_parent_widgetHome from '../components/campaigns_for_one_parent_widget/Home';
import campaigns_for_one_child_widgetHome from '../components/campaigns_for_one_child_widget/Home';
import RedirectToCampaignsHome from '../components/RedirectToCampaignsHome';

const AppRouter = () => (
  <BrowserRouter>
    <div>
      <Switch>
        <Route path="/login" component={Login} />

        <PrivateRoute
          path="/campaigns"
          Component={campaigns_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/widgets"
          Component={widgets_for_all_campaignsHome}
        />
        <PrivateRoute path="/ads" Component={ads_for_all_campaignsHome} />
        <PrivateRoute path="/offers" Component={offers_for_all_campaignsHome} />
        <PrivateRoute
          path="/campaign/days/:volid"
          Component={days_for_one_campaignHome}
        />
        <PrivateRoute
          path="/campaign/offers/:volid"
          Component={offers_for_one_campaignHome}
        />
        <PrivateRoute
          path="/campaign/ads/:volid"
          Component={ads_for_one_campaignHome}
        />
        <PrivateRoute
          path="/campaign/widgets/:volid/:mgidid/:max_lead_cpa/:name"
          Component={widgets_for_one_campaignHome}
        />
        <PrivateRoute
          path="/widget/parent/:widgetID"
          Component={campaigns_for_one_parent_widgetHome}
        />
        <PrivateRoute
          path="/widget/child/:widgetID"
          Component={campaigns_for_one_child_widgetHome}
        />
        <PrivateRoute Component={RedirectToCampaignsHome} />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;
