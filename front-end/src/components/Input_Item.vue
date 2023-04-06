export default {
  data() {
    return {
      isActive: false,
    };
  },
};


<template>
  <div>
    <div class = "title"> 
        <h2>Input Item</h2>
    </div>
    <input class ="text" type="text" v-model="input" placeholder="Search..." />

    <div class = "title"> 
        <h2>Current Location</h2>
    </div>
    <input class ="text" type="text" v-model="input2" placeholder="Search..." />

    <div class = "title">
        <h2>Search Radius (miles)</h2>
    </div>
    <div class = "radius-buttons">
    <button class ="buttons" @click="toggle">1</button>
    <button class ="buttons" @click="toggle">5</button>
    <button class ="buttons" @click="toggle">10</button>
    <button class ="buttons" @click="toggle">15</button>
    <button class ="buttons" @click="toggle">20</button>
     </div>
     <div class = "bottom-user">
      <div class = "open-store">
        <label class = "open-store-label">Display open stores only </label>
        <input type ="checkbox" value="Display open stores only" id="Display open stores only" class = "checkbox">
      </div>
      <router-link to="/result" custom v-slot="{ navigate }">
        <button class="pill" @click="navigate">Search</button>
      </router-link>
    </div>
    
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
    font-size: 19px;
    top: 10px;
}

input.text {
  display: block;
  width: 42vw; /*600px*/
  height: 6vh;
  margin: 20px auto;
  padding: 10px 45px;
  background: rgb(244, 244, 244) url("@/assets/search-icon.svg") no-repeat 20px center;
  background-size: 15px 15px;
  font-size: 18px;
  border: none;
  border-radius: 10px;
  box-shadow: hsla(240, 30%, 28%, 0.251) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}

input.checkbox{
  width: 3vh;
  height: 3vh;
  vertical-align: middle;
  left: 0.5vw;
}

.buttons {
  justify-content: center;
  width:4vw; /*50px*/
  height:7vh;
  text-align:center;
  margin-top: 32px;
  margin-left: auto;
  margin-right: auto;
  box-shadow: #32325d40 0px 2px 5px -1px;
  background: rgb(244, 244, 244);
  border: 1px solid black;
}
.buttons:hover{
  transform: scale(1.1);
}
.radius-buttons{
  display: flex;
  justify-content: center;
}

.pill {
  border-radius: 15px;
  padding: 2vh 2vw;
  box-shadow: #32325d40 0px 2px 5px -1px;
  left: 17vw;
  background: rgb(244, 244, 244);
  border: 1px solid black;
  font-size: 18px;
}
.pill:hover{
  transform: scale(1.1);
}
.open-store{
  left: 15vw;
  width: 20vw;
  top: 1vh;
}
.open-store-label{
  font-size: 18px;
}

.bottom-user{
  display: flex;
  width: 44vw;
  left: 3vw;
  top: 5vh;
}
</style>

