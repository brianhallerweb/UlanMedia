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
          <DatesDropdown
            selectDateRange={this.props.selectDateRange}
            dateRange={this.props.dateRange}
          />
          <p>
            Widget cost greater than{' '}
            <input
              type="number"
              name="quantity"
              min="0"
              max="100"
              step="1"
              value={this.props.precondition}
              onChange={e => this.props.selectPrecondition(e.target.value)}
            />
          </p>
          <ConditionCheckboxes
            toggleCondition={this.props.toggleCondition}
            c1={this.props.c1}
            c2={this.props.c2}
            c3={this.props.c3}
            c4={this.props.c4}
            c5={this.props.c5}
            c6={this.props.c6}
            c7={this.props.c7}
            c8={this.props.c8}
          />
          <input type="submit" value="submit" disabled={this.props.loading} />
        </form>
      </div>
    );
  }
}

export default NavBar;
