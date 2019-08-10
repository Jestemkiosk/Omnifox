<template>
    <div>
        <FoxesHeader />
            <div class="foxes">
                <h1>API Endpoint: http://localhost:5000/foxes</h1>
                <div class="row" v-bind:key="foxes.index" v-for="foxes in chunkedFoxes">
                    <Fox v-bind:fox="fox" v-bind:key="fox.id" v-for="fox in foxes"/>
                </div>
            </div>
        <Footer />
    </div>
</template>

<script>
import Fox from '../components/Fox.vue'
import FoxesHeader from "../components/FoxesHeader.vue"
import Footer from "../components/Footer.vue"

import axios from 'axios'
import chunk from 'chunk'

export default {
    name: "FoxesView",
    components: {
        FoxesHeader,
        Footer,
        Fox
    },
    data(){
        return{
            foxes: [

            ]
        }
    },
    created(){
        axios.get('http://localhost:5000/foxes/')
        .then(res => {
        this.foxes = res.data
        console.log(this.foxes)
        })
        .catch(err => console.log(err))
    },
    computed: {
        chunkedFoxes(){
            return chunk(this.foxes, 4)
        }
    }
}
</script>

<style scoped>
.foxes{
    margin: 50px 50px;
}

h1{
    color:black;
    text-align: center;
    font-size: 0.7em;
    margin: 20px;
}
</style>