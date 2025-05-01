<script setup lang="ts">
import { ref, onMounted, type Ref } from 'vue'
import MapView from './components/MapView.vue'

interface BackendResponse {
  message: string;
  status: string;
}

const message: Ref<string> = ref('')
const healthStatus: Ref<string> = ref('')

async function fetchData() {
  try {
    const response = await fetch('http://localhost:8000/')
    const data: BackendResponse = await response.json()
    message.value = data.message
  } catch (error) {
    console.error('Error fetching data:', error)
    message.value = 'Error connecting to backend'
  }
}

async function checkHealth() {
  try {
    const response = await fetch('http://localhost:8000/api/health')
    const data: BackendResponse = await response.json()
    healthStatus.value = data.status
  } catch (error) {
    console.error('Error checking health:', error)
    healthStatus.value = 'unhealthy'
  }
}

onMounted(() => {
  fetchData()
  checkHealth()
})
</script>

<template>
  <div class="dashboard">
    <header>
      <h1>Dashboard</h1>
      <div class="status-pill" :class="{ 'status-healthy': healthStatus === 'healthy' }">
        Backend Status: {{ healthStatus }}
      </div>
    </header>
    
    <div class="dashboard-content">
      <div class="dashboard-left">
        <div class="card system-info">
          <h2>System Information</h2>
          <p>{{ message }}</p>
        </div>
        
        <div class="card">
          <h2>Quick Stats</h2>
          <div class="stats-grid">
            <div class="stat-item">
              <h3>Users</h3>
              <p>0</p>
            </div>
            <div class="stat-item">
              <h3>Active</h3>
              <p>0</p>
            </div>
            <div class="stat-item">
              <h3>Tasks</h3>
              <p>0</p>
            </div>
            <div class="stat-item">
              <h3>Completed</h3>
              <p>0</p>
            </div>
          </div>
        </div>
      </div>
      
      <div class="dashboard-right">
        <div class="card map-card">
          <h2>Map View</h2>
          <MapView />
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* Reset default margins and padding */
body {
  margin: 0;
  padding: 0;
  overflow: hidden;
}

#app {
  height: 100vh;
  width: 100vw;
}
</style>

<style scoped>
.dashboard {
  height: 100vh;
  width: 100vw;
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

header {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.5rem;
  background-color: white;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.status-pill {
  padding: 0.25rem 1rem;
  border-radius: 20px;
  background-color: #52c41a;
  color: white;
  font-size: 0.9rem;
  font-weight: 500;
}

.dashboard-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  padding: 1.5rem;
  flex: 1;
  overflow: hidden;
  height: calc(100vh - 64px); /* Subtract header height */
}

.dashboard-left {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  height: 100%;
  overflow-y: auto;
}

.dashboard-right {
  height: 100%;
  overflow: hidden;
}

.card {
  background: white;
  padding: 1.25rem;
  border-radius: 8px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.system-info {
  flex: 0 0 auto;
}

.map-card {
  height: 100%;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.map-card h2 {
  margin-bottom: 1rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  margin-top: 1rem;
}

.stat-item {
  text-align: center;
  padding: 1rem;
  background: #f8f8f8;
  border-radius: 6px;
}

.stat-item h3 {
  margin: 0;
  color: #666;
  font-size: 0.9rem;
  font-weight: normal;
}

.stat-item p {
  margin: 0.25rem 0 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: #2c3e50;
}

h1 {
  color: #2c3e50;
  margin: 0;
  font-size: 1.75rem;
  font-weight: 600;
}

h2 {
  color: #42b983;
  font-size: 1.1rem;
  margin: 0;
  font-weight: 500;
}

p {
  margin: 0.5rem 0;
  color: #666;
}

@media (max-width: 1024px) {
  .dashboard-content {
    grid-template-columns: 1fr;
    height: auto;
    overflow: auto;
  }
  
  .map-card {
    height: 400px;
  }
}

@media (max-width: 640px) {
  .dashboard {
    height: auto;
  }
  
  .dashboard-content {
    padding: 1rem;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
}
</style>
