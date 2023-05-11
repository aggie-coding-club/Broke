<!--
Description:

Component that creates the Google maps display on the results page. This
feature is currently not fully working.

Used in:

ResultView.vue
-->

<template>
  <div class="map-wrapper">
    <img
      src="@/assets/map.png"
      alt="placeholder image for map"
      class="map-img"
    />
  </div>
</template>

<style>
.map-wrapper {
  width: 490px;
  height: 450px;
}

.map-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 5%;
}
</style>
