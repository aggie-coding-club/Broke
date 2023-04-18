<template>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Josefin+Sans">
  <div>
    <div class = "title"> 
        <h2>Input Item</h2>
    </div>
    <input class ="text" type="text" v-on:input="updateItem" placeholder="Search..." />

    <div class = "title"> 
        <h2>Current Location</h2>
    </div>
    <input class ="text" type="text" v-on:input="updateLocType" placeholder="Search..." />

    <div class = "title">
        <h2>Search Radius (miles)</h2>
    </div>
    <div class = "radius-buttons">
    <button class ="buttons" @click = updateRadius(1)>1</button>
    <button class ="buttons" @click = updateRadius(5)>5</button>
    <button class ="buttons" @click = updateRadius(10)>10</button>
    <button class ="buttons" @click = updateRadius(15)>15</button>
    <button class ="buttons" @click = updateRadius(20)>20</button>
     </div>
     <div class = "bottom-user">
      <div class = "open-store">
        <label class = "open-store-label">Display open stores only </label>
        <input type ="checkbox" value="Display open stores only" id="Display open stores only" class = "checkbox">
      </div>
      <router-link to="/result" custom v-slot="{ navigate }">
        <button class="pill" @click="createGet()">Search</button>
        <!--<button class="pill" @click = navigate>Search</button>-->
      </router-link>
    </div>
    
  </div>
 
 </template>

<script setup>
import { ref } from "vue";
let input = ref("");
</script>

<script>
import axios from "axios";

export default{
  data(){
    return {
      postData: {
        item: '',
        location: ''
      },
      getData: {
        loctype: '',
        item: '',
        location: '',
        radius: 5
      },
      getResponse: [],
      postResponse: []
    }
  },

  mounted(){
      this.$store.commit('setAddress', "")
      //this.getData.loctype = ""
      this.$store.commit('setItem', "")
      //this.getData.item = ""
      this.$store.commit('setRadius', 5)
      //this.getData.radius = 5
  },

  methods: {
    createPost(){
      axios.post('http://127.0.0.1:5000/restdemo', this.postData)
        .then((response) => {this.postResponse = JSON.stringify(response.data); this.printData('post');})
        this.$router.push('/result')
    },

    createGet(){
      if(this.$store.state.address !== "" && this.$store.state.item !== ""){
        axios.post('http://127.0.0.1:5000/findlocations', {'loctype': this.$store.state.locationType,
            'item': this.$store.state.item, 'address': this.$store.state.address, 'radius': this.$store.state.radius})
          .then((response) => {this.postResponse = JSON.stringify(response.data); this.$store.commit('setPostResponse',
            this.postResponse); this.printData('post'); this.$router.push('/result');})
      }
    },

    printData(typeOfData){
      if(typeOfData === 'post'){
        console.log(JSON.parse(this.postResponse))
        console.log(this.$store.state.postResponse)

        const res = JSON.parse(this.$store.state.postResponse);
        this.$store.commit('setPostResponse', res);


      }else if(typeOfData === 'get'){
        console.log(JSON.parse(this.getResponse))
      }
    },

    increment(){
      console.log(this.$store.state.locationType)
      console.log(this.$store.state.item)
      console.log(this.$store.state.radius)

    },

    updateLocType(event){
      this.$store.commit('setAddress', event.target.value)
    },

    updateItem(event){
      this.$store.commit('setItem', event.target.value)
    },

    updateRadius(r){
      this.$store.commit('setRadius', r)
    }
  }
}
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
.title h2{
  font-family: "Josefin Sans", sans-serif;
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
  font-family: "Josefin Sans", sans-serif;
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
  font-family: "Josefin Sans", sans-serif;
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
  font-family: "Josefin Sans", sans-serif;
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
  font-family: "Inter Tight", sans-serif;
}

.bottom-user{
  display: flex;
  width: 44vw;
  left: 3vw;
  top: 5vh;
}
h2{
  font-family: "Inter Tight", sans-serif;
}
</style>

