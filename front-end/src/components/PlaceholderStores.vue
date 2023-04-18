<script setup>
  import DisplayItem from './DisplayItem.vue'
</script>

<script>
import axios from "axios";

export default{
  data(){
    return {
      results: [],
      loading: true,
      processedData: [],
      id:0
    }
  },
  mounted(){
    if(this.$store.state.address !== "" && this.$store.state.item !== ""){
      axios.post('http://127.0.0.1:5000/findlocations', {'loctype': this.$store.state.category,
          'item': this.$store.state.item, 'address': this.$store.state.address, 'radius': this.$store.state.radius})
        .then((response) => {this.results = JSON.parse(JSON.stringify(response.data));}).then(() =>
          {
            for (const key in this.results){
              if(this.results.hasOwnProperty(key)){
                var jsonData = [this.id, key, this.results[key][0], this.results[key][1], this.results[key][2]]

                this.processedData.push(jsonData)

                this.id += 1
              }
            }

            this.loading = false;
          }
        )
    }
  }
}
</script>

<template>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inter+Tight">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Josefin+Sans">
<div class="resultBox" v-show="!loading">
  <div v-for="store in processedData" :key="store[0]">
    <DisplayItem :store-name=store[1] :item-name=store[2] :price=store[3]
      :address=store[4] :hours="'N/A'" :distance=0.0></DisplayItem>
  </div>
</div>
<div class="loading-text" v-show="loading">
  <h1>Loading...</h1>
</div>

</template>

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
  font-family: "Inter Tight", sans-serif;
}
.item-name{
  overflow-wrap: break-word;
  max-width: 15vw; 
  text-align: right;
  font-family: "Josefin Sans", sans-serif;
  font-size: 1.0em;
}
.store-details{
  color: black;
  font-size: 1.2em;
  font-family: "Josefin Sans", sans-serif;
}
.loading-text{
  
}
</style>
