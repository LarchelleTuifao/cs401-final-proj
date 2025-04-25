
<template>
  <div>
    <h1>Local Businesses Directory</h1>
    <form @submit.prevent="addBusiness">
      <input v-model="newBusiness.name" placeholder="Business Name" required />
      <input v-model="newBusiness.type" placeholder="Type (e.g. Café, Bookstore)" required />
      <input v-model="newBusiness.location" placeholder="Location" required />
      <input v-model="newBusiness.contact" placeholder="Contact Info" required />
      <button type="submit">Add Business</button>
    </form>

    <ul>
      <li v-for="business in businesses" :key="business.id">
        <strong>{{ business.name }}</strong><br />
        Type: {{ business.type }}<br />
        Location: {{ business.location }}<br />
        Contact: {{ business.contact }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const newBusiness = ref({ name: '', type: '', location: '', contact: '' })
const businesses = ref([])

const loadBusinesses = async () => {
  const res = await fetch('http://localhost:5001/api/businesses')
  businesses.value = await res.json()
}

const addBusiness = async () => {
  const res = await fetch('http://localhost:5001/api/businesses', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(newBusiness.value),
  })

  if (res.ok) {
    await loadBusinesses()
    newBusiness.value = { name: '', type: '', location: '', contact: '' }
  } else {
    console.error('Failed to submit business:', res.status)
  }
}

onMounted(loadBusinesses)
</script>

<style scoped>
body {
  background-color: #f1f8e9;
  font-family: Arial, sans-serif;
  padding: 2rem;
  margin: 0;
}

h1 {
  text-align: center;
  color: #558b2f;
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
  background-color: #558b2f;
  color: white;
  border: none;
  cursor: pointer;
  transition: background 0.3s;
}

button:hover {
  background-color: #33691e;
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
  background-color: #dcedc8;
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

