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
  c4,
  c5,
  c6,
  c7,
  c8,
  c9,
  c9Value,
  c10,
  c10Value,
  c11,
  c11Value,
  c12,
  c12Value,
  c13,
  c13Value,
  c14,
  c14Value,
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
          {'Campaign cost more than '}
          <input
            type="number"
            name="c1Value"
            min="0"
            max="1000"
            step="1"
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
          {'Campaign lost more than '}
          <input
            type="number"
            name="c2Value"
            min="0"
            max="1000"
            step="1"
            value={c2Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
        </span>
      </div>

      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        need to lower cost or tighten targeting:
      </p>
      <div>
        <input
          type="checkbox"
          name="c3"
          checked={c3}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Campaign CPC is more than EPC</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c4"
          checked={c4}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Campaign CPL is more than EPL</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c5"
          checked={c5}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Campaign CPS is more than EPS</span>
      </div>

      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        can raise cost or loosen targeting:
      </p>
      <div>
        <input
          type="checkbox"
          name="c6"
          checked={c6}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Campaign EPC is more than CPC</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c7"
          checked={c7}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Campaign EPL is more than CPL</span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c8"
          checked={c8}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Campaign EPS is more than CPS</span>
      </div>

      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        need to lower max per click/lead/sale:
      </p>
      <div>
        <input
          type="checkbox"
          name="c9"
          checked={c9}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPC is '}
          <input
            type="number"
            name="c9Value"
            min="0"
            max="1"
            step=".01"
            value={c9Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {' greater than EPC'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c10"
          checked={c10}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPL is '}
          <input
            type="number"
            name="c10Value"
            min="0"
            max="10"
            step="1"
            value={c10Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {' greater than EPL'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c11"
          checked={c11}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPS is '}
          <input
            type="number"
            name="c11Value"
            min="0"
            max="1000"
            step="25"
            value={c11Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {' greater than EPS'}
        </span>
      </div>

      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        can raise max per click/lead/sale:
      </p>
      <div>
        <input
          type="checkbox"
          name="c12"
          checked={c12}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPC is '}
          <input
            type="number"
            name="c12Value"
            min="0"
            max="1"
            step=".01"
            value={c12Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {' less than EPC'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c13"
          checked={c13}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPL is '}
          <input
            type="number"
            name="c13Value"
            min="0"
            max="10"
            step="1"
            value={c13Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {' less than EPL'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c14"
          checked={c14}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPS is '}
          <input
            type="number"
            name="c14Value"
            min="0"
            max="1000"
            step="25"
            value={c14Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {' less than EPS'}
        </span>
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
