import React from 'react'

const Checkbox = (props) => {
    return (
        <div class="form-check">
            <input
                class="form-check-input"
                type="checkbox"
                checked={props.checked ? true : false}
                disabled={props.disabled ? true : false}
                id = "checkbox"
            />
            {props.label && (
                <label class="form-check-label" for="checkbox">
                    {props.label}
                </label>
            )}
        </div>
    )
}

export default Checkbox
