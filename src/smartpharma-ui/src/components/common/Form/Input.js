import * as React from 'react';
import '../../../sass/input.scss'

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
            className={`form-control ${props.classes}`}
            autoComplete="off"
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
            <div className="floating-label">
                {inputField()}
                {!props.noFloat && <label>{props.label}</label>}
                <span className="focus-border"></span>
                {props.error && (
                    <div className="invalid-feedback">
                        { props.error}
                    </div>
                )}
            </div>
        ) : inputField()

    );
};