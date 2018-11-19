//@format
import React, {Component} from 'react';
import DatesDropdown from './DatesDropdown';

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
            EPC greater than or equal to {' '}
            <input
              type="number"
              name="quantity"
              min="0"
              max="1"
              step=".05"
              value={this.props.precondition}
              onChange={e => this.props.selectPrecondition(e.target.value)}
            />
          </p>
          <input
            type="submit"
            value="Submit"
          />
        </form>
      </div>
    );
  }
}

export default NavBar;
