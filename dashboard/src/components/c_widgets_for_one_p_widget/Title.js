//@format
import React from 'react';

const Title = ({pWidgetID, mgidRequestDates, volRequestDates}) => (
  <div>
    <h3>c widgets for one p widget ({pWidgetID})</h3>
    {volRequestDates && <p>(vol: {volRequestDates})</p>}
    {mgidRequestDates && <p>(mgid: {mgidRequestDates})</p>}
  </div>
);

export default Title;
