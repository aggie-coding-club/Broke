<script setup>
import { RouterLink, RouterView } from "vue-router";
import Footer from "./components/Footer.vue";
import Logo from "./components/logo.vue";
</script>

<template>
 
 <header>
    <Logo />
  </header>
  <div>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/userinput">Input</RouterLink>
    </nav>

    <RouterView v-slot = "{Component}">

      <transition :name="fade" out-in>
        <Component :is="Component" />
      </transition>

    </RouterView>
  </div>
  
  <Footer></Footer>

</template>

<style scoped>

header {
  line-height: 1;
  max-height: 100vh;
  width: 30vw;
  height: 20vh;
  
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  /*
  header {
    display: flex;
    place-items: top;
    padding-right: calc(var(--section-gap) / 2);
  }*/

  .logo {
    margin: 0 2rem 0 0;
  }

  /*
  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }*/
  
  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }

  footer {
    text-align: center;
  }

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease-out;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

  }
</style>
