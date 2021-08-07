import React from 'react';
import { NavLink } from 'react-router-dom';
import routes from './routes';
import './sidebar.scss';
    
function Sidebar(props) {
    return (
        <nav className="col-md-3 col-lg-2 sidebar ">
            <div className="sidebar-sticky pt-3">
                <ul className="nav flex-column">
                    {routes.map((route, index)=>(
                        <li className="nav-item" key={index}>
                            <NavLink
                                to={route.path}
                                exact = {route.exact}
                                className="nav-link"
                                activeClassName="active">
                                {route.label}
                            </NavLink>
                        </li>
                    ))}
                </ul>
            </div>
        </nav>
    )
}

export default Sidebar

