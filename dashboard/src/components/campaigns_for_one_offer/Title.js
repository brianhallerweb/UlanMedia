//@format
import React from 'react';

const Title = ({offerID, volRequestDates}) => (
  <div className="title">
    <h3>campaigns for one offer ({offerID})</h3>
    {volRequestDates && <p>(vol: {volRequestDates})</p>}
  </div>
);

export default Title;
