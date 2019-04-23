//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

const InternalLink = ({className, activeClassName, to, target, label}) => (
  <div className={className}>
    <NavLink
      onClick={e => e.stopPropagation()}
      to={to}
      activeClassName={activeClassName}
      target={target}>
      {label}
    </NavLink>
  </div>
);

export default InternalLink;
