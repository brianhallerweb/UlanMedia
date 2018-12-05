//@format
import React from 'react';
import {NavLink} from 'react-router-dom';

const GlobalNavBar = () => (
  <div className="globalNavBar">
    <li className="globalNavItem">
      <NavLink to={'campaigns'} target="_blank" activeClassName="is-active">
        campaigns
      </NavLink>
    </li>

    <li className="globalNavItem">
      <NavLink
        to={'pwidgetsforallcampaigns'}
        target="_blank"
        activeClassName="is-active">
        p widgets
      </NavLink>
    </li>

    <li className="globalNavItem">
      <NavLink to={'offers'} target="_blank" activeClassName="is-active">
        offers
      </NavLink>
    </li>

    <li className="globalNavItem">
      <NavLink to={'ads'} target="_blank" activeClassName="is-active">
        ads
      </NavLink>
    </li>
  </div>
);

export default GlobalNavBar;
