<script setup>
import Map from "../components/Map.vue";
</script>
<template>
  <div class = "result-view">
  <div class = "map-view">
    <Map></Map>
  </div>
  </div>
</template>

<style>
.result-view{
  position:fixed;
  width: 100vw;
  height: 100vh;
  left: 0px;
  top: 0px;
  background-color: #f2fdfe;
}
.map-view{
  position: fixed;
  top: 30vh;
  left: 11vw;
}
</style>