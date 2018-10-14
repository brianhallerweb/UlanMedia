import React from "react";
import NavItem from "./NavItem";

const navItems = [
  "Campaigns",
  "Widgets",
  "Offers",
  "Ads"
];

const NavBar = () => (
  <div>
    <ul>{navItems.map(navItem => <NavItem key={navItem} text={navItem} />)}</ul>
  </div>
);

export default NavBar;
