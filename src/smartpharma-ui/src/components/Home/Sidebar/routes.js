import { lazy } from "react";
const Dashboard = lazy(() => import('../../Dashboard/Dashboard'));
const Product = lazy(() => import('../../Product/Product'));


const routes = [
    {
        path: '/',
        label: 'Dashboard',
        exact: true,
        component: () => <Dashboard />
    },
    {
        path: '/sales',
        label: 'Sales',
        exact: true,
        component: () => <div>Sales list</div>
    },
    {
        path: '/products',
        label: 'Products',
        exact: true,
        component: () => <Product />
    }
];

export default routes

