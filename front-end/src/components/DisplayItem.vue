<script>
export default {
    props: {
        storeName: String,
        price: 0.0
    }
}
</script>

<template>
      <div class="result">
        <div class="flexbox">
          <div class="storeName">{{storeName}}</div>
          <div class="price">${{price}}</div>
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
</template>
    