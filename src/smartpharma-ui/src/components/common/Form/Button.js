import React from 'react';
import '../../../sass/button.scss';

const Button = props => (
    <button
        {...props}
        className={`btn ${props.disabled ? 'btn-default' : props.variant ? props.variant : 'btn-primary'} ${props.classes}`}
        onClick={()=> props.onClick && props.onClick()}
    >{props.label}</button>
);

export default Button