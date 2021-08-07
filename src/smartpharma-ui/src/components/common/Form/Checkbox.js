import React from 'react'

const Checkbox = (props) => {
    return (
        <div className="form-check">
            <input
                className="form-check-input"
                type="checkbox"
                checked={props.checked ? true : false}
                disabled={props.disabled ? true : false}
                onChange={props.onClick}
                id = "checkbox"
            />
            {props.label && (
                <label className="form-check-label" for="checkbox">
                    {props.label}
                </label>
            )}
        </div>
    )
}

export default Checkbox
