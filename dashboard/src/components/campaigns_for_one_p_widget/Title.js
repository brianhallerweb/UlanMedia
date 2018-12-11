//@format
import React from 'react';

const Title = ({ID, mgidRequestDates, volRequestDates}) => (
  <div>
    <h3>campaigns for one p widget ({ID})</h3>
    {volRequestDates && <p>(vol: {volRequestDates})</p>}
    {mgidRequestDates && <p>(mgid: {mgidRequestDates})</p>}
  </div>
);

export default Title;
