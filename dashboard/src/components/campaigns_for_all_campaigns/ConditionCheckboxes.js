//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

const ConditionCheckboxes = ({
  toggleCondition,
  setConditionValue,
  c1,
  c2,
  c3,
  c4,
  c5,
  c6,
  c7,
  c7Value,
  c8,
  c8Value,
  c9,
  c9Value,
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
        <span>Campaign CPC is more than EPC</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c2"
          checked={c2}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Campaign CPL is more than EPL</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c3"
          checked={c3}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Campaign CPS is more than EPS</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c4"
          checked={c4}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Campaign EPC is more than CPC</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c5"
          checked={c5}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Campaign EPL is more than CPL</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c6"
          checked={c6}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Campaign EPS is more than CPS</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c7"
          checked={c7}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPC differs more than '}
          <input
            type="number"
            name="c7Value"
            min="0"
            max="1"
            step=".01"
            value={c7Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {' from EPC'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c8"
          checked={c8}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPL differs more than '}
          <input
            type="number"
            name="c8Value"
            min="0"
            max="10"
            step="1"
            value={c8Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {' from EPL'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c9"
          checked={c9}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPS differs more than '}
          <input
            type="number"
            name="c9Value"
            min="0"
            max="1000"
            step="25"
            value={c9Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {' from EPS'}
        </span>
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
