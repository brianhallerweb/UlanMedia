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
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {
            'Campaign is losing more than one maxSaleCPA --- (profit < -1*maxSaleCpa)'
          }
        </span>
      </div>
      <div>
        <input
          type="checkbox"
          name="c2"
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
          name="c3"
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {
            'Campaign cost is more than one third of maxSaleCPA AND leadCPA is more than double maxLeadCPA --- (cost > 0.3*maxSaleCPA AND leadCPA > 2*maxLeadCPA)'
          }
        </span>
      </div>
      <div>
        <input
          type="checkbox"
          name="c4"
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {
            'Campaign cost is more than one half of maxSaleCPA AND leadCPA is more than 1.5 maxLeadCPA --- cost > 0.5*maxSaleCPA AND leadCPA > 1.5*maxLeadCPA'
          }
        </span>
      </div>
      <div>
        <input
          type="checkbox"
          name="c5"
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {
            'Campaign cost is more than double maxSaleCPA AND leadCPA is more than maxLeadCPA --- cost > 2*maxSaleCPA AND leadCPA > maxLeadCPA'
          }
        </span>
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
