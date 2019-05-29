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
          <DatesDropdown
            selectDateRange={this.props.selectDateRange}
            dateRange={this.props.dateRange}
          />
          <input type="submit" value="submit" disabled={this.props.loading} />
        </form>
      </div>
    );
  }
}

export default NavBar;
