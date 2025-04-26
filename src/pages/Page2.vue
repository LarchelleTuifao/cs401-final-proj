<template>
  <div class="page2-container">
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
    <main class="container">
      <h1>📇 Local Businesses Directory</h1>

      <!-- Post Your Business Button -->
      <div class="center-post">
        <div class="post-business-button" @click="showForm = !showForm">
          🏢 Post Your Business!
        </div>
      </div>

      <!-- Form to add business -->
      <div v-if="showForm" class="form-flyer">
        <form @submit.prevent="addBusiness">
          <input v-model="newBusiness.name" placeholder="Business Name" required />
          <input v-model="newBusiness.type" placeholder="Type (e.g. Café, Bookstore)" required />
          <input v-model="newBusiness.location" placeholder="Location" required />
          <input v-model="newBusiness.contact" placeholder="Contact Info" required />
          <button type="submit">Add Business</button>
        </form>
      </div>

      <!-- Business flyers -->
      <ul>
        <li 
          v-for="(business, index) in filteredBusinesses" 
          :key="index"
          class="business-flyer"
          @click="deleteBusiness(index)"
        >
          <div class="pin">📌</div>
          <strong>{{ business.name }}</strong><br />
          🏷️ {{ business.type }}<br />
          📍 {{ business.location }}<br />
          📞 {{ business.contact }}
        </li>
      </ul>

      <!-- Trash Can -->
      <div class="shredder" @click="toggleTrash">
        🗑️ ({{ deletedBusinesses.length }})
      </div>

      <!-- Trash Modal -->
      <div v-if="showTrash" class="trash-modal">
        <h2>Shredded Businesses</h2>
        <ul>
          <li v-for="(biz, idx) in deletedBusinesses" :key="idx" class="deleted-sheet">
            <strong>{{ biz.name }}</strong><br />
            Type: {{ biz.type }}<br />
            Location: {{ biz.location }}<br />
            Contact: {{ biz.contact }}
            <div class="restore-button" @click="restoreBusiness(idx)">Restore</div>
          </li>
        </ul>
        <button @click="toggleTrash">Close</button>
      </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
      <p>&copy; 2025 Team Procrastinators. All rights reserved.</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const newBusiness = ref({ name: '', type: '', location: '', contact: '' })
const businesses = ref([])
const deletedBusinesses = ref([])
const showForm = ref(false)
const showTrash = ref(false)

// Computed: businesses that are not deleted
const filteredBusinesses = computed(() => {
  const deletedSet = new Set(deletedBusinesses.value.map(b => b.name + b.location))
  return businesses.value.filter(biz => !deletedSet.has(biz.name + biz.location))
})

// Load businesses and deleted ones from localStorage
const loadLocalData = () => {
  businesses.value = JSON.parse(localStorage.getItem('businesses')) || []
  deletedBusinesses.value = JSON.parse(localStorage.getItem('deletedBusinesses')) || []
}

// Save to localStorage
const saveLocalData = () => {
  localStorage.setItem('businesses', JSON.stringify(businesses.value))
  localStorage.setItem('deletedBusinesses', JSON.stringify(deletedBusinesses.value))
}

// Add a new business
const addBusiness = () => {
  const newEntry = { ...newBusiness.value }
  businesses.value.push(newEntry)
  saveLocalData()
  newBusiness.value = { name: '', type: '', location: '', contact: '' }
  showForm.value = false
}

// Delete (shred) a business
const deleteBusiness = (index) => {
  const removed = filteredBusinesses.value[index]
  if (removed) {
    deletedBusinesses.value.push(removed)
    saveLocalData()
  }
}

// Restore business from trash
const restoreBusiness = (idx) => {
  const restored = deletedBusinesses.value.splice(idx, 1)[0]
  businesses.value.push(restored)
  saveLocalData()
}

// Toggle trash modal
const toggleTrash = () => {
  showTrash.value = !showTrash.value
}

onMounted(loadLocalData)
</script>

<style scoped>
/* Container & Navbar */
.page2-container {
  background: #fff3e0;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: 'Quicksand', sans-serif;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f57c00;
  padding: 0.5rem 2rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.title-container {
  display: flex;
  align-items: center;
}

.site-title {
  color: white;
  font-size: 1.8rem;
  font-weight: bold;
}

.nav-links {
  display: flex;
  gap: 1rem;
}

.nav-link {
  background-color: #ffb74d;
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-weight: bold;
  transition: transform 0.2s, background-color 0.3s;
}

.nav-link:hover {
  background-color: #fb8c00;
  transform: scale(1.05);
}

/* Main */
.container {
  flex: 1;
  background-color: #fff3e0;
  padding: 2rem;
}

h1 {
  text-align: center;
  color: #e65100;
  margin-bottom: 2rem;
  font-size: 2rem;
}

/* Center Post Button */
.center-post {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}

.post-business-button {
  background: #dcedc8;
  border: 2px solid #c5e1a5;
  padding: 1rem 2rem;
  border-radius: 12px;
  font-size: 1.5rem;
  font-weight: bold;
  color: #33691e;
  cursor: pointer;
  box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
  transition: background 0.3s;
}

.post-business-button:hover {
  background: #c5e1a5;
}

/* Form */
.form-flyer {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  max-width: 400px;
  margin: 0 auto 2rem;
  padding: 1rem;
}

form {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

input, button {
  padding: 0.75rem;
  font-size: 1rem;
  border-radius: 8px;
  border: 1px solid #ffe0b2;
}

button {
  background-color: #f57c00;
  color: white;
  border: none;
  cursor: pointer;
  transition: background 0.3s;
}

button:hover {
  background-color: #fb8c00;
}

/* Flyers */
ul {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
  padding: 0;
  list-style: none;
}

.business-flyer {
  background-color: #ffcc80;
  box-shadow: 4px 4px 12px rgba(0,0,0,0.1);
  padding: 1rem;
  width: 220px;
  border-radius: 12px;
  text-align: center;
  position: relative;
  font-size: 0.95rem;
  transition: transform 0.2s;
  cursor: pointer;
}

.business-flyer:hover {
  transform: scale(1.03) rotate(1deg);
}

.pin {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 1.5rem;
}

/* Shredder */
.shredder {
  position: fixed;
  bottom: 20px;
  right: 20px;
  font-size: 2.5rem;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.shredder:hover {
  animation: wiggle 0.5s infinite;
}

@keyframes wiggle {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(3deg); }
  50% { transform: rotate(-3deg); }
  75% { transform: rotate(3deg); }
}

/* Trash Modal */
.trash-modal {
  position: fixed;
  bottom: 80px;
  right: 20px;
  width: 300px;
  max-height: 400px;
  background: white;
  border: 2px solid #558b2f;
  overflow-y: auto;
  padding: 1rem;
  border-radius: 12px;
  box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
  z-index: 1000;
}

.deleted-sheet {
  background-color: #f0f8f0;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  text-align: left;
}

.restore-button {
  margin-top: 0.5rem;
  background: #558b2f;
  color: white;
  padding: 0.4rem 0.6rem;
  border-radius: 6px;
  font-size: 0.85rem;
  text-align: center;
  cursor: pointer;
  transition: background 0.3s;
}

.restore-button:hover {
  background: #33691e;
}

/* Footer */
.footer {
  background-color: #f57c00;
  color: white;
  padding: 1rem;
  text-align: center;
}
</style>
