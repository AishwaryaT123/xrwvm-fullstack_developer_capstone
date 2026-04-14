import React from "react";

function Header({ user, onLogout }) {
  return (
    <nav style={styles.nav}>
      <a href="/" style={styles.brand}>🚗 Cars Dealership</a>
      <div style={styles.links}>
        <a href="/" style={styles.link}>Home</a>
        <a href="/static/About.html" style={styles.link}>About</a>
        <a href="/static/Contact.html" style={styles.link}>Contact</a>
        {user ? (
          <>
            <span style={styles.username}>👤 {user}</span>
            <button onClick={onLogout} style={styles.btn}>Logout</button>
          </>
        ) : (
          <>
            <a href="/djangoapp/login" style={styles.btn}>Login</a>
            <a href="/djangoapp/register" style={{ ...styles.btn, background: "#e94560" }}>Register</a>
          </>
        )}
      </div>
    </nav>
  );
}

const styles = {
  nav: { background: "#1a1a2e", padding: "1rem 2rem", display: "flex", justifyContent: "space-between", alignItems: "center" },
  brand: { color: "#fff", fontWeight: "700", fontSize: "1.3rem", textDecoration: "none" },
  links: { display: "flex", alignItems: "center", gap: "1rem" },
  link: { color: "rgba(255,255,255,0.8)", textDecoration: "none", fontSize: "0.95rem" },
  username: { color: "#fff", fontSize: "0.9rem" },
  btn: { background: "transparent", border: "1px solid #fff", color: "#fff", padding: "0.4rem 1rem", borderRadius: "6px", cursor: "pointer", textDecoration: "none", fontSize: "0.9rem" },
};

export default Header;
