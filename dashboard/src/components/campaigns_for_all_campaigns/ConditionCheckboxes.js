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
  c7Value,
  c8,
  c8Value,
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
  c15,
  c15Value,
  c16,
  c16Value,
  c17,
  c17Value,
  c18,
  c18Value,
  c19,
  c19Value,
  c20,
  c20Value,
  c21,
  c21Value,
  c22,
  c22Value,
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
        <span>Campaign classification is </span>
        <select
          onChange={e => setConditionValue('c1Value', e.target.value)}
          defaultValue={c1Value}>
          <option value="not yet">not yet</option>
          <option value="good">good</option>
          <option value="bad">bad</option>
        </select>
      </div>

      <div>
        <input
          type="checkbox"
          name="c2"
          checked={c2}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign cost more than $'}
          <input
            className="inputBox"
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

      <div>
        <input
          type="checkbox"
          name="c3"
          checked={c3}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign lost more than $'}
          <input
            className="inputBox"
            type="number"
            name="c3Value"
            min="0"
            max="1000"
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
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign sales more than '}
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
        </span>
      </div>

      <p>-----------------------------------------------------</p>

      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        need to lower cost or tighten targeting:
      </p>

      <div>
        <input
          type="checkbox"
          name="c5"
          checked={c5}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign CPC is equal to or greater than EPC plus '}
          <input
            className="inputBox"
            type="number"
            name="c5Value"
            min="0"
            max="l000"
            step="1"
            value={c5Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [CPC >= EPC+(EPC*0.30)]'}
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
          {'Campaign CPL is equal to or greater than EPL plus '}
          <input
            className="inputBox"
            type="number"
            name="c6Value"
            min="0"
            max="l000"
            step="1"
            value={c6Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [CPL >= EPL+(EPL*0.30)]'}
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
          {'Campaign CPS is equal to or greater than EPS plus '}
          <input
            className="inputBox"
            type="number"
            name="c7Value"
            min="0"
            max="l000"
            step="1"
            value={c7Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [CPS >= EPS+(EPS*0.30)]'}
        </span>
      </div>

      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        can raise cost or loosen targeting:
      </p>
      <div>
        <input
          type="checkbox"
          name="c8"
          checked={c8}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign CPC is equal to or less than EPC minus '}
          <input
            className="inputBox"
            type="number"
            name="c8Value"
            min="0"
            max="l000"
            step="1"
            value={c8Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [CPC <= EPC-(EPC*0.30)]'}
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
          {'Campaign CPL is equal to or less than EPL minus '}
          <input
            className="inputBox"
            type="number"
            name="c9Value"
            min="0"
            max="l000"
            step="1"
            value={c9Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [CPL <= EPL-(EPL*0.30)]'}
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
          {'Campaign CPS is equal to or less than EPS minus '}
          <input
            className="inputBox"
            type="number"
            name="c10Value"
            min="0"
            max="l000"
            step="1"
            value={c10Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [CPS <= EPS-(EPS*0.30)]'}
        </span>
      </div>

      <p>-----------------------------------------------------</p>

      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        need to lower max per click/lead/sale:
      </p>
      <div>
        <input
          type="checkbox"
          name="c11"
          checked={c11}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPC is equal to or greater than EPC plus '}
          <input
            className="inputBox"
            type="number"
            name="c11Value"
            min="0"
            max="l000"
            step="1"
            value={c11Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [MPC >= EPC+(EPC*0.30)]'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c12"
          checked={c12}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPL is equal to or greater than EPL plus '}
          <input
            className="inputBox"
            type="number"
            name="c12Value"
            min="0"
            max="l000"
            step="1"
            value={c12Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [MPL >= EPL+(EPL*0.30)]'}
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
          {'Campaign MPS is equal to or greater than EPS plus '}
          <input
            className="inputBox"
            type="number"
            name="c13Value"
            min="0"
            max="l000"
            step="1"
            value={c13Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [MPS >= EPS+(EPS*0.30)]'}
        </span>
      </div>

      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        can raise max per click/lead/sale:
      </p>
      <div>
        <input
          type="checkbox"
          name="c14"
          checked={c14}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPC is equal to or less than EPC minus '}
          <input
            className="inputBox"
            type="number"
            name="c14Value"
            min="0"
            max="l000"
            step="1"
            value={c14Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [MPC <= EPC-(EPC*0.30)]'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c15"
          checked={c15}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPL is equal to or less than EPL minus '}
          <input
            className="inputBox"
            type="number"
            name="c15Value"
            min="0"
            max="l000"
            step="1"
            value={c15Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [MPL <= EPL-(EPL*0.30)]'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c16"
          checked={c16}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign MPS is equal to or less than EPS minus '}
          <input
            className="inputBox"
            type="number"
            name="c16Value"
            min="0"
            max="l000"
            step="1"
            value={c16Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [MPS <= EPS-(EPS*0.30)]'}
        </span>
      </div>

      <p>-----------------------------------------------------</p>

      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        need to lower cost or tighten targeting or raise max per
        click/lead/sale:
      </p>
      <div>
        <input
          type="checkbox"
          name="c17"
          checked={c17}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign CPC is equal to or greater than MPC plus '}
          <input
            className="inputBox"
            type="number"
            name="c17Value"
            min="0"
            max="l000"
            step="1"
            value={c17Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [CPC >= MPC+(MPC*0.30)]'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c18"
          checked={c18}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign CPL is equal to or greater than MPL plus '}
          <input
            className="inputBox"
            type="number"
            name="c18Value"
            min="0"
            max="l000"
            step="1"
            value={c18Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [CPL >= MPL+(MPL*0.30)]'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c19"
          checked={c19}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign CPS is equal to or greater than MPS plus '}
          <input
            className="inputBox"
            type="number"
            name="c19Value"
            min="0"
            max="l000"
            step="1"
            value={c19Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [CPS >= MPS+(MPS*0.30)]'}
        </span>
      </div>

      <p style={{marginBottom: 0, fontWeight: 'bold'}}>
        can raise cost or loosen targeting or lower max per click/lead/sale:
      </p>
      <div>
        <input
          type="checkbox"
          name="c20"
          checked={c20}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign CPC is equal to or less than MPC minus '}
          <input
            className="inputBox"
            type="number"
            name="c20Value"
            min="0"
            max="l000"
            step="1"
            value={c20Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [CPC <= MPC-(MPC*0.30)]'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c21"
          checked={c21}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign CPL is equal to or less than MPL minus '}
          <input
            className="inputBox"
            type="number"
            name="c21Value"
            min="0"
            max="l000"
            step="1"
            value={c21Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [CPL <= MPL-(MPL*0.30)]'}
        </span>
      </div>

      <div>
        <input
          type="checkbox"
          name="c22"
          checked={c22}
          onChange={e => toggleCondition(e.target.name)}
        />
        <span>
          {'Campaign CPS is equal to or less than MPS minus '}
          <input
            className="inputBox"
            type="number"
            name="c22Value"
            min="0"
            max="l000"
            step="1"
            value={c22Value}
            onChange={e => setConditionValue(e.target.name, e.target.value)}
          />
          {'% [CPS <= MPS-(MPS*0.30)]'}
        </span>
      </div>

      <p>-----------------------------------------------------</p>
    </div>
  );
};

export default ConditionCheckboxes;
