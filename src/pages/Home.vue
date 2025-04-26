<template>
  <div class="home-container">
    <header class="navbar">
      <div class="title-container">
        <h1 class="site-title">Business Event Boards</h1>
      </div>
      <nav class="nav-links">
        <router-link to="/" class="nav-link">🏠 Home</router-link>
        <router-link to="/about" class="nav-link">📖 About</router-link>
        <router-link to="/page1" class="nav-link">📋 Community Events Bulletin</router-link>
        <router-link to="/page2" class="nav-link">🏪 Local Business Directory</router-link>
        <router-link to="/page3" class="nav-link">💰 Funding Opportunities</router-link>
      </nav>
    </header>

    <main class="main-content">
      <h2 class="welcome-text">Welcome to the hub for community-driven connections and resources!</h2>

      <section class="hero-links">
        <div class="card">
          <img src="https://img.icons8.com/color/96/calendar--v1.png" alt="Community Events" class="card-image" />
          <h3 class="card-title">Community Events Bulletin</h3>
          <router-link to="/page1" class="card-button">Explore Events</router-link>
        </div>

        <div class="card">
          <img src="https://img.icons8.com/color/96/shop.png" alt="Local Business Directory" class="card-image" />
          <h3 class="card-title">Local Business Directory</h3>
          <router-link to="/page2" class="card-button">View Businesses</router-link>
        </div>

        <div class="card">
          <img src="https://img.icons8.com/color/96/money-bag.png" alt="Funding Opportunities" class="card-image" />
          <h3 class="card-title">Funding Opportunities</h3>
          <router-link to="/page3" class="card-button">Find Funding</router-link>
        </div>
      </section>
    </main>

    <footer class="footer">
      <p>&copy; 2025 Team Procrastinators. All rights reserved.</p>
    </footer>
  </div>
</template>

<script setup>
// No extra JS needed for home page
</script>

<style scoped>
.home-container {
  background: #e6f7ff; /* light blue background */
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: 'Quicksand', sans-serif;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #3399cc; /* vibrant ocean blue */
  padding: 0.5rem 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.title-container {
  display: flex;
  align-items: center;
}

.site-title {
  color: white;
  font-size: 1.8rem;
  font-weight: bold;
  margin-right: 20px;
}

.nav-links {
  display: flex;
  gap: 1rem;
}

.nav-link {
  background-color: #66c2ff; /* lighter blue button */
  color: #ffffff;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: bold;
  transition: transform 0.2s, background-color 0.3s;
}

.nav-link:hover {
  background-color: #4da6ff; /* darker on hover */
  transform: scale(1.05);
}

.main-content {
  padding: 2rem;
  flex: 1;
  text-align: center;
}

.welcome-text {
  font-size: 1.5rem;
  color: #005b96; /* navy blue */
  margin-bottom: 2rem;
}

.hero-links {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
}

.card {
  background-color: #ccf2ff; /* pastel blue */
  border-radius: 12px;
  padding: 1.5rem;
  width: 260px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: transform 0.2s;
}

.card:hover {
  transform: scale(1.05);
}

.card-image {
  width: 80px;
  height: 80px;
  margin-bottom: 1rem;
}

.card-title {
  font-size: 1.2rem;
  color: #0077b6;
  margin-bottom: 1rem;
}

.card-button {
  display: inline-block;
  background-color: #3399cc;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  text-decoration: none;
  transition: background-color 0.3s;
}

.card-button:hover {
  background-color: #267fa1;
}

.footer {
  background-color: #3399cc;
  color: white;
  padding: 1rem;
  text-align: center;
}
</style>
