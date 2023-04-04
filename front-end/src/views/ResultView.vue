<script setup>
import Map from "../components/Map.vue";
import Nav from '../components/Nav.vue'
</script>
<template>
  <nav>
    <Nav />
  </nav>
  <main class = "result-view">
    <Map></Map>
  </main>
</template>

<style>
.result-view{
  position:fixed;
  top: 30vh;
  left: 12vw;
}
</style>