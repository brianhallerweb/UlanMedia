import React from "react";
import { Redirect } from "react-router-dom";

const RedirectToCampaignsHome = () => (
  <div>
    <Redirect to="/campaigns" />
  </div>
);

export default RedirectToCampaignsHome;


