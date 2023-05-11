<!--
  Description:

  Final page displaying results of search.
  Store information displayed to the right in individual rounded boxes.
  Google map with store location displayed to the left (currently just a place-holder).
  Logo, navigation bar, and footer are displayed on the result page but are used in App.vue.
-->

<script setup>
import Map from "../components/Map.vue";
import PlaceholderStores from "../components/PlaceholderStores.vue";
import Nav from '../components/Nav.vue'

</script>

<template>
  <div class = "result-view">
    <div class = "map-view">
      <Map></Map>
    </div>
    <div class = "stores-view">
      <PlaceholderStores></PlaceholderStores>
    </div>
    <div>
      <Nav></Nav>
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
.stores-view{
  position: fixed;
  right: 10vw;
  top: 20vh;
}
</style>