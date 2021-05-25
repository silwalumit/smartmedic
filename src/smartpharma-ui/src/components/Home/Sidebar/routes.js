import { lazy } from "react";
const Dashboard = lazy(() => import('../../Dashboard/Dashboard'))

const routes = [
    {
        path: '/',
        label: 'Dashboard',
        exact:true,
        component: () => <Dashboard />
    },
    {
        path: '/sales',
        label: 'Sales',
        exact:true,
        component: () => <div>Sales list</div>
    },
    {
        path: '/products',
        label: 'Products',
        exact: true,
        component: ()=> <div>Products list</div>
    }
];

export default routes

