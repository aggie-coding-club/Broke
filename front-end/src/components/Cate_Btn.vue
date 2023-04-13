<script>
export default {
    methods: {
        grocery_page() {
            console.log("grocery") // grocery will be printed out to console when that button is clicked, the actual functionality will be added later on
        },
        dinning_page() {
            console.log("dinning")
        },
        drinks_page() {
            console.log("drinks")
        },
        gas_page() {
            console.log("gas")
        },
    }
}
</script>
<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inter+Tight">
    <div class = "cat-buttons">
        <ul>
            <router-link to="/userinput" custom v-slot="{ navigate }">
            <!--
            <li><button @click="grocery_page" role = "link" class="cate_btn">Grocery</button></li>
            <li><button @click="dinning_page" class="cate_btn">Dining</button></li>
            <li><button @click="drinks_page" class="cate_btn">Drinks</button></li>
            <li><button @click="gas_page" class="cate_btn">Gas</button></li>
            -->
            <li><button @click="navigate" class="cate_btn">Grocery</button></li>
            <li><button @click="navigate" class="cate_btn">Dining</button></li>
            <li><button @click="navigate" class="cate_btn">Drinks</button></li>
            <li><button @click="navigate" class="cate_btn">Gas</button></li>
            </router-link>
        </ul>  
    </div>
</template>

<style>
    ul {
        list-style-type: none;
    }
    .cate_btn{
        background-color: rgb(244, 244, 244)/*#dcf7f9 #f0fbff*/;
        color: #808784;
        text-decoration: none;
        font-size: 2vw;
        padding: 3vh 2vw; 
        margin: 2vh 0px;
        border-radius: 15px;
        /*left: 9vw;*/
        width: 20vw;
        transition: .4s;
        border: 1px solid black;
        font-family: "Inter Tight", sans-serif;
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