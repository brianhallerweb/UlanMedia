//@format
import React from 'react';

const Title = ({volRequestDates, mgidRequestDates}) => (
  <div>
    <h3>p widgets for all campaigns</h3>
    {volRequestDates && <p>(vol: {volRequestDates})</p>}
    {mgidRequestDates && <p>(mgid: {mgidRequestDates})</p>}
  </div>
);

export default Title;
