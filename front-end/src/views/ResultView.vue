<script setup>
import Map from "../components/Map.vue";
import PlaceholderStores from "../components/PlaceholderStores.vue";
</script>
<template>
  <main class = "result-view">
    <Map></Map>
  </main>
  <PlaceholderStores></PlaceholderStores>
</template>

<style>
.result-view{
  position:fixed;
  top: 30vh;
  left: 12vw;
}
</style>