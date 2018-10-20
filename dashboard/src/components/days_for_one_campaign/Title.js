//@format
import React from 'react';

const Title = props => (
  <div>
    {props.dayRecords.length > 0 && (
      <h3>days for one campaign ({props.dayRecords[0].name})</h3>
    )}
  </div>
);

export default Title;
