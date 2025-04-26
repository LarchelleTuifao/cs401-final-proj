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

    <main class="container">
      <h1>💰 Funding Opportunities</h1>

      <div class="center-post">
        <div class="post-opportunity-button" @click="showForm = !showForm">
          📄 Post a Funding Opportunity!
        </div>
      </div>

      <div v-if="showForm" class="form-sheet">
        <form @submit.prevent="addOpportunity">
          <input v-model="newOpportunity.name" placeholder="Opportunity Name" required />
          <input v-model="newOpportunity.deadline" type="date" required />
          <input v-model="newOpportunity.source" placeholder="Funding Source" required />
          <input v-model="newOpportunity.description" placeholder="Short Description" required />
          <button type="submit">Add Opportunity</button>
        </form>
      </div>

      <ul>
        <li
          v-for="(opportunity, index) in filteredOpportunities"
          :key="index"
          @click="deleteSticky(index)"
          class="opportunity-sheet"
        >
          <div class="paperclip"></div>
          <div class="sheet-content">
            <strong>{{ opportunity.name }}</strong><br />
            ⏳ Deadline: {{ opportunity.deadline }}<br />
            🏛️ Source: {{ opportunity.source }}<br />
            📄 {{ opportunity.description }}
          </div>
        </li>
      </ul>

      <!-- Trash bin & modal -->
      <div class="trash-bin" @click="toggleTrash">
        🗑️ ({{ deletedOpportunities.length }})
      </div>

      <div v-if="showTrash" class="trash-modal">
        <h2>Deleted Opportunities</h2>
        <ul>
          <li v-for="(item, idx) in deletedOpportunities" :key="idx" class="deleted-sheet">
            <strong>{{ item.name }}</strong><br />
            Deadline: {{ item.deadline }}<br />
            Source: {{ item.source }}<br />
            Description: {{ item.description }}
            <div class="restore-button" @click="restoreOpportunity(idx)">Restore</div>
          </li>
        </ul>
        <button @click="toggleTrash">Close</button>
      </div>
    </main>

    <footer class="footer">
      <p>&copy; 2025 Team Procrastinators. All rights reserved.</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const newOpportunity = ref({ name: '', deadline: '', source: '', description: '' })
const opportunities = ref([])
const deletedOpportunities = ref([])
const showForm = ref(false)
const showTrash = ref(false)

const filteredOpportunities = computed(() => {
  const deletedSet = new Set(deletedOpportunities.value.map(op => op.name + op.source))
  return opportunities.value.filter(op => !deletedSet.has(op.name + op.source))
})

const loadLocalData = () => {
  opportunities.value = JSON.parse(localStorage.getItem('opportunities')) || []
  deletedOpportunities.value = JSON.parse(localStorage.getItem('deletedOpportunities')) || []
}

const saveLocalData = () => {
  localStorage.setItem('opportunities', JSON.stringify(opportunities.value))
  localStorage.setItem('deletedOpportunities', JSON.stringify(deletedOpportunities.value))
}

const addOpportunity = () => {
  const newEntry = { ...newOpportunity.value }
  opportunities.value.push(newEntry)
  saveLocalData()
  newOpportunity.value = { name: '', deadline: '', source: '', description: '' }
  showForm.value = false
}

const deleteSticky = (index) => {
  const removed = filteredOpportunities.value[index]
  if (removed) {
    deletedOpportunities.value.push(removed)
    saveLocalData()
  }
}

const restoreOpportunity = (idx) => {
  const restored = deletedOpportunities.value.splice(idx, 1)[0]
  opportunities.value.push(restored)
  saveLocalData()
}

const toggleTrash = () => {
  showTrash.value = !showTrash.value
}

onMounted(loadLocalData)
</script>

<style scoped>
/* Combined styles from both components */
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&display=swap');

.home-container {
  background: #e8f5e9;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: 'Quicksand', sans-serif;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #388e3c;
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
  margin-right: 20px;
}

.nav-links {
  display: flex;
  gap: 1rem;
}

.nav-link {
  background-color: #81c784;
  color: #ffffff;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: bold;
  transition: transform 0.2s, background-color 0.3s;
}

.nav-link:hover {
  background-color: #66bb6a;
  transform: scale(1.05);
}

.container {
  background-color: #e8f5e9;
  padding: 2rem;
  min-height: 100vh;
}

h1 {
  text-align: center;
  color: #388e3c;
  margin-bottom: 2rem;
  font-size: 2rem;
}

.center-post {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}

.post-opportunity-button {
  background: #ffe0b2;
  border: 2px solid #ffcc80;
  padding: 1.5rem 3rem;
  border-radius: 12px;
  font-size: 1.8rem;
  font-weight: bold;
  color: #e65100;
  box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
  cursor: pointer;
  transition: background 0.3s;
}

.post-opportunity-button:hover {
  background: #ffcc80;
}

.form-sheet {
  background: #ffffff;
  border: 2px solid #ffe0b2;
  border-radius: 8px;
  box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
  padding: 1rem;
  max-width: 400px;
  margin: 1rem auto 2rem;
}

input,
button {
  padding: 0.75rem;
  font-size: 1rem;
  border: 1px solid #a5d6a7;
  border-radius: 8px;
  width: 100%;
  box-sizing: border-box;
}

button {
  background-color: #43a047;
  color: white;
  border: none;
  cursor: pointer;
  transition: background 0.3s;
}

button:hover {
  background-color: #388e3c;
}

ul {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
  list-style: none;
  padding: 0;
}

.opportunity-sheet {
  position: relative;
  background-color: #ffffff;
  border: 2px solid #ffe0b2;
  box-shadow: 4px 4px 8px rgba(0,0,0,0.2);
  padding: 1.5rem;
  width: 260px;
  height: 240px;
  border-radius: 8px;
  text-align: center;
  transition: transform 0.2s, background 0.3s;
  cursor: pointer;
}

.opportunity-sheet:hover {
  transform: scale(1.03);
  background-color: #fff8e1;
}

.paperclip {
  position: absolute;
  top: 10px;
  left: 10px;
  width: 12px;
  height: 20px;
  border: 2px solid #555;
  border-top: none;
  border-left: none;
  transform: rotate(-20deg);
}

.trash-bin {
  position: fixed;
  bottom: 20px;
  right: 20px;
  font-size: 2.5rem;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.trash-bin:hover {
  animation: wiggle 0.5s ease infinite;
}

@keyframes wiggle {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(3deg); }
  50% { transform: rotate(-3deg); }
  75% { transform: rotate(3deg); }
}

.trash-modal {
  position: fixed;
  bottom: 80px;
  right: 20px;
  width: 300px;
  max-height: 400px;
  background: white;
  border: 2px solid #ef6c00;
  box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
  overflow-y: auto;
  padding: 1rem;
  border-radius: 12px;
  z-index: 1000;
}

.deleted-sheet {
  background-color: #fff8e1;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  text-align: left;
  position: relative;
}

.restore-button {
  margin-top: 0.5rem;
  background: #ef6c00;
  color: white;
  padding: 0.4rem 0.6rem;
  border-radius: 6px;
  text-align: center;
  font-size: 0.85rem;
  cursor: pointer;
  transition: background 0.3s;
}

.restore-button:hover {
  background: #e65100;
}

.footer {
  background-color: #388e3c;
  color: white;
  padding: 1rem;
  text-align: center;
}
</style>
