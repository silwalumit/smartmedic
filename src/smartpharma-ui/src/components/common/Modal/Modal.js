import React from "react";

const Modal = (props) => (
    <div role="dialog" className="modal show fade" style={props.show ? { display: "block" } : {display:"none"}}>
        <div className="modal-dialog modal-lg" role="document">
            <div className="modal-content">
                <div className="modal-header">
                    <h5 className="modal-title">{props.title}</h5>
                    <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div className="modal-body">
                    hello there!
                </div>
            </div>
        </div>
    </div>
);

export default Modal