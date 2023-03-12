<template>
    <ul>
        <li><button class="cate_btn">Grocery</button></li>
        <li><button class="cate_btn">Dinning</button></li>
        <li><button class="cate_btn">Drinks</button></li>
        <li><button class="cate_btn">Gas</button></li>
    </ul>  
</template>

<style>
    ul {
        list-style-type: none;
    }
    .cate_btn{
        background-color: #c1b599;
        color: black;
        text-decoration: none;
        border: 2px solid transparent;
        font-size: 25px;
        padding: 20px 25px;
        margin: 15px 0px;
        border-radius: 15px;
        width: 250px;
        transition: .4s;
    }
    .cate_btn:hover{
        transform: scale(1.1);
    }
</style>