import React, { useState, useEffect } from "react";

function Dealers() {
  const [dealers, setDealers] = useState([]);
  const [state, setState] = useState("All");
  const [loading, setLoading] = useState(true);

  const states = ["All", "Kansas", "California", "Florida", "New York", "Texas"];

  useEffect(() => {
    fetchDealers();
  }, [state]);

  const fetchDealers = async () => {
    setLoading(true);
    try {
      const url = state === "All"
        ? "/djangoapp/get_dealers"
        : `/djangoapp/get_dealers/${state}`;
      const res = await fetch(url);
      const data = await res.json();
      setDealers(data.dealers || []);
    } catch (err) {
      console.error("Error fetching dealers:", err);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "1100px", margin: "0 auto" }}>
      <h2 style={{ fontWeight: "700", marginBottom: "1rem" }}>Find a Dealership</h2>

      {/* State filter */}
      <div style={{ marginBottom: "1.5rem", display: "flex", gap: "0.5rem", flexWrap: "wrap" }}>
        {states.map(s => (
          <button
            key={s}
            onClick={() => setState(s)}
            style={{
              padding: "0.4rem 1rem",
              borderRadius: "20px",
              border: "2px solid #e94560",
              background: state === s ? "#e94560" : "white",
              color: state === s ? "white" : "#e94560",
              cursor: "pointer",
              fontWeight: "600",
            }}
          >
            {s}
          </button>
        ))}
      </div>

      {/* Dealer grid */}
      {loading ? (
        <p>Loading dealerships...</p>
      ) : (
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))", gap: "1rem" }}>
          {dealers.map(dealer => (
            <div key={dealer.id} style={cardStyle}>
              <h5 style={{ fontWeight: "700", marginBottom: "0.3rem" }}>{dealer.full_name}</h5>
              <p style={{ color: "#888", marginBottom: "0.2rem" }}>📍 {dealer.city}, {dealer.st}</p>
              <p style={{ color: "#888", fontSize: "0.85rem", marginBottom: "1rem" }}>{dealer.address}</p>
              <a
                href={`/djangoapp/dealer/${dealer.id}/`}
                style={{ background: "#e94560", color: "white", padding: "0.4rem 1rem", borderRadius: "6px", textDecoration: "none", fontSize: "0.9rem", fontWeight: "600" }}
              >
                View Reviews
              </a>
            </div>
          ))}
          {dealers.length === 0 && <p style={{ color: "#888" }}>No dealerships found.</p>}
        </div>
      )}
    </div>
  );
}

const cardStyle = {
  background: "white",
  borderRadius: "12px",
  padding: "1.25rem",
  boxShadow: "0 4px 15px rgba(0,0,0,0.08)",
};

export default Dealers;
