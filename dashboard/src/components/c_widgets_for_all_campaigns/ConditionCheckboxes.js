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
  c6Value,
  c7,
  c7Value1,
  c7Value2,
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
          <option value="wait">wait</option>
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
          defaultValue={c2Value}>
          <option value="not yet listed">not yet listed</option>
          <option value="pc_whitelist">pc_whitelist</option>
          <option value="pc_greylist">pc_greylist</option>
          <option value="pc_blacklist">pc_blacklist</option>
          <option value="p_whitelist">p_whitelist</option>
          <option value="p_greylist">p_greylist</option>
          <option value="p_blacklist">p_blacklist</option>
          <option value="c_whitelist">c_whitelist</option>
          <option value="c_greylist">c_greylist</option>
          <option value="c_blacklist">c_blacklist</option>
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
        <span>
          {'Widget leadCVR is less than or equal to '}
          <input
            className="inputBox"
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
          {'Widget saleCPA is more than $'}
          <input
            className="inputBox"
            type="number"
            name="c6Value"
            min="200"
            max="500"
            step="20"
            value={c6Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c7"
          checked={c7}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Widget has clicks greater than or equal to '}
          <input
            style={{width: 40}}
            type="number"
            name="c7Value1"
            min="200"
            max="2000"
            step="20"
            value={c7Value1}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {' OR cost greater than or equal to $'}
          <input
            className="inputBox"
            type="number"
            name="c7Value2"
            min="0"
            max="100"
            step="5"
            value={c7Value2}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
        </span>
      </div>
    </div>
  );
};

export default ConditionCheckboxes;
