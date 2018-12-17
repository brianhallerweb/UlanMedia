//@format
import React from 'react';

const Title = ({offerName, volRequestDates}) => (
  <div className="title">
    <h3>campaigns for one offer ({offerName})</h3>
    {volRequestDates && <p>(vol: {volRequestDates})</p>}
  </div>
);

export default Title;
