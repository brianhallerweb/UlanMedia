//@format
import React from 'react';

const Title = ({campaignName, volRequestDates}) => (
  <div className="title">
    <h3>offers for one campaign ({campaignName})</h3>
    {volRequestDates && <p>(vol: {volRequestDates})</p>}
  </div>
);

export default Title;
