//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

const ConditionCheckboxes = ({toggleCondition, c1, c2, c3, c4, c5}) => {
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
            'Ad lost more than 20  --- (cost < 20)'
          }
        </span>
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
