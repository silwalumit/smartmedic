import * as React from 'react';


export const Container = ({classes, children, ...rest}) => (
    <div className = {classes} {...rest}>
        {children} 
    </div>
);