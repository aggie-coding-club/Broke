import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from './App.vue'
import router from './router'

import './assets/main.css'

const store = createStore({
    state () {
        return {
            category: "",
            item: "",
            address: "",
            radius: 0,
            postResponse: {}
        }   
    },
    mutations: {
        setCategory(state, category){
            state.category = category;
        },

        setItem(state, item){
            state.item = item;
        },

        setRadius(state, r){
            state.radius = r;
        },

        setAddress(state, addr){
            state.address = addr;
        },

        setPostResponse(state, pr){
            state.postResponse = pr;
        }
    }
})

const app = createApp(App)

app.use(router)
app.use(store)

app.mount('#app')
