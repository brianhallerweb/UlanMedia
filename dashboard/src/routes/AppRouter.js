//@format
import React from 'react';
import {BrowserRouter, Switch, Route} from 'react-router-dom';
import Title from '../components/Title';
import NavBar from '../components/NavBar';
import CampaignsRecords from '../components/CampaignsRecords';
import Home from '../components/Home';

const AppRouter = () => (
  <BrowserRouter>
    <div>
      <Title />
      <NavBar />
      <Switch>
        <Route path="/" exact={true} component={Home} />
        <Route path="/:navitem" component={CampaignsRecords} />
      </Switch>
    </div>
  </BrowserRouter>
);

export default AppRouter;
