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
  c6,
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
        <span>Widget classification is </span>
        <select
          onChange={e => setConditionValue('c1Value', e.target.value)}
          defaultValue={c1Value}>
          <option value="not yet">not yet</option>
          <option value="white">white</option>
          <option value="black">black</option>
          <option value="grey">grey</option>
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
          defaultValue={c1Value}>
          <option value="not yet listed">not yet listed</option>
          <option value="p_whitelist">p_whitelist</option>
          <option value="p_greylist">p_greylist</option>
          <option value="p_blacklist">p_blacklist</option>
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
          {'Widget cost more than $'}
          <input
            className="inputBox"
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
            className="inputBox"
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
        Widget has included bad campaigns
      </div>

      <div>
        <input
          type="checkbox"
          name="c6"
          checked={c6}
          onChange={e => toggleCondition(e.target.name)}
        />
        Widget classification doesn't match global status
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
