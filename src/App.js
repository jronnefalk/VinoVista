import React, { useState } from "react";
import "./App.css";

function App() {
  // State variables to store user input and recommendations
  const [country, setCountry] = useState("");
  const [taste, setTaste] = useState("");
  const [recommendations, setRecommendations] = useState([]);

  // Event handler for country input change
  const handleCountryChange = (event) => {
    setCountry(event.target.value);
  };

  // Event handler for taste input change
  const handleTasteChange = (event) => {
    setTaste(event.target.value);
  };

  // Event handler for form submission
  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      // Update the fetch URL to match the Flask route
      const response = await fetch(
        "https://wine-recommendation.herokuapp.com/api/recommend",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ country, taste }),
        }
      );

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setRecommendations(data);
    } catch (error) {
      console.error("A problem occurred with the fetch operation:", error);
    }
  };

  // Function to truncate long wine descriptions
  const truncateDescription = (description) => {
    const words = description.split(" ");
    if (words.length > 60) {
      return words.slice(0, 60).join(" ") + "...";
    } else {
      return description;
    }
  };

  return (
    <div className="container">
      <h1 className="title">VinoVista</h1>
      <div className="form-container">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>
              Country:
              <input
                type="text"
                value={country}
                onChange={handleCountryChange}
                className="input-field"
              />
            </label>
          </div>
          <div className="form-group">
            <label>
              Taste preferences:
              <input
                type="text"
                value={taste}
                onChange={handleTasteChange}
                className="input-field"
              />
            </label>
          </div>
          <button type="submit" className="submit-button">
            FIND WINES
          </button>
        </form>
      </div>
      <div className="recommendations">
        {recommendations.map((wine, index) => (
          <div key={index} className="recommendation-item">
            <h3>{wine.title}</h3>
            <p className="province">Province: {wine.province}</p>
            <p>{truncateDescription(wine.description)}</p>
            <p className="price">${wine.price}</p>
            <p className="points">Rating: {wine.points} points</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
