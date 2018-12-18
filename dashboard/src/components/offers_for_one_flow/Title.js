//@format
import React from 'react';

const Title = ({offerFlow, volRequestDates}) => (
  <div className="title">
    <h3>offers for one flow {offerFlow}</h3>
    {volRequestDates && <p>(vol: {volRequestDates})</p>}
  </div>
);

export default Title;
