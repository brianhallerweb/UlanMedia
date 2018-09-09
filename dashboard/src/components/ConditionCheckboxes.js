//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

const ConditionCheckboxes = ({toggleCondition}) => {
  return (
    <div>
      <div>
        <input
          type="checkbox"
          name="c1"
          checked
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {
            'Campaign has more than 1000 clicks but no leads --- (clicks > 1000 AND leads = 0)'
          }
        </span>
      </div>
      <div>
        <input
          type="checkbox"
          name="c2"
          checked
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {
            'Campaign cost is more than a third of maxSaleCPA AND leadCPA is more than 2x maxLeadCPA --- (cost > 0.3*maxSaleCPA AND leadCPA > 2*maxLeadCPA)'
          }
        </span>
      </div>
      <div>
        <input
          type="checkbox"
          name="c3"
          checked
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {
            'Campaign cost is more than half of maxSaleCPA AND leadCPA is more than 1.5x maxLeadCPA --- (cost > 0.5*maxSaleCPA AND leadCPA > 1.5*maxLeadCPA)'
          }
        </span>
      </div>
      <div>
        <input
          type="checkbox"
          name="c4"
          checked
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {
            'Campaign cost is more than 2x maxSaleCPA AND leadCPA is more than maxLeadCPA --- (cost > 2*maxSaleCPA AND leadCPA > maxLeadCPA)'
          }
        </span>
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
