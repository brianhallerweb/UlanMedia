//@format
import React from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import PrivateRoute from './PrivateRoute.js';
import Login from '../components/Login.js';
import campaigns_for_all_campaignsHome from '../components/campaigns_for_all_campaigns/Home';
import countries_for_all_campaignsHome from '../components/countries_for_all_campaigns/Home';
import p_widgets_for_all_campaignsHome from '../components/p_widgets_for_all_campaigns/Home';
import c_widgets_for_all_campaignsHome from '../components/c_widgets_for_all_campaigns/Home';
import ads_for_all_campaignsHome from '../components/ads_for_all_campaigns/Home';
import ads_for_one_campaignHome from '../components/ads_for_one_campaign/Home';
import offers_for_all_campaignsHome from '../components/offers_for_all_campaigns/Home';
import offers_for_one_campaignHome from '../components/offers_for_one_campaign/Home';
import offers_for_one_flowHome from '../components/offers_for_one_flow/Home';
import days_for_one_campaignHome from '../components/days_for_one_campaign/Home';
import p_widgets_for_one_campaignHome from '../components/p_widgets_for_one_campaign/Home';
import c_widgets_for_one_p_widgetHome from '../components/c_widgets_for_one_p_widget/Home';
import campaigns_for_one_p_widgetHome from '../components/campaigns_for_one_p_widget/Home';
import campaigns_for_one_c_widgetHome from '../components/campaigns_for_one_c_widget/Home';
import campaigns_for_one_adHome from '../components/campaigns_for_one_ad/Home';
import campaigns_for_one_offerHome from '../components/campaigns_for_one_offer/Home';
import p_widgets_for_all_campaignsListPWidgetConfirmation from '../components/p_widgets_for_all_campaigns/ListPWidgetConfirmation';
import c_widgets_for_all_campaignsListCWidgetConfirmation from '../components/c_widgets_for_all_campaigns/ListCWidgetConfirmation';
import campaigns_for_one_p_widgetExcludeCampaignConfirmation from '../components/campaigns_for_one_p_widget/ExcludeCampaignConfirmation';
import campaigns_for_one_c_widgetExcludeCampaignForOneCWidgetConfirmation from '../components/campaigns_for_one_c_widget/ExcludeCampaignForOneCWidgetConfirmation';
import p_widgets_for_all_campaignsExcludePWidgetConfirmation from '../components/p_widgets_for_all_campaigns/ExcludePWidgetConfirmation';
import c_widgets_for_all_campaignsExcludeCWidgetConfirmation from '../components/c_widgets_for_all_campaigns/ExcludeCWidgetConfirmation';
import ExcludeOneCampaignForAllBlacklistedPWidgets from '../components/ExcludeOneCampaignForAllBlacklistedPWidgets';
import RedirectToHome from '../components/RedirectToHome';

const AppRouter = () => (
  <BrowserRouter>
    <div>
      <Switch>
        <Route path="/login" component={Login} />
        <PrivateRoute
          path="/campaignsforallcampaigns"
          Component={campaigns_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/countriesforallcampaigns"
          Component={countries_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/daysforonecampaign/:volid"
          Component={days_for_one_campaignHome}
        />
        <PrivateRoute
          path="/pwidgetsforonecampaign/:volid/:name"
          Component={p_widgets_for_one_campaignHome}
        />
        <PrivateRoute
          path="/pwidgetsforallcampaigns"
          Component={p_widgets_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/cwidgetsforallcampaigns"
          Component={c_widgets_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/cwidgetsforonepwidget/:pWidgetID"
          Component={c_widgets_for_one_p_widgetHome}
        />
        <PrivateRoute
          path="/campaignsforonepwidget/:pWidgetID"
          Component={campaigns_for_one_p_widgetHome}
        />
        <PrivateRoute
          path="/campaignsforoneoffer/:offerID/:fullOfferName"
          Component={campaigns_for_one_offerHome}
        />
        <PrivateRoute
          path="/offersforallcampaigns"
          Component={offers_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/offersforonecampaign/:volID/:campaignName"
          Component={offers_for_one_campaignHome}
        />
        <PrivateRoute
          path="/offersforoneflow/:offerFlow"
          Component={offers_for_one_flowHome}
        />
        <PrivateRoute
          path="/campaignsforonecwidget/:widgetID"
          Component={campaigns_for_one_c_widgetHome}
        />
        <PrivateRoute
          path="/adsforonecampaign/:volid/:name"
          Component={ads_for_one_campaignHome}
        />
        <PrivateRoute
          path="/adsforallcampaigns"
          Component={ads_for_all_campaignsHome}
        />
        <PrivateRoute
          path="/campaignsforonead/:adImage"
          Component={campaigns_for_one_adHome}
        />
        <PrivateRoute
          path="/listpwidgetconfirmation/:pWidgetID/:listType"
          Component={p_widgets_for_all_campaignsListPWidgetConfirmation}
        />
        <PrivateRoute
          path="/listcwidgetconfirmation/:cWidgetID/:listType"
          Component={c_widgets_for_all_campaignsListCWidgetConfirmation}
        />
        <PrivateRoute
          path="/excludecampaignconfirmation/:pWidgetID/:mgidCampaignID"
          Component={campaigns_for_one_p_widgetExcludeCampaignConfirmation}
        />
        <PrivateRoute
          path="/excludecampaignforonecwidgetconfirmation/:cWidgetID/:mgidCampaignID"
          Component={
            campaigns_for_one_c_widgetExcludeCampaignForOneCWidgetConfirmation
          }
        />
        <PrivateRoute
          path="/excludepwidgetconfirmation/:pWidgetID"
          Component={p_widgets_for_all_campaignsExcludePWidgetConfirmation}
        />
        <PrivateRoute
          path="/excludecwidgetconfirmation/:cWidgetID"
          Component={c_widgets_for_all_campaignsExcludeCWidgetConfirmation}
        />
        <PrivateRoute
          path="/excludeonecampaignforallblacklistedpwidgets"
          Component={ExcludeOneCampaignForAllBlacklistedPWidgets}
        />
        // redirect to campaigns_for_all_campaigns if url doesn't match a route
        <PrivateRoute Component={RedirectToHome} />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;
