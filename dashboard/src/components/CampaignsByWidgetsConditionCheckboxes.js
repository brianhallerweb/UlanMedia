//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

const CampaignsByWidgetsConditionCheckboxes = ({toggleCondition, c1, c2}) => {
  return (
    <div>
      <div>
        <input
          type="checkbox"
          name="c1"
          checked={c1}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>{'Widget has 1 or more leads --- (leads > 1)'}</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c2"
          checked={c2}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>{'Widget has 1 or more sales --- (sales > 1)'}</span>
      </div>
    </div>
  );
};

export default CampaignsByWidgetsConditionCheckboxes;
