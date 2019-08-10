<template>
    <div class="col city-box">
          <figure class="city-photo">
            <img :src="city.image_url" alt="">
          </figure>
          <h3>{{city.name}}</h3>
          <ul>
            <li><MdPersonIcon class='icon-small'/>{{city.users}} foxlovers</li>
            <li v-if="city.foxes"><MdPawIcon class='icon-small'/>{{city.foxes.length}} beautiful foxes</li>
            <li v-else><MdPawIcon class='icon-small'/>No foxes yet!</li>
          </ul>
        </div>
</template>

<script>
import MdPawIcon from 'vue-ionicons/dist/md-paw.vue'
import MdPersonIcon from 'vue-ionicons/dist/md-person.vue'

export default {
    name: "City",
    components: {
        MdPawIcon,
        MdPersonIcon
    },
    props: ["city"]
}
</script>

<style scoped>
img{
  width: 100%;
  height: auto;
  margin-bottom: 10px;
  transform: scale(1.4);
  opacity: 0.8;
  transition: transform 0.5s, opacity 0.5s;
}

img:hover{
  transform: scale(1.3);
  opacity: 1;
}

li{
  list-style: none;
  padding-bottom: 5px;
}

i{
  color: #e67e22;
  padding-right: 10px;
  font-size: 1.3em;
}

.city-photo{
  width:100%;
  margin: 0;
  margin-bottom: 15px;
  overflow: hidden;
  background-color: #000;
  margin-left: 5px;
}

.city-box{
    padding-right: 10px;
}

.icon-small{
    margin-right: 20px;
    color: #e67e22;
}
</style>