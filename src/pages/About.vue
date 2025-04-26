<template>
    <div class="about-page-container">
      <!-- Navbar -->
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
  
      <!-- Main Content -->
      <main class="about-main">
        <!-- About Header -->
        <div class="about-header">
          <h1>📖 About Us</h1>
          <p class="description">
            Welcome to Business Event Boards! We are a community-powered platform that brings together events,
            promotes local businesses, and shares funding opportunities to boost our local economy and help
            everyone grow together.
          </p>
        </div>
  
        <!-- Title Sticky -->
        <div class="about-title-container">
          <div class="about-title-sticky">
            <div class="pin-emoji">📌</div>
            <h2 class="about-title-text">Meet the Team</h2>
          </div>
        </div>
  
        <!-- Sticky Notes for Workers -->
        <div class="about-sticky-board">
          <!-- Bennett Bush -->
          <div class="worker-sticky yellow tilt-left">
            <strong>Bennett Bush</strong><br />
            Computer Science Major<br />
            Junior
          </div>
  
          <!-- Larchelle Tuifao -->
          <div class="worker-sticky pink tilt-right">
            <strong>Larchelle Tuifao</strong><br />
            Computer Science Major<br />
            Senior
          </div>
  
          <!-- Karl Nick Matias -->
          <div class="worker-sticky blue tilt-left">
            <strong>Karl Nick Matias</strong><br />
            Computer Science Major<br />
            Junior
          </div>
        </div>
      </main>
  
      <!-- Footer -->
      <footer class="footer">
        <p>&copy; 2025 Team Procrastinators. All rights reserved.</p>
      </footer>
    </div>
  </template>
  
  <script setup>
  // No script needed for the About page
  </script>
  
  <style scoped>
  .about-page-container {
    background-color: #f5f0e1;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    font-family: 'Comic Sans MS', cursive, sans-serif;
  }
  
  /* Navbar with light pink colors */
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #ffb6c1; /* light pink */
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
    background-color: #ffc9d6; /* slightly lighter pink */
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    font-weight: bold;
    transition: transform 0.2s, background-color 0.3s;
  }
  
  .nav-link:hover {
    background-color: #ff99af; /* darker pink on hover */
    transform: scale(1.05);
  }
  
  /* Main Content */
  .about-main {
    flex: 1;
    padding: 2rem;
    text-align: center;
  }
  
  .about-header {
    font-size: 2rem;
    color: #4b3b2b;
    margin-bottom: 1rem;
  }
  
  .description {
    font-size: 1.1rem;
    color: #6a1b4d;
    max-width: 700px;
    margin: 0 auto 3rem;
    line-height: 1.6;
  }
  
  /* Title Sticky */
  .about-title-container {
    display: flex;
    justify-content: center;
    margin-bottom: 3rem;
  }
  
  .about-title-sticky {
    position: relative;
    background: #fff89a;
    padding: 2rem 4rem;
    border: 2px solid #f0e68c;
    border-radius: 12px;
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.15);
    width: fit-content;
  }
  
  .pin-emoji {
    position: absolute;
    top: -24px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 2rem;
  }
  
  .about-title-text {
    font-size: 2rem;
    color: #4b3b2b;
    margin: 0;
    font-weight: bold;
  }
  
  /* Sticky Board */
  .about-sticky-board {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    justify-content: center;
    align-items: center;
    margin-bottom: 3rem;
  }
  
  .worker-sticky {
    width: 220px;
    height: 220px;
    padding: 1rem;
    border-radius: 12px;
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.15);
    text-align: center;
    font-weight: bold;
    color: #4b3b2b;
    font-size: 1.2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    transition: transform 0.3s;
  }
  
  .worker-sticky:hover {
    transform: scale(1.05);
  }
  
  .tilt-left {
    transform: rotate(-3deg);
  }
  
  .tilt-right {
    transform: rotate(3deg);
  }
  
  .yellow {
    background-color: #fff89a;
    border: 2px solid #f0e68c;
  }
  
  .pink {
    background-color: #ffd1dc;
    border: 2px solid #ffb6c1;
  }
  
  .blue {
    background-color: #add8e6;
    border: 2px solid #87ceeb;
  }
  
  /* Footer with light pink */
  .footer {
    background-color: #ffb6c1;
    color: white;
    padding: 1rem;
    text-align: center;
  }
  </style>
  