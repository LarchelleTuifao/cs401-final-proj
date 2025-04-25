
<template>
  <div>
    <h1>Funding Opportunities</h1>
    <form @submit.prevent="addOpportunity">
      <input v-model="newOpportunity.name" placeholder="Opportunity Name" required />
      <input v-model="newOpportunity.deadline" type="date" required />
      <input v-model="newOpportunity.source" placeholder="Funding Source" required />
      <input v-model="newOpportunity.description" placeholder="Short Description" required />
      <button type="submit">Add Opportunity</button>
    </form>

    <ul>
      <li v-for="opportunity in opportunities" :key="opportunity.id">
        <strong>{{ opportunity.name }}</strong><br />
        Deadline: {{ opportunity.deadline }}<br />
        Source: {{ opportunity.source }}<br />
        Description: {{ opportunity.description }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const newOpportunity = ref({ name: '', deadline: '', source: '', description: '' })
const opportunities = ref([])

const loadOpportunities = async () => {
  const res = await fetch('http://localhost:5001/api/opportunities')
  opportunities.value = await res.json()
}

const addOpportunity = async () => {
  const res = await fetch('http://localhost:5001/api/opportunities', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(newOpportunity.value),
  })

  if (res.ok) {
    await loadOpportunities()
    newOpportunity.value = { name: '', deadline: '', source: '', description: '' }
  } else {
    console.error('Failed to submit opportunity:', res.status)
  }
}

onMounted(loadOpportunities)
</script>

<style scoped>
body {
  background-color: #fff3e0;
  font-family: Arial, sans-serif;
  padding: 2rem;
  margin: 0;
}

h1 {
  text-align: center;
  color: #ef6c00;
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
  background-color: #ef6c00;
  color: white;
  border: none;
  cursor: pointer;
  transition: background 0.3s;
}

button:hover {
  background-color: #e65100;
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
  background-color: #ffe0b2;
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

