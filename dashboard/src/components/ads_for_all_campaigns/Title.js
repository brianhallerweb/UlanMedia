//@format
import React from 'react';

const Title = ({volRequestDates}) => (
  <div className="title">
    <h3>ads for all campaigns</h3>
    {volRequestDates && <p>(vol: {volRequestDates})</p>}
  </div>
);

export default Title;
