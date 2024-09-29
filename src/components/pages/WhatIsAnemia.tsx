import React from "react";
import "./WhatIsAnemia.css"; // Import the CSS file
import anemiaImage from "./anemia-image.jpg"; // Import an image (local or URL)

const WhatIsAnemia: React.FC = () => {
  return (
    <div className="anemia-container">
      <h1>What Is Anemia?</h1>
      <div className="image-container">
        <img src={anemiaImage} alt="Anemia" />
      </div>
      <div className="section">
        <p>
          Anemia is a condition where your body doesn't have enough healthy red
          blood cells to carry oxygen to your tissues. When you have anemia,
          your body doesn't get enough oxygen, which can make you feel tired,
          weak, and short of breath. One-fourth of the global population is
          estimated to be anemic, with cases increasing rapidly for women,
          expectant mothers, young girls, and children younger than age 5 [1].
          Anemia is the third-leading cause of years with lived disability in
          the world. Globally, in 2021, 31.2% of women had anemia compared with
          17.5% of men. The gender difference was more pronounced during the
          reproductive years, ages 15–49. In this age group, anemia prevalence
          in women was 33.7% versus 11.3% in men [1].
        </p>
      </div>
      <div className="section">
        <p>
          [1]
          https://www.healthdata.org/news-events/newsroom/news-releases/lancet-
          new-study-reveals-global-anemia-cases-remain-persistently#:~:text=Topics&text
          =One%2Dfourth%20of%20the%20global,million%20cases%20over%20three%20decades.
        </p>
      </div>
    </div>
  );
};

export default WhatIsAnemia;
