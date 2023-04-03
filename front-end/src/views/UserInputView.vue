<script setup>
import Input_Item from '../components/Input_Item.vue'
import Searched_images from '../components/MostSearchedImages.vue'
</script>

<template>
  <div class="input-view">
    <div class="searched-images">
      <Searched_images />
    </div>
    <main class = "input-page">
      <Input_Item />
    </main>
  </div>
</template>

<style>
.input-view{
  height: 70vh;
  width: 80vw;
  position: fixed; /*changed from absolute to fixed*/
  /*right: -10vw;
  bottom: -25vh;*/
  left: 10vw;
  top: 8vw;
}

.searched-images{
  margin-top: 12vh;
  display: inline-block;
  padding: 1rem 1rem;
  vertical-align: middle;
  left: 4vw;
}

.input-page{
  position: fixed;
  width: 48vw;
  height: 80vh;
  justify-content: center;
  /*top: -27vh;
  left: -5vw;*/
  right: 5vw;
  top: 25vh;
}
</style>