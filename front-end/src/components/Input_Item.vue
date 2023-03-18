<template>
  <div>
    <div class = "inputitem">
        <h2>Input Item</h2>
    </div>
    <input type="text" v-model="input" placeholder="Search..." />
  </div>
 </template>

<script setup>
import { ref } from "vue";
let input = ref("");

</script>

<style scoped>
.inputitem {
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
  background: rgb(224, 223, 223);
  background-size: 15px 15px;
  font-size: 16px;
  border: none;
  border-radius: 10px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}


.item {
  width: 350px;
  margin: 0 auto 10px auto;
  padding: 10px 20px;
  color: rgb(0, 0, 0);
  border-radius: 5px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 3px 0px,
    rgba(0, 0, 0, 0.06) 0px 1px 2px 0px;
}
</style>
