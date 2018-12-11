//@format
import React from 'react';

const Title = ({adImage, volRequestDates}) => (
  <div className="title">
    <h3>campaigns for one ad ({adImage})</h3>
    {volRequestDates && <p>(vol: {volRequestDates})</p>}
  </div>
);

export default Title;
