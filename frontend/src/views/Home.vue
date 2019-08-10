<template>
  <div id="app">
    <MainHeader />
    <Features />
    <Collage />
    <Feedback />
    <Cities v-bind:cities="cities" />
    <Footer />
  </div>
</template>

<script>
import MainHeader from "../components/MainHeader.vue"
import TopNav from "../components/Cities.vue"
import Features from "../components/Features.vue"
import Collage from "../components/Collage.vue"
import Steps from "../components/Steps.vue"
import Feedback from "../components/Feedback.vue"
import Cities from "../components/Cities.vue"
import Footer from "../components/Footer.vue"

import axios from 'axios'

export default {
    name: "app",
    components: {
        MainHeader,
        TopNav,
        Features,
        Collage,
        Steps,
        Feedback,
        Cities,
        Footer
    },
    data(){
        return{
            foxes:[

            ],
            cities:[

            ]
        }
    },
    created(){
        axios.get('http://localhost:5000/cities/')
        .then(res => {
        this.cities = res.data
        })
        .catch(err => console.log(err))

        axios.get('http://localhost:5000/foxes/')
        .then(res => {
        this.foxes = res.data
        })
        .catch(err => console.log(err))
    }
};

</script>

<style>


</style>