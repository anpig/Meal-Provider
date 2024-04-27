import React from "react";
import "./style.css";

export const Login = () => {
    return (
        <div className="login">
            <div className="overlap-wrapper">
                <div className="overlap">
                    <div className="overlap-group">
                        <div className="group">
                            <div className="div">
                                <div className="frame">
                                    <div className="frame-2">
                                        <div className="text-wrapper">Staff ID</div>
                                        <div className="div-wrapper">
                                            <div className="text-wrapper-2">ex. 000001</div>
                                        </div>
                                    </div>
                                    <div className="frame-3">
                                        <div className="frame-2">
                                            <div className="text-wrapper">Password</div>
                                            <div className="div-wrapper">
                                                <div className="text-wrapper-3">ex. password123</div>
                                            </div>
                                        </div>
                                        <div className="frame-4">
                                            <div className="text-wrapper-4">Login</div>
                                        </div>
                                    </div>
                                </div>
                                <div className="text-wrapper-5">Forget Password</div>
                            </div>
                        </div>
                    </div>
                    <div className="frame-5">
                        <img
                            className="taiwan-semiconductor"
                            alt="Taiwan semiconductor"
                            src="taiwan-semiconductor-manufacturing-company-logo-svg.svg"
                        />
                        <p className="welcome-to-TSMC-meal">
                            Welcome to TSMC <br />
                            Meal Provider
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};
