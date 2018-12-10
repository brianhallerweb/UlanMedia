//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

const ConditionCheckboxes = ({
  toggleCondition,
  c1,
  c2,
  c3,
  c4,
  c5,
  c6,
  c7,
  c8,
}) => {
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
        <span>
          {
            'Widget global status is whitelisted --- (globalStatus == "whitelist")'
          }
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c3"
          checked={c3}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {
            'Widget global status is greylisted --- (globalStatus == "greylist")'
          }
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c4"
          checked={c4}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {
            'Widget global status is blacklisted --- (globalStatus == "blacklist")'
          }
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c5"
          checked={c5}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>{'Widget leads is 0 --- (leads == 0)'}</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c6"
          checked={c6}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>{'Widget leadCVR is less than 0.25% --- (leadCVR < 0.25)'}</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c7"
          checked={c7}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>{'Widget saleCPA is more than $500 --- (saleCPA > 500)'}</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c8"
          checked={c8}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>{'Widget lost more than $200 --- (profit < 200)'}</span>
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
