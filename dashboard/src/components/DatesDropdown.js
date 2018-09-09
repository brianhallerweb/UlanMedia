//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

const DatesDropdown = ({selectDateRange}) => (
  <div>
    <select onChange={e => selectDateRange(e.target.value)}>
      <option value="yesterday_by_campaigns_data">Yesterday</option>
      <option value="seven_by_campaigns_data">7 days</option>
      <option value="thirty_by_campaigns_data">30 days</option>
      <option value="ninety_by_campaigns_data">90 days</option>
      <option value="oneeighty_by_campaigns_data">180 days</option>
    </select>
  </div>
);

export default DatesDropdown;
