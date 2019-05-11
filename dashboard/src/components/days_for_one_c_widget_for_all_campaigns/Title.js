//@format
import React from 'react';
import {Helmet} from 'react-helmet';

const Title = props => {
  let title = `days for one c widget for all campaigns (${props.cWidgetID})`;
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
