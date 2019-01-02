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
  c4,
  c4Value,
  c5,
  c5Value,
  c6,
  c6Value1,
  c6Value2,
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
        <span>Widget status is </span>
        <select
          onChange={e => setConditionValue('c1Value', e.target.value)}
          defaultValue={c1Value}>
          <option value="all">all</option>
          <option value="included">included</option>
          <option value="excluded">excluded</option>
        </select>
      </div>

      <div>
        <input
          type="checkbox"
          name="c2"
          checked={c2}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Widget global status is </span>
        <select
          onChange={e => setConditionValue('c2Value', e.target.value)}
          defaultValue={c2Value}>
          <option value="not yet listed">not yet listed</option>
          <option value="whitelist">whitelist</option>
          <option value="greylist">greylist</option>
          <option value="blacklist">blacklist</option>
        </select>
      </div>

      <div>
        <input
          type="checkbox"
          name="c3"
          checked={c3}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Widget cost is more than $'}
          <input
            type="number"
            name="c3Value"
            min="0"
            max="100"
            step="10"
            value={c3Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
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
          {'Widget lost more than $'}
          <input
            type="number"
            name="c4Value"
            min="0"
            max="100"
            step="10"
            value={c4Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c5"
          checked={c5}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Widget leadCVR is less than or equal to '}
          <input
            type="number"
            name="c5Value"
            min="0"
            max=".50"
            step=".25"
            value={c5Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'%'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c6"
          checked={c6}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Widget has clicks greater than or equal to '}
          <input
            type="number"
            name="c6Value1"
            min="200"
            max="2000"
            step="20"
            value={c6Value1}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {' OR cost greater than or equal to $'}
          <input
            type="number"
            name="c6Value2"
            min="0"
            max="100"
            step="5"
            value={c6Value2}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
        </span>
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
