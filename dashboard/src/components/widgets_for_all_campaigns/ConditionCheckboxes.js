//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

const ConditionCheckboxes = ({toggleCondition, c1, c2, c3, c4}) => {
  return (
    <div>
      <div>
        <input
          type="checkbox"
          name="c1"
          checked={c1}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {
            'Widget global status is Not Yet Listed --- (globalStatus == "not yet listed")'
          }
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c2"
          checked={c2}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>{'Widget leads is 0 --- (leads == 0)'}</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c3"
          checked={c3}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>{'Widget leadCVR is less than .25% --- (leadCVR < .25)'}</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c4"
          checked={c4}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>{'Widget saleCPA is more than $500 --- (saleCPA > 500)'}</span>
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
