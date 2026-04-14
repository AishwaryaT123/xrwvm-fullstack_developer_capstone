import React, { useState } from "react";

function Register() {
  const [username, setUsername] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    const registerData = {
      userName: username,
      firstName: firstName,
      lastName: lastName,
      password: password,
      email: email,
    };

    try {
      const res = await fetch("/djangoapp/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(registerData),
      });
      const data = await res.json();
      if (data.status === "Authenticated") {
        setMessage("Registration successful! Redirecting...");
        setTimeout(() => (window.location.href = "/"), 1500);
      } else {
        setMessage(data.message || "Registration failed. Please try again.");
      }
    } catch (err) {
      setMessage("An error occurred. Please try again.");
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <div style={styles.header}>
          <h2 style={styles.title}>🚗 Create Account</h2>
          <p style={styles.subtitle}>Join Cars Dealership today</p>
        </div>

        <form onSubmit={handleRegister} style={styles.form}>
          {/* Username */}
          <div style={styles.field}>
            <label style={styles.label}>Username</label>
            <input
              type="text"
              style={styles.input}
              placeholder="Choose a username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>

          {/* First Name */}
          <div style={styles.field}>
            <label style={styles.label}>First Name</label>
            <input
              type="text"
              style={styles.input}
              placeholder="Enter your first name"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
              required
            />
          </div>

          {/* Last Name */}
          <div style={styles.field}>
            <label style={styles.label}>Last Name</label>
            <input
              type="text"
              style={styles.input}
              placeholder="Enter your last name"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
              required
            />
          </div>

          {/* Email */}
          <div style={styles.field}>
            <label style={styles.label}>Email</label>
            <input
              type="email"
              style={styles.input}
              placeholder="Enter your email address"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          {/* Password */}
          <div style={styles.field}>
            <label style={styles.label}>Password</label>
            <input
              type="password"
              style={styles.input}
              placeholder="Create a password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          {message && (
            <p style={styles.message}>{message}</p>
          )}

          <button type="submit" style={styles.button}>
            Register
          </button>

          <p style={styles.loginLink}>
            Already have an account?{" "}
            <a href="/djangoapp/login" style={styles.link}>Sign In</a>
          </p>
        </form>
      </div>
    </div>
  );
}

const styles = {
  container: {
    minHeight: "100vh",
    background: "linear-gradient(135deg, #1a1a2e, #16213e)",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    padding: "2rem",
  },
  card: {
    background: "#fff",
    borderRadius: "20px",
    padding: "2.5rem",
    width: "100%",
    maxWidth: "440px",
    boxShadow: "0 20px 60px rgba(0,0,0,0.3)",
  },
  header: { textAlign: "center", marginBottom: "2rem" },
  title: { color: "#1a1a2e", fontWeight: "700", fontSize: "1.8rem", margin: 0 },
  subtitle: { color: "#888", marginTop: "0.5rem" },
  form: { display: "flex", flexDirection: "column", gap: "1rem" },
  field: { display: "flex", flexDirection: "column", gap: "0.3rem" },
  label: { fontWeight: "600", color: "#333", fontSize: "0.9rem" },
  input: {
    padding: "0.75rem 1rem",
    border: "2px solid #e0e0e0",
    borderRadius: "10px",
    fontSize: "0.95rem",
    outline: "none",
    transition: "border-color 0.2s",
  },
  button: {
    background: "#e94560",
    color: "#fff",
    border: "none",
    padding: "0.9rem",
    borderRadius: "10px",
    fontSize: "1rem",
    fontWeight: "700",
    cursor: "pointer",
    marginTop: "0.5rem",
  },
  message: { color: "#e94560", textAlign: "center", fontSize: "0.9rem" },
  loginLink: { textAlign: "center", color: "#888", fontSize: "0.9rem" },
  link: { color: "#e94560", fontWeight: "600", textDecoration: "none" },
};

export default Register;
