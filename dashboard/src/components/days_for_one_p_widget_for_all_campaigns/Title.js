//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = props => {
  let title = `days for one p widget for all campaigns`;
  return (
    <div>
      <div>
        <Helmet>
          <meta charSet="utf-8" />
          <title>{title}</title>
        </Helmet>
        <h3>{title}</h3>
      </div>
    </div>
  );
};

export default Title;
