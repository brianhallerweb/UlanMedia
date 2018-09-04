import React from "react";
import { NavLink } from "react-router-dom";

const NavItem = ({ text }) => {
  const report = text.toLowerCase().replace(/ /g, "");
  return (
    <li>
      <NavLink to={`/${report}`} activeClassName="is-active">
        {text}
      </NavLink>
    </li>
  );
};

export default NavItem;


