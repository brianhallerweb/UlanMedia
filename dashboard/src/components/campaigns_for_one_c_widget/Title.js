//@format
import React from 'react';

const Title = ({ID, mgidRequestDates, volRequestDates}) => (
  <div className="title">
    <h3>campaigns for one c widget ({ID})</h3>
    {volRequestDates && <p>(vol: {volRequestDates})</p>}
    {mgidRequestDates && <p>(mgid: {mgidRequestDates})</p>}
  </div>
);

export default Title;
