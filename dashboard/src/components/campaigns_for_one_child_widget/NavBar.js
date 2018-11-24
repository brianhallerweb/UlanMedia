//@format
import React, {Component} from 'react';
import DatesDropdown from './DatesDropdown';
import ConditionCheckboxes from './ConditionCheckboxes';

class NavBar extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div>
        <form
          onSubmit={e => {
            e.preventDefault();
            this.props.submitForm();
          }}>
          <DatesDropdown selectDateRange={this.props.selectDateRange} />
          <select
            onChange={e => this.props.selectPrecondition2(e.target.value)}
            defaultValue="all">
            <option value="all">Status = all</option>
            <option value="included">Status = included</option>
            <option value="excluded">Status = excluded</option>
          </select>
          <p>
            Widget cost greater than
            <input
              type="number"
              name="quantity"
              min="0"
              max="10"
              step="1"
              value={this.props.precondition}
              onChange={e => this.props.selectPrecondition(e.target.value)}
            />
          </p>
          <ConditionCheckboxes
            toggleCondition={this.props.toggleCondition}
            c1={this.props.c1}
            c2={this.props.c2}
          />
          <input type="submit" value="submit" disabled={this.props.loading} />
        </form>
      </div>
    );
  }
}

export default NavBar;
