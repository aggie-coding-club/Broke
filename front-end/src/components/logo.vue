<template>
    <div class="logo-wrapper">
        <img src="@/assets/broke-logo.png" alt="logo" class="logo-picture">
        <div class="logo-text">
            <h2>Budget Guard</h2>
        </div>
    </div>
</template>


<style>
.logo-wrapper{
    height: 19vh;
    display: flex;
    align-items: center;
    justify-content: center;
    /*
    right: 38vw;
    bottom: 35vh;
    */
    left: 10vw;
    top: 5vh;
    position: fixed;
    z-index: 1;
}

.logo-picture{
    border-radius: 50%;
    height: 19vh;
    width: 12vw;
    /*margin: 0 auto;*/
}
.logo-text{
    height: 8vh;
    width: 20vw;
    left: 1vw;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3vw;
    color: #000000;
}
</style>