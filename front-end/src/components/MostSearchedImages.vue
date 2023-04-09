<script>
export default {
  data() {
    return {
      item1: 'Honey',
      item2: 'Banana',
      item3: 'Ground beef',
      item4: 'Doritos',
      item5: 'Brownie Mix',
      item6: 'Milk',
    }
  }
}
</script>

<template>

    <h2 class="searched-header-text">Most Searched Items in the last week: </h2>
    <div class="item_pictures">
        <div class="item_picture-wrapper">
            <div class="item_text-wrapper"> 
                <p @click="searchItem" class="item_text">{{item1}}</p>
            </div>
            <div class="item_picture">
                <img src="../assets/honeyIMG.jpg" alt="image-here" class="item-pic">
            </div>
        </div>
        <div class="item_picture-wrapper">
            <div class="item_text-wrapper"> 
                <p class="item_text">{{item2}}</p>
            </div>
            <div class="item_picture">
                <img src="../assets/bananaIMG.jpg" alt="" class="item-pic">
            </div>
        </div>
        <div class="item_picture-wrapper">
            <div class="item_text-wrapper"> 
                <p class="item_text">{{item3}}</p>
            </div>
            <div class="item_picture">
                <img src="../assets/groundBeefIMG.jpg" alt="" class="item-pic">   
            </div>
        </div>
        <div class="item_picture-wrapper">
            <div class="item_text-wrapper"> 
                <p class="item_text">{{item4}}</p>
            </div>
            <div class="item_picture">
                <img src="../assets/DoritosIMG.png" alt="" class="item-pic">  
            </div>
        </div>
        <div class="item_picture-wrapper">
            <div class="item_text-wrapper"> 
                <p class="item_text">{{item5}}</p>
            </div>
            <div class="item_picture">
                <img src="../assets/brownieMixIMG.jpg" alt="" class="item-pic">
            </div>
        </div>
        <div class="item_picture-wrapper">
            <div class="item_text-wrapper"> 
                <p class="item_text">{{item6}}</p>
            </div>
            <div class="item_picture">
                <img src="../assets/milkIMG.jpg" alt="" class="item-pic">
            </div>
        </div>


    </div>
</template>

<style>
.item_pictures{
    display: flex;
    flex-wrap: wrap;
  	height: 365px;
  	width: 35vw;
    margin-left: 0px;
    margin-top: 32px;
    border: 2px solid red;
}

.searched-header-text{
    display: flex;
    align-items: center;
    line-height: 39px;
    text-align: center;
    color-scheme: #000000;
    font-size: 32px;
    font-weight: 400;
    width: 35vw;
    margin: 0 auto;
}

.item_text-wrapper{
    display: flex;
    justify-content: center;
    align-items:center;
}

.item-text{
    font-weight: 400;
    font-size: 24px;
}

.item_picture{
    box-sizing: border-box;
    border: 1px solid black;
    margin-top: 8px;
    margin-right: 22px;
    margin-left: 22px;
    height: 122px;
    width: 122px;
    border: 1px solid #000000;
    filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
    border-radius: 20px;
}

.item-pic{
    height: 120px;
    width: 120px;
    border-radius: 20px;
}

</style>