import React from "react";
import { NavLink } from "react-router-dom";

const GlobalNavItem = ({ text }) => {
  return (
    <li className="globalNavItem">
      <NavLink to={`/${text}`} target="_blank" activeClassName="is-active">
        {text}
      </NavLink>
    </li>
  );
};

export default GlobalNavItem;
