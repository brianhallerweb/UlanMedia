import React from "react";
import NavItem from "./NavItem";

const navItems = [
  "Yesterday",
  "7 days",
  "30 days",
  "90 days",
  "180 days"
];

const NavBar = () => (
    <ul>{navItems.map(navItem => <NavItem key={navItem} text={navItem} />)}</ul>
);

export default NavBar;
