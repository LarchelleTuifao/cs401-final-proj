<template>
  <div>
    <h1>Community Events Bulletin</h1>
    <form @submit.prevent="addEvent">
      <input v-model="newEvent.name" placeholder="Event Name" required />
      <input v-model="newEvent.time" type="datetime-local" required />
      <input v-model="newEvent.where" placeholder="Location" required />
      <input v-model="newEvent.why" placeholder="Why (Purpose)" required />
      <button type="submit">Add Event</button>
    </form>

    <ul>
      <li v-for="event in events" :key="event.id">
        <strong>{{ event.name }}</strong><br />
        When: {{ event.time }}<br />
        Where: {{ event.where }}<br />
        Why: {{ event.why }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const newEvent = ref({ name: '', time: '', where: '', why: '' })
const events = ref([])

const loadEvents = async () => {
  const res = await fetch('http://localhost:5001/api/events')
  events.value = await res.json()
}


const addEvent = async () => {
  const res = await fetch('http://localhost:5001/api/events', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(newEvent.value),
  });

  if (res.ok) {
    await loadEvents();
    newEvent.value = { name: '', time: '', where: '', why: '' };
  } else {
    console.error('Failed to submit event:', res.status);
  }
};


onMounted(loadEvents)
</script>

<style scoped>
body {
  background-color: #e0f7fa;
  font-family: Arial, sans-serif;
  padding: 2rem;
  margin: 0;
}

h1 {
  text-align: center;
  color: #007c91;
}

form {
  display: flex;
  flex-direction: column;
  max-width: 400px;
  margin: 0 auto 2rem;
  gap: 0.5rem;
}

input,
button {
  padding: 0.5rem;
  font-size: 1rem;
}

button {
  background-color: #007c91;
  color: white;
  border: none;
  cursor: pointer;
  transition: background 0.3s;
}

button:hover {
  background-color: #005f6b;
}

ul {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
  list-style: none;
  padding: 0;
}

li {
  background-color: #fff59d;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  padding: 1rem;
  width: 220px;
  border-radius: 8px;
  transform: rotate(-2deg);
  font-size: 0.95rem;
}

li:nth-child(odd) {
  transform: rotate(2deg);
}
</style>

