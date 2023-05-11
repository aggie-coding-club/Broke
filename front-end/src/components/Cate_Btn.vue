<!--
Description:

Component that creates the category buttons on the main page. This contains four
buttons: grocery, food, drinks, and gas.

Used in:

HomeView.vue
-->

<script>
export default {
    methods: {
        storeAndNavigate(category){
            this.$store.commit('setCategory', category)
            this.$router.push('/userinput')
        }
    }
}
</script>
<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Josefin+Sans">
    <div class = "cat-buttons">
        <ul>
            <li><button @click="storeAndNavigate('grocery')" class="cate_btn">Grocery</button></li>
            <li><button @click="storeAndNavigate('food')" class="cate_btn">Dining</button></li>
            <li><button @click="storeAndNavigate('drink')" class="cate_btn">Drinks</button></li>
            <li><button @click="storeAndNavigate('gas')" class="cate_btn">Gas</button></li>
        </ul>  
    </div>
</template> 

<style>
    ul {
        list-style-type: none;
    }
    .cate_btn{
        background-color: rgb(244, 244, 244);
        color: #808784;
        text-decoration: none;
        font-size: 2vw;
        padding: 3vh 2vw; 
        margin: 2vh 0px;
        border-radius: 15px;
        width: 20vw;
        transition: .4s;
        border: 1px solid black;
        font-family: "Josefin Sans", sans-serif;
    } 
    .cate_btn:hover{
        transform: scale(1.1);
        color: black;
    }
    .cat-buttons{
        right: 0px;
        top: 60px;
    }
</style>