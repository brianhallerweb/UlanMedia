//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

const CampaignsByWidgetsDatesDropdown = ({selectDateRange}) => (
  <div>
    <select
      onChange={e => selectDateRange(e.target.value)}
      defaultValue="seven">
      <option value="yesterday">Yesterday</option>
      <option value="seven">7 days</option>
      <option value="thirty">30 days</option>
      <option value="ninety">90 days</option>
      <option value="oneeighty">180 days</option>
    </select>
  </div>
);

export default CampaignsByWidgetsDatesDropdown;
