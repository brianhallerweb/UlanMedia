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
          <ConditionCheckboxes
            toggleCondition={this.props.toggleCondition}
            setConditionValue={this.props.setConditionValue}
            loading={this.props.loading}
            c1={this.props.c1}
            c1Value={this.props.c1Value}
            c2={this.props.c2}
            c2Value={this.props.c2Value}
            c3={this.props.c3}
            c3Value={this.props.c3Value}
            c4={this.props.c4}
            c4Value={this.props.c4Value}
            c5={this.props.c5}
            c5Value={this.props.c5Value}
            c6={this.props.c6}
            c6Value={this.props.c6Value}
            c7={this.props.c7}
            c7Value={this.props.c7Value}
            c8={this.props.c8}
            c9={this.props.c9}
            c9Value={this.props.c9Value}
          />
          <input type="submit" value="submit" disabled={this.props.loading} />
        </form>
      </div>
    );
  }
}

export default NavBar;
