//@format
import React from 'react';

const Title = ({name, volRequestDates}) => (
  <div className="title">
    <h3>ads for one campaign ({name})</h3>
    {volRequestDates && <p>(vol: {volRequestDates})</p>}
  </div>
);

export default Title;
