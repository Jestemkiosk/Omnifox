<template>
    <div class="col fox-box">
          <figure class="fox-photo">
            <img :src="fox.image_url" alt="">
          </figure>
          <h3 v-if="fox.gender === 'Male'">{{fox.name}} <MdMaleIcon /></h3>
          <h3 v-else>{{fox.name}} <MdFemaleIcon /></h3>
          <ul>
            <li v-if="fox.city"><MdBusinessIcon class='icon-small'/>Residing in {{fox.city.name}}</li>
            <li v-else><MdBusinessIcon class='icon-small'/>No home city yet!</li>
            <li><MdPawIcon class='icon-small'/>{{fox.age}} years old</li>
          </ul>
        </div>
</template>

<script>
import MdPawIcon from 'vue-ionicons/dist/md-paw.vue'
import MdBusinessIcon from 'vue-ionicons/dist/md-business.vue'
import MdMaleIcon from 'vue-ionicons/dist/md-male.vue'
import MdFemaleIcon from 'vue-ionicons/dist/md-female.vue'

export default {
    name: "Fox",
    components: {
        MdPawIcon,
        MdBusinessIcon,
        MdMaleIcon,
        MdFemaleIcon
    },
    props: ["fox"]
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

.fox-photo{
  width:100%;
  margin: 0;
  margin-bottom: 15px;
  overflow: hidden;
  background-color: #000;
  margin-left: 5px;
}

.fox-box{
    padding-right: 10px;
}

.icon-small{
    margin-right: 20px;
    color: #e67e22;
}
</style>