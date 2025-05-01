<script setup lang="ts">
import { ref, onMounted, onUnmounted, type Ref } from 'vue'
import * as L from 'leaflet'
import 'leaflet/dist/leaflet.css'

const mapContainer: Ref<HTMLElement | null> = ref(null)
let map: L.Map | null = null

function initMap() {
  if (mapContainer.value) {
    if (map) {
      map.remove()
    }
    
    // Initialize the map
    map = L.map(mapContainer.value, {
      zoomControl: true,
      scrollWheelZoom: true,
      dragging: true
    }).setView([51.505, -0.09], 13)
    
    // Add the OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
    }).addTo(map)

    // Move zoom control to top-right
    map.zoomControl?.setPosition('topright')
  }
}

function handleResize() {
  if (map) {
    map.invalidateSize()
  }
}

onMounted(() => {
  initMap()
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  if (map) {
    map.remove()
  }
})
</script>

<template>
  <div ref="mapContainer" class="map-container"></div>
</template>

<style scoped>
.map-container {
  width: 100%;
  height: 100%;
  min-height: 200px;
  border-radius: 6px;
  overflow: hidden;
  position: relative;
  flex: 1;
}

:deep(.leaflet-control-zoom) {
  border: none;
  margin-right: 12px;
  margin-top: 12px;
}

:deep(.leaflet-control-zoom-in),
:deep(.leaflet-control-zoom-out) {
  border: none !important;
  width: 30px !important;
  height: 30px !important;
  line-height: 30px !important;
  background-color: white !important;
  color: #666 !important;
  font-size: 16px !important;
  border-radius: 4px !important;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1) !important;
}

:deep(.leaflet-control-zoom-in) {
  margin-bottom: 4px !important;
}
</style> 