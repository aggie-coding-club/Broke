<!--
  Description:
  
  Home page of the website, allow users to select a category relevant to their query.
  Consists of category buttons and description of the website purpose.
  Logo and footer are displayed on the home page but are used in App.vue.
-->


<script setup>
import Cate_btn from '../components/Cate_Btn.vue'
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
  left: 10vw;
  top: 8vw;
}
.home-view{
  height: 100vh;
  width: 100vw;
  position: fixed;
  left: 0vw;
  top: 0vw;
  background-color: #f2fdfe;
}
</style>


