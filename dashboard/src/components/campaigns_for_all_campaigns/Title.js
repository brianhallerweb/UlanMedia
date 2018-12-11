//@format
import React from 'react';

const Title = ({volRequestDates, mgidRequestDates}) => (
  <div className="title">
    <h3>campaigns for all campaigns</h3>
    {volRequestDates && <p>(vol: {volRequestDates})</p>}
    {mgidRequestDates && <p>(mgid: {mgidRequestDates})</p>}
  </div>
);

export default Title;
