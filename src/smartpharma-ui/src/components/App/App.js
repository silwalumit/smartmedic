import React, { Suspense, lazy } from "react";
import {
    BrowserRouter as Router,
    Switch,
} from 'react-router-dom'

import PublicRoute from "../common/PublicRoute";
import PrivateRoute from "../common/ProtectedRoute";
const Login = lazy(() => import('../Login/Login'));
const Home = lazy(() => import('../Home/Home'));

const App = () => {
    return (
        <Router>
            <Suspense fallback={<div>Loading...</div>}>
                <Switch>
                    <PublicRoute path="/login" >
                        <Login />
                    </PublicRoute>
                    <PrivateRoute path="/">
                        <Home />
                    </PrivateRoute>
                </Switch>
            </Suspense>
        </Router>
        
    );
}

export default App;