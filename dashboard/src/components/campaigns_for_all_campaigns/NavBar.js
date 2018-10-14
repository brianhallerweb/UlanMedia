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
          <p>
            Campaign lost more than{' '}
            <input
              type="number"
              name="quantity"
              min=".25"
              max="3"
              step=".25"
              value={this.props.precondition}
              onChange={e => this.props.selectPrecondition(e.target.value)}
            />
            x maxSaleCPA
          </p>
          <ConditionCheckboxes
            toggleCondition={this.props.toggleCondition}
            c1={this.props.c1}
            c2={this.props.c2}
            c3={this.props.c3}
            c4={this.props.c4}
            c5={this.props.c5}
          />
          <input
            type="submit"
            value="Submit"
            disabled={!this.props.isConditionSelected()}
          />
        </form>
      </div>
    );
  }
}

export default NavBar;
