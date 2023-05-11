<!--
Description:

Component that creates a single display box that contains the information for
a single store returned from the back-end.

Used in:

PlaceholderStores.vue
-->

<script>
export default {
  props: {
      storeName: String,
      price: 0.0,
      itemName: String,
      address: String,
      distance: 0.0,
      hours: "N/A"
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
        <div class="dist">{{distance}} mi</div>
        <div class="address">{{address}}</div>
        <div class="hours">Hours: {{hours}}</div>
      </div>
      <div class="item-name">{{itemName}}</div>
    </div>
  </div>
  <br>
</template>
    