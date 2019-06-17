//@format
import React, {Component} from 'react';
import {NavLink} from 'react-router-dom';

const ConditionCheckboxes = ({
  toggleCondition,
  setConditionValue,
  loading,
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
  c6Value,
}) => {
  return (
    <div style={{paddingTop: 15, paddingBottom: 15}}>
      <div>
        <input
          type="checkbox"
          name="c1"
          checked={c1}
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>Widget status is </span>
        <select
          onChange={e => setConditionValue('c1Value', e.target.value)}
          defaultValue={c1Value}>
          <option value="included">included</option>
          <option value="excluded">excluded</option>
          <option value="inactive">inactive</option>
        </select>
      </div>

      <div>
        <input
          type="checkbox"
          name="c2"
          checked={c2}
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Widget cost is greater than or equal to $'}
          <input
            type="number"
            name="c2Value"
            min="0"
            max="100"
            step="1"
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
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Widget loss is greater than or equal to $'}
          <input
            type="number"
            name="c3Value"
            min="0"
            max="100"
            step="1"
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
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Widget CPL is less than or equal to MPL minus '}
          <input
            className="inputBox"
            type="number"
            name="c4Value"
            min="0"
            max="100"
            step="1"
            value={c4Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {`% [CPL <= MPL-(MPL*${c4Value})]`}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c5"
          checked={c5}
          disabled={loading}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Widget CPS is less than or equal to MPS minus '}
          <input
            className="inputBox"
            type="number"
            name="c5Value"
            min="0"
            max="100"
            step="1"
            value={c5Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {`% [CPS <= MPS-(MPS*${c5Value})]`}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c6"
          checked={c6}
          disabled={true}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Max recommended bid $'}
          <input
            className="inputBox"
            type="number"
            name="c6Value"
            min="0"
            max="10"
            step=".01"
            value={c6Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
        </span>
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
