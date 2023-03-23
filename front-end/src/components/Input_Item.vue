<template>
  <div>
    <div class = "title"> 
        <h2>Input Item</h2>
    </div>
    <input type="text" v-model="input" placeholder="Search..." />

    <div class = "title"> 
        <h2>Current Location</h2>
    </div>
    <input type="text" v-model="input" placeholder="Search..." />
  </div>
  
 </template>

<script setup>
import { ref } from "vue";
let input = ref("");

</script>

<style scoped>
.search_icon {
  width: 200px;

}
.title {
    display: flex;
    color:rgb(0, 0, 0);
    justify-content:center;
    text-align: center;

}
input {
  display: block;
  width: 500px;
  margin: 20px auto;
  padding: 10px 45px;
  background: rgb(244, 244, 244) url("@/assets/search-icon.svg") no-repeat 20px center;
  background-size: 15px 15px;
  font-size: 16px;
  border: none;
  border-radius: 10px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}

</style>
