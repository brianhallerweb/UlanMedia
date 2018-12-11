//@format
import React from 'react';

const Title = ({name, mgidRequestDates, volRequestDates}) => (
  <div className="title">
    <h3>p widgets for one campaign ({name})</h3>
    {volRequestDates && <p>(vol: {volRequestDates})</p>}
    {mgidRequestDates && <p>(mgid: {mgidRequestDates})</p>}
  </div>
);

export default Title;
