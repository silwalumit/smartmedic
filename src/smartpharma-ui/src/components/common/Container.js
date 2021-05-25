import * as React from 'react';


export const Container = ({classess, children, ...rest}) => (
    <div className = {classess} {...rest}>
        {children} 
    </div>
);