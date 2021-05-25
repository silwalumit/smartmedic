import * as React from 'react';


export const Input = props => {
    const validate = (e)=>{
        const pattern = props.pattern;
        if (pattern){
            const regex = RegExp(pattern)
            if (parseInt(e.which) !== 8 && !regex.test(e.key)){
                 e.preventDefault();
            }
        }
        return true;
    };

    const inputField = () => (
        <input
            type = {props.type ? props.type : 'text'}
            placeholder = {props.placeholder}
            className={`form-control ${props.classess}`}
            autoComplete="off"
            id={props.placeholder.toLowerCase()}
            onKeyPress = {validate}
            onChange={e => {
                e.preventDefault();
                e.stopPropagation();
                props.valueChanged(e.target.value)
            }}
        />
    );

    return (
        props.label ? (
            <div className="form-floating">
                {inputField()}
                <label htmlFor = {props.placeholder.toLowerCase()}>{props.label}</label>
            </div>
        ) : inputField()

    );
};