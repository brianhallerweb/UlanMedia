import React from "react";
import GlobalNavItem from "./GlobalNavItem";

const globalNavItems = [
  "campaigns",
  "widgets",
  "offers",
  "ads"
];

const GlobalNavBar = () => (
    <div className="globalNavBar">{globalNavItems.map(globalNavItem => <GlobalNavItem key={globalNavItem} text={globalNavItem} />)}</div>
);

export default GlobalNavBar;
