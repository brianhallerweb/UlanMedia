//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

const ConditionCheckboxes = ({
  toggleCondition,
  setConditionValue,
  c1,
  c1Value,
  c2,
  c2Value,
  c3,
  c3Value,
}) => {
  return (
    <div style={{paddingTop: 15, paddingBottom: 15}}>
      <div>
        <input
          type="checkbox"
          name="c1"
          checked={c1}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Widget cost more than $'}
          <input
            type="number"
            name="c1Value"
            min="0"
            max="100"
            step="10"
            value={c1Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
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
          {'Widget lost more than $'}
          <input
            type="number"
            name="c2Value"
            min="0"
            max="100"
            step="10"
            value={c2Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
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
          {'Widget leadCVR is less than or equal to '}
          <input
            type="number"
            name="c3Value"
            min="0"
            max=".50"
            step=".25"
            value={c3Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'%'}
        </span>
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
