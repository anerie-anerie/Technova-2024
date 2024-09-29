import React from "react";
import "./IronDeficiencyAnemia.css"; // Import the CSS file
import anemiaImage from "./IronDeficiencyAnemia.jpg";

const IronDeficiencyAnemia: React.FC = () => {
  return (
    <div className="anemia-container">
      <h1>Iron Deficiency Anemia</h1>
      <div className="image-container">
        <img src={anemiaImage} alt="Anemia" />
      </div>
      <div className="section">
        <p>
          It's important to identify and treat anemia early, as it can lead to
          serious health problems if left untreated. The most common case is
          iron-deficiency anemia. Iron-deficiency anemia is caused by a lack of
          iron in the body, which is necessary for the production of hemoglobin,
          the protein in red blood cells that carries oxygen. This type of
          anemia can be treated with iron supplements and dietary changes to
          increase iron intake.
        </p>
      </div>
    </div>
  );
};

export default IronDeficiencyAnemia;
