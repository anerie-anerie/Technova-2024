import React from "react";
import "./NavBar.css";
import { Link } from "react-router-dom";

const brandName: string = "Iron Will";

const NavBar: React.FC = () => {
  return (
    <nav className="navbar navbar-expand-lg bg-primary navbar-dark">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">
          {brandName}
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link active" to="/" aria-current="page">
                Home
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/what-is-anemia">
                What Is Anemia?
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/iron-deficiency-anemia">
                Iron-Deficiency Anemia
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/check">
                Check
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/chatbot">
                Chatbot
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/form">
                Get Help Form
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
