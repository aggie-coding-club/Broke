<script setup>
import Cate_btn from '../components/Cate_btn.vue'
import Description from '../components/Description.vue'
</script>
<template>
  <div class = "home-view">

    <div class = "intro">
      <Description />
    </div>

    <main class = "intro">
      <Cate_btn />
    </main>

  </div>
</template>

<style>
.intro{
  display: inline-block;
  padding: 1rem 1rem;
  vertical-align: middle;
}
.home-view{
  height: 70vh;
  width: 80vw;
  left: 30px;
}
</style>


