import React from 'react'
import { Redirect, Route } from 'react-router'
import { isAuthenticated } from '../../helpers/authHelpers'

function PublicRoute({ children, ...rest }) {
    return (
        <Route
            {...rest}
            render={({ location }) =>
                !isAuthenticated() ? (children) : (
                    <Redirect to="/" />
                )
            } 
        />
    )
}

export default PublicRoute
