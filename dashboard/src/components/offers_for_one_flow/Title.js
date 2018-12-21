//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = ({offerFlow, volRequestDates}) => {
  const title = `offers for one flow (${offerFlow})`;
  return (
    <div className="title">
      <Helmet>
        <meta charSet="utf-8" />
        <title>{title}</title>
      </Helmet>
      <h3>{title}</h3>
      {volRequestDates && <p>(vol: {volRequestDates})</p>}
    </div>
  );
};

export default Title;
