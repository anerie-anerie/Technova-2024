import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import NavBar from "./components/NavBar";
import Home from "./components/pages/Home";
import WhatIsAnemia from "./components/pages/WhatIsAnemia";
import IronDeficiencyAnemia from "./components/pages/IronDeficiencyAnemia";
import Check from "./components/pages/Check";

const App: React.FC = () => {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/what-is-anemia" element={<WhatIsAnemia />} />
        <Route
          path="/iron-deficiency-anemia"
          element={<IronDeficiencyAnemia />}
        />
        <Route path="/check" element={<Check />} />
      </Routes>
    </Router>
  );
};

export default App;
