<!--
Description:

Component that creates the navbar that allows the user to go back to the home page.

Used in:

ResultView.vue, UserInputView.vue
-->

<script>
</script>

<template>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Josefin+Sans">
    <nav>
        <ul class="navbar">
            <a href="/">
            <li><button class = "navbar-button">Home</button></li>
            </a>
        </ul>
    </nav>

</template>

<style>
    .navbar {
        position: fixed;
        top: 0px;
        left: 0px;
        list-style-type: none;
        /*background-color:rgb(244, 244, 244);*/
        width: 100%;
        height: 43px;
        /*border-bottom: 1px solid rgb(200, 200, 200);*/
    }
    .navbar-button {
        background-color: white;
        display: inline;
        font-size: 16px;
        margin-top: 10px;
        height: 35px;
        width: 80px;
        border-radius: 20px;
        font-family: 'Josefin Sans', sans-serif;
    }
    .navbar-button:hover{
        transform: scale(1.1);
    }
</style>