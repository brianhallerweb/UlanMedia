import React from "react";
import { NavLink } from "react-router-dom";

const NavItem = ({ text }) => {
  const category = text.toLowerCase().replace(/ /g, "");
  return (
    <li>
      <NavLink to={`/${category}`} activeClassName="is-active">
        {text}
      </NavLink>
    </li>
  );
};

export default NavItem;
