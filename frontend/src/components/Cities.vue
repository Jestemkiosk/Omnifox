<template>
<div>
    <section v-if="cities.length > 0" class="section-cities">
        <div class="row">
            <h2 class="col span-1-of-1"> We're currently in these cities</h2>
        </div>
        <div class="row">
            <City v-bind:city="city" v-bind:key="city.id" v-for="city in chunkedCities[0]"/>
        </div>
        <div class="row more-cities">
            <h4 v-if="cities.length>4" class="col span-1-of-1">And {{cities.length-4}} more! Check the full list <a href="/cities">here!</a></h4>
            <h4 v-else style="display: none"></h4>
        </div>
    </section>
    <div v-else>
    </div>
</div>

</template>

<script>
import City from './City.vue'
import chunk from 'chunk'

export default {
    name: "Cities",
    components: {
        City
    },
    props: ["cities"],
    computed: {
        chunkedCities(){
            return chunk(this.cities, 4)
        }
    }
}
</script>

<style scoped>

a{
    font-weight: 500;
    color: #e67e22;
    text-decoration: underline;
}

.more-cities{
  margin-top: 30px;
  text-align: center;
}



/* Small tablet to big tablet: from 768px to 1023px */
@media only screen and (max-width: 1023px){
    .section-cities{
    font-size: 0.7em;
    }

    h4{
        font-size: 1.5em;
    }
}

/* Small phones: from 0 to 480px */
@media only screen and (max-width: 480px){
    .section-cities ul{
        margin-bottom: 15px;
    }

    .section-cities .span-1-of-4 {
        width: 47.6%;
    }
}

</style>