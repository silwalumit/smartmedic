import React from 'react'
import { Route, Redirect } from 'react-router-dom';
import { isAuthenticated } from '../../helpers/authHelpers';

function ProtectedRoute({ children, ...rest }) {
    return (
        <Route
            {...rest}
            render={({ location }) =>
                isAuthenticated() ? (children) : (
                    <Redirect to={{
                        pathname: "/login",
                        state: {
                            from: location
                        }
                    }} />
                )
            }
        />
    )
}

export default ProtectedRoute