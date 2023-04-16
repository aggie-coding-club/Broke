<script setup>
  import DisplayItem from './DisplayItem.vue'
  import { ref } from 'vue'
  const stores = ref([
    {id: 0, name: 'HEB', price: 10.99},
    {id: 1, name: 'Costco', price: 69.69},
    {id: 2, name: 'Walmart', price: 19.99},
  ])
</script>

<template>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inter+Tight">
<div class="resultBox">
  <div v-for="store in stores" :key="store.id">
    <DisplayItem :store-name=store.name :price=store.price></DisplayItem>
  </div>
  
</div>

</template>
<!--

  <div class="resultBox">
    <div class="result">
      <div class="flexbox">
        <div class="storeName">HEB</div>
        <div class="price">$19.99</div>
    </div>
    <div class="flexbox">
      <div class = "store-details">
        <div class="dist">2.5 mi</div>
        <div class="address">123 Main St. College Station, TX</div>
        <div class="hours">6AM - 6PM</div>
      </div>
      <div class="item-name">HEB Select Ingredients Tomato Sauce 8oz</div>
    </div>
    
  </div>
  <br>

  <div class="result">
    <div class="flexbox">
      <div class="storeName">Costco</div>
      <div class="price">$19.99</div>
    </div>
    <div class="flexbox">
      <div class = "store-details">
        <div class="dist">2.5 mi</div>
        <div class="address">123 Main St. College Station, TX</div>
        <div class="hours">6AM - 6PM</div>
      </div>
      <div class="item-name">Costco Select Ingredients Tomato Sauce 8oz</div>
    </div>
  </div>
  <br>
  
  <div class="result">
    <div class="flexbox">
       	<div class="storeName">Walmart</div>
        <div class="price">$19.99</div>
      </div>
      <div class="flexbox">
        <div class = "store-details">
        <div class="dist">2.5 mi</div>
        <div class="address">123 Main St. College Station, TX</div>
        <div class="hours">6AM - 6PM</div>
      </div>
      <div class="item-name">Walmart Select Ingredients Tomato Sauce 8oz</div>
    </div>
  </div>  
  <br>

  <div class="result">
    <div class="flexbox">
      <div class="storeName">Really Long Name Here</div>
        <div class="price">$19.99</div>
    </div>
    <div class="flexbox">
      <div class = "store-details">
        <div class="dist">2.5 mi</div>
        <div class="address">123 Main St. College Station, TX</div>
        <div class="hours">6AM - 6PM</div>
      </div>
      <div class="item-name">XXX Select Ingredients Tomato Sauce 8oz</div>
    </div>
  </div>
  <br>
  
  <div class="result">
    <div class="flexbox">
       	<div class="storeName">Brookshire Brothers Express (Add on for length)</div>
        <div class="price">$19.99</div>
    </div>
    <div class="flexbox">
      <div class = "store-details">
        <div class="dist">2.5 mi</div>
        <div class="address">123 Main St. College Station, TX</div>
        <div class="hours">6AM - 6PM</div>
      </div>
      <div class="item-name">Brookshire Brothers Select Ingredients Tomato Sauce 8oz</div>
    </div>
  </div>
  <br>

  <div class="result">
    <div class="flexbox">
       	<div class="storeName">Brookshire Brothers Express (Add on for length)</div>
        <div class="price">$19.99</div>
    </div>
    <div class="flexbox">
      <div class = "store-details">
        <div class="dist">2.5 mi</div>
        <div class="address">123 Main St. College Station, TX</div>
        <div class="hours">6AM - 6PM</div>
      </div>
      <div class="item-name">Brookshire Brothers Select Ingredients Tomato Sauce 8oz</div>
    </div>
  </div>
  <br>

  <div class="result">
    <div class="flexbox">
       	<div class="storeName">Brookshire Brothers Express (Add on for length)</div>
        <div class="price">$19.99</div>
    </div>
    <div class="flexbox">
      <div class = "store-details">
        <div class="dist">2.5 mi</div>
        <div class="address">123 Main St. College Station, TX</div>
        <div class="hours">6AM - 6PM</div>
      </div>
      <div class="item-name">Brookshire Brothers Select Ingredients Tomato Sauce 8oz</div>
    </div>
  </div>
  <br>

  <div class="result">
    <div class="flexbox">
       	<div class="storeName">Brookshire Brothers Express (Add on for length)</div>
        <div class="price">$19.99</div>
    </div>
    <div class="flexbox">
      <div class = "store-details">
        <div class="dist">2.5 mi</div>
        <div class="address">123 Main St. College Station, TX</div>
        <div class="hours">6AM - 6PM</div>
      </div>
      <div class="item-name">Brookshire Brothers Select Ingredients Tomato Sauce 8oz</div>
    </div>
  </div>
  <br>

  <div class="result">
    <div class="flexbox">
       	<div class="storeName">Brookshire Brothers Express (Add on for length)</div>
        <div class="price">$19.99</div>
      </div>
    <div class="flexbox">
      <div class = "store-details">
        <div class="dist">2.5 mi</div>
        <div class="address">123 Main St. College Station, TX</div>
        <div class="hours">6AM - 6PM</div>
      </div>
      <div class="item-name">Brookshire Brothers Select Ingredients Tomato Sauce 8oz</div>
    </div>
  </div>
  <br>

  <div class="result">
    <div class="flexbox">
       	<div class="storeName">Brookshire Brothers Express (Add on for length)</div>
        <div class="price">$19.99</div>
    </div>
    <div class="flexbox">
      <div class = "store-details">
        <div class="dist">2.5 mi</div>
        <div class="address">123 Main St. College Station, TX</div>
        <div class="hours">6AM - 6PM</div>
      </div>
      <div class="item-name">Brookshire Brothers Select Ingredients Tomato Sauce 8oz</div>
    </div>
  </div>
</div>  
</template>
-->



<style>
.resultBox {
  width: 40vw;
  height: 70vh;
  overflow-y: scroll;
}
.result {
  padding: 20px;
  outline: 2px solid black;
  margin: 5px;
  border-radius:16px;
  background-color: rgb(244, 244, 244) /*#d9d9d9*/;
}
.flexbox {
  display:flex;
  justify-content:space-between;
}
.storeName {
  font-weight: bold;
}
.storeName, .price {
  color: #da2c2c;
  font-size: 2em;
}
.dist, .address, .hours {
  color: black;
  font-size: 1.3em;
}
.item-name{
  overflow-wrap: break-word;
  max-width: 15vw; 
  text-align: right;
}
.storeName, .price, .dist, .address, .hours{
  font-family: "Inter Tight", sans-serif;
}
</style>
