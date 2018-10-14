import React from "react";
import { Redirect } from "react-router-dom";

const RedirectToHome = () => (
  <div>
    <Redirect to="/campaigns" />
  </div>
);

export default RedirectToHome;


