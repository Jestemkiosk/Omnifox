<template>
    <div>
        <CitiesHeader />
            <div class="cities">
                <h1>API Endpoint: http://localhost:5000/cities</h1>
                <div class="row" v-bind:key="cities.index" v-for="cities in chunkedCities">
                    <City v-bind:city="city" v-bind:key="city.id" v-for="city in cities"/>
                </div>
            </div>
        <Footer />
    </div>
</template>

<script>
import City from '../components/City.vue'
import CitiesHeader from "../components/CitiesHeader.vue"
import Footer from "../components/Footer.vue"

import axios from 'axios'
import chunk from 'chunk'

export default {
    name: "CitiesView",
    components: {
        CitiesHeader,
        Footer,
        City
    },
    data(){
        return{
            cities: [

            ]
        }
    },
    created(){
        axios.get('http://localhost:5000/cities/')
        .then(res => {
        this.cities = res.data
        console.log(this.cities)
        })
        .catch(err => console.log(err))
    },
    computed: {
        chunkedCities(){
            return chunk(this.cities, 4)
        }
    }
}
</script>

<style scoped>
.cities{
    margin: 50px 50px;
}

h1{
    color:black;
    text-align: center;
    font-size: 0.7em;
    margin: 20px;
}
</style>