import React from 'react';
import { NavLink } from 'react-router-dom';
import routes from './routes';
import './sidebar.css';
    
function Sidebar(props) {
    return (
        <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
            <div class="position-sticky pt-3">
                <ul class="nav flex-column">
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

