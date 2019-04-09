//@format
import React, {Component} from 'react';
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
          <ConditionCheckboxes
            toggleCondition={this.props.toggleCondition}
            setConditionValue={this.props.setConditionValue}
            c1={this.props.c1}
            c1Value={this.props.c1Value}
            c2={this.props.c2}
            c2Value={this.props.c2Value}
            c3={this.props.c3}
            c3Value={this.props.c3Value}
          />
          <input type="submit" value="Submit" />
        </form>
      </div>
    );
  }
}

export default NavBar;
