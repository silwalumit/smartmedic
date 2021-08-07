import React, { Component } from 'react';
import { Route, Switch } from 'react-router';
import Header from './Header/Header';
import routes from './Sidebar/routes';
import Sidebar from './Sidebar/Sidebar';

class Home extends Component {
    render() {
        return (
            <>
                <Header />
                <div className="container-fluid">
                    <div className="row">
                        <Sidebar />
                        <main className="col-md-9 col-lg-10 px-3 py-3">
                            <Switch>
                                {routes.map((route, index) => (
                                    <Route
                                        key={index}
                                        path={route.path}
                                        exact={route.exact}
                                        children={< route.component />}
                                    ></Route>
                                ))}
                            </Switch>
                        </main>
                    </div>
                </div>
            </>
        );
    }
}

export default Home;