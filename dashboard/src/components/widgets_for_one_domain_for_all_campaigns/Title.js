//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = ({volRequestDates, mgidRequestDates, domain}) => {
  const title = `widgets for one domain for all campaigns`;
  return (
    <div>
      <div className="title">
        <Helmet>
          <meta charSet="utf-8" />
          <title>{title}</title>
        </Helmet>
        <h3>{title}</h3>
        {volRequestDates && <p>(vol: {volRequestDates})</p>}
        {mgidRequestDates && <p>(mgid: {mgidRequestDates})</p>}
      </div>
      <p>{domain}</p>
    </div>
  );
};

export default Title;
