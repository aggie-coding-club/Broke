<template>
    <div class="resultBox">
	<div class="result">
    	<div class="flexbox">
       	 	<div class="storeName">HEB</div>
        	<div class="price">$19.99</div>
        </div>
        <div class="dist">2.5 mi</div>
        <div class="address">123 Main St. College Station, TX</div>
        <div class="hours">6AM - 6PM</div>
    </div>
    <div class="result">
    	<div class="flexbox">
       	 	<div class="storeName">Costco</div>
        	<div class="price">$19.99</div>
        </div>
        <div class="dist">2.5 mi</div>
        <div class="address">123 Main St. College Station, TX</div>
        <div class="hours">6AM - 6PM</div>
    </div>
    </div>
</template>



<style>
body {
  background-color:#E7E9EB;
}

.resultBox {
  background-color: lightblue;
  width: 400px;
  height: 200px;
  overflow-y: scroll;
}
.result {
  padding: 20px;
  outline: 2px solid black;
  margin: 5px;
  border-radius:16px;
  background-color:#D6D6D6;
}
.flexbox {
  display:flex;
  justify-content:space-between;
}
</style>
