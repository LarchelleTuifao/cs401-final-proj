<template>
  <div class="page-container">
    <!-- Top Nav Bar -->
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

    <!-- Centered Post Button -->
    <div class="center-post">
      <div class="post-event-button" @click="showForm = !showForm">
        📝 Post A Community Event!
      </div>
    </div>

    <!-- Form sticky -->
    <div v-if="showForm" class="form-sticky">
      <form @submit.prevent="addEvent">
        <input v-model="newEvent.name" placeholder="Event Name" required />
        <input v-model="newEvent.time" type="datetime-local" required />
        <input v-model="newEvent.where" placeholder="Location" required />
        <input v-model="newEvent.why" placeholder="Why (Purpose)" required />
        <button type="submit">Add Event</button>
      </form>
    </div>

    <!-- Events list -->
    <ul>
      <li
        v-for="(event, index) in filteredEvents"
        :key="index"
        @click="deleteEvent(index)"
        :class="['sticky-note', event.colorClass]"
      >
        <div class="pin">📌</div>
        <strong>{{ event.name }}</strong><br />
        🕒 {{ formatDate(event.time) }}<br />
        📍 {{ event.where }}<br />
        💬 {{ event.why }}
      </li>
    </ul>

    <!-- Trash bin and modal -->
    <div class="trash-bin" @click="toggleTrash">
      🗑️ ({{ deletedEvents.length }})
    </div>

    <div v-if="showTrash" class="trash-modal">
      <h2>Deleted Events</h2>
      <ul>
        <li v-for="(deleted, idx) in deletedEvents" :key="idx" class="deleted-note">
          <strong>{{ deleted.name }}</strong><br />
          When: {{ formatDate(deleted.time) }}<br />
          Where: {{ deleted.where }}<br />
          Why: {{ deleted.why }}
          <div class="restore-button" @click="restoreEvent(idx)">Restore</div>
        </li>
      </ul>
      <button @click="toggleTrash">Close</button>
    </div>

    <!-- Footer -->
    <footer class="footer">
      <p>&copy; 2025 Team Procrastinators. All rights reserved.</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const newEvent = ref({ name: '', time: '', where: '', why: '' })
const events = ref([])
const deletedEvents = ref([])
const showForm = ref(false)
const showTrash = ref(false)

const colors = ['yellow-note', 'pink-note', 'blue-note', 'green-note', 'purple-note']

const filteredEvents = computed(() => {
  const deletedSet = new Set(deletedEvents.value.map(e => e.time + e.name))
  return events.value.filter(event => !deletedSet.has(event.time + event.name))
})

const loadLocalData = () => {
  events.value = JSON.parse(localStorage.getItem('events')) || []
  deletedEvents.value = JSON.parse(localStorage.getItem('deletedEvents')) || []
}

const saveLocalData = () => {
  localStorage.setItem('events', JSON.stringify(events.value))
  localStorage.setItem('deletedEvents', JSON.stringify(deletedEvents.value))
}

const addEvent = () => {
  const newEntry = { ...newEvent.value, colorClass: randomColor() }
  events.value.push(newEntry)
  saveLocalData()
  newEvent.value = { name: '', time: '', where: '', why: '' }
  showForm.value = false
}

const deleteEvent = (index) => {
  const removed = filteredEvents.value[index]
  if (removed) {
    deletedEvents.value.push(removed)
    events.value = events.value.filter(e => !(e.name === removed.name && e.time === removed.time))
    saveLocalData()
  }
}

const restoreEvent = (idx) => {
  const restored = deletedEvents.value.splice(idx, 1)[0]
  events.value.push(restored)
  saveLocalData()
}

const toggleTrash = () => {
  showTrash.value = !showTrash.value
}

const randomColor = () => {
  return colors[Math.floor(Math.random() * colors.length)]
}

const formatDate = (datetime) => {
  const options = { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }
  return new Date(datetime).toLocaleString(undefined, options)
}

onMounted(loadLocalData)
</script>

<style scoped>
/* Layout & Styling: Combines both styles */
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&display=swap');

.page-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #6d4f34;
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
  background-color: #8d6e63;
  color: #ffffff;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: bold;
  transition: transform 0.2s, background-color 0.3s;
}

.nav-link:hover {
  background-color: #7b5e50;
  transform: scale(1.05);
}

.center-post {
  display: flex;
  justify-content: center;
  margin: 2rem 0;
}

.post-event-button {
  background: #fff89a;
  border: 2px solid #f0e68c;
  padding: 1.5rem 3rem;
  border-radius: 12px;
  font-size: 1.8rem;
  font-weight: bold;
  color: #4b3b2b;
  box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
  cursor: pointer;
  transform: rotate(-2deg);
  transition: background 0.3s, transform 0.3s;
}

.post-event-button:hover {
  background: #fff56d;
  transform: rotate(0deg) scale(1.03);
}

.form-sticky {
  background: #fff89a;
  border: 2px solid #f0e68c;
  border-radius: 12px;
  box-shadow: 3px 3px 7px rgba(0,0,0,0.2);
  padding: 1rem;
  max-width: 400px;
  margin: 0 auto 2rem;
  transform: rotate(1deg);
}

form {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

input,
button {
  padding: 0.75rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
}

button {
  background-color: #6d4c41;
  color: white;
  border: none;
  cursor: pointer;
  transition: background 0.3s;
}

button:hover {
  background-color: #4e342e;
}

ul {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
  list-style: none;
  padding: 0;
}

.sticky-note {
  background-color: #fff9c4;
  box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
  padding: 1rem;
  width: 220px;
  border-radius: 12px;
  transform: rotate(-2deg);
  cursor: pointer;
  position: relative;
  font-size: 0.95rem;
  transition: transform 0.2s;
}

.sticky-note:hover {
  transform: rotate(0deg) scale(1.03);
}

.pin {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 1.5rem;
}

.yellow-note { background-color: #fff89a; border: 2px solid #f0e68c; }
.pink-note   { background-color: #ffd1dc; border: 2px solid #ffb6c1; }
.blue-note   { background-color: #add8e6; border: 2px solid #87ceeb; }
.green-note  { background-color: #c1f0c1; border: 2px solid #a8d5a8; }
.purple-note { background-color: #e1d5f5; border: 2px solid #b9a3e3; }

.trash-bin {
  position: fixed;
  bottom: 20px;
  right: 20px;
  font-size: 2.5rem;
  cursor: pointer;
  transition: transform 0.2s;
}

.trash-bin:hover {
  animation: wiggle 0.5s ease infinite;
}

@keyframes wiggle {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(5deg); }
  50% { transform: rotate(-5deg); }
  75% { transform: rotate(5deg); }
}

.trash-modal {
  position: fixed;
  bottom: 80px;
  right: 20px;
  width: 300px;
  max-height: 400px;
  background: white;
  border: 2px solid #4b3b2b;
  box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
  overflow-y: auto;
  padding: 1rem;
  border-radius: 12px;
  z-index: 1000;
}

.deleted-note {
  background-color: #fff8e1;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  text-align: left;
  position: relative;
}

.restore-button {
  margin-top: 0.5rem;
  background: #4b3b2b;
  color: white;
  padding: 0.4rem 0.6rem;
  border-radius: 6px;
  text-align: center;
  font-size: 0.85rem;
  cursor: pointer;
  transition: background 0.3s;
}

.restore-button:hover {
  background: #2e2216;
}

.footer {
  margin-top: auto;
  background-color: #6d4f34;
  color: white;
  padding: 1rem;
  text-align: center;
}
</style>
