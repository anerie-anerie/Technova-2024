import React from "react";
import "./Home.css"; // Import the CSS file
import anemiaImage1 from "./homepage.jpg"; // Import your images

const Home: React.FC = () => {
  return (
    <div>
      <div className="home-container">
        <h1>Welcome to Iron Will</h1>
        <p>Your resource for understanding and managing anemia.</p>
      </div>
      <div className="image-container">
        <img
          src={anemiaImage1}
          alt="Anemia information"
          style={{ width: "300px", height: "auto" }} // Explicit inline style
        />
      </div>
    </div>
  );
};

export default Home;
