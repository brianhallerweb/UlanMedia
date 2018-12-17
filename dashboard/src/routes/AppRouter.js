//@format
import React from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import PrivateRoute from './PrivateRoute.js';
import Login from '../components/Login.js';
import campaigns_for_all_campaignsHome from '../components/campaigns_for_all_campaigns/Home';
import p_widgets_for_all_campaignsHome from '../components/p_widgets_for_all_campaigns/Home';
import ads_for_all_campaignsHome from '../components/ads_for_all_campaigns/Home';
import ads_for_one_campaignHome from '../components/ads_for_one_campaign/Home';
import offers_for_all_campaignsHome from '../components/offers_for_all_campaigns/Home';
import offers_for_one_campaignHome from '../components/offers_for_one_campaign/Home';
import days_for_one_campaignHome from '../components/days_for_one_campaign/Home';
import p_widgets_for_one_campaignHome from '../components/p_widgets_for_one_campaign/Home';
import c_widgets_for_one_p_widgetHome from '../components/c_widgets_for_one_p_widget/Home';
import campaigns_for_one_p_widgetHome from '../components/campaigns_for_one_p_widget/Home';
import campaigns_for_one_c_widgetHome from '../components/campaigns_for_one_c_widget/Home';
import campaigns_for_one_adHome from '../components/campaigns_for_one_ad/Home';
import campaigns_for_one_offerHome from '../components/campaigns_for_one_offer/Home';
import RedirectToCampaignsHome from '../components/RedirectToCampaignsHome';

const AppRouter = () => (
  <BrowserRouter>
    <div>
      <Switch>
        // login route
        <Route path="/login" component={Login} />
        // campaigns routes
        <PrivateRoute
          path="/campaigns"
          Component={campaigns_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/campaign/days/:volid"
          Component={days_for_one_campaignHome}
        />
        <PrivateRoute
          path="/campaign/offers/:volid"
          Component={offers_for_one_campaignHome}
        />
        <PrivateRoute
          path="/pwidgetsforonecampaign/:volid/:mgidid/:max_lead_cpa/:name"
          Component={p_widgets_for_one_campaignHome}
        />
        // widgets routes
        <PrivateRoute
          path="/pwidgetsforallcampaigns"
          Component={p_widgets_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/cwidgetsforonepwidget/:pWidgetID"
          Component={c_widgets_for_one_p_widgetHome}
        />
        <PrivateRoute
          path="/campaignsforonepwidget/:widgetID"
          Component={campaigns_for_one_p_widgetHome}
        />
        <PrivateRoute
          path="/campaignsforoneoffer/:offerID/:offerName"
          Component={campaigns_for_one_offerHome}
        />
        <PrivateRoute
          path="/offersforonecampaign/:volID/:campaignName"
          Component={offers_for_one_campaignHome}
        />
        <PrivateRoute
          path="/campaignsforonecwidget/:widgetID"
          Component={campaigns_for_one_c_widgetHome}
        />
        // ads routes
        <PrivateRoute
          path="/ads/:volid/:name"
          Component={ads_for_one_campaignHome}
        />
        <PrivateRoute path="/ads" Component={ads_for_all_campaignsHome} />
        <PrivateRoute
          path="/ad/:adImage"
          Component={campaigns_for_one_adHome}
        />
        // offers routes
        <PrivateRoute path="/offers" Component={offers_for_all_campaignsHome} />
        // redirect to campaigns_for_all_campaigns if url doesn't match a route
        <PrivateRoute Component={RedirectToCampaignsHome} />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;
