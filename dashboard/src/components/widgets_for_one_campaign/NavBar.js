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
	  <span>Status </span>
          <select
            onChange={e => this.props.selectPrecondition2(e.target.value)}
            defaultValue="all">
            <option value="all">all</option>
            <option value="included">included</option>
            <option value="excluded">excluded</option>
          </select>
          <p>
            Widget lost more than{' '}
            <input
              type="number"
              name="quantity"
              min=".25"
              max="4"
              step=".25"
              value={this.props.precondition}
              onChange={e => this.props.selectPrecondition(e.target.value)}
            />
            x maxLeadCPA ($
            {this.props.maxLeadCPA})
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
