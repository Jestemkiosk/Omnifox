<template>
    <header>
      <PagedNav />
      <div class="hero-text-box">
        <h1>A complete list of all our foxes!</h1>
        <h2>Is there a happier place <span>anywhere</span> on earth?!</h2>
      </div>
    </header>
</template>

<script>
import PagedNav from "../components/PagedNav.vue";

export default {
  name: "FoxesHeader",
  components: {
    PagedNav
  }
};
</script>

<style scoped>
header{
  background-image: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)), url(../assets/2.jpg);
  background-size: cover;
  background-position: center;
  height: 60vh;
  background-attachment: fixed;
}

nav .row{
  margin: 0;
  max-width: 1920px;
}

.hero-text-box{
  margin: 10% 0 0 25%;
}

.hero-text-box h2{
  color: #fff;
  text-align: left;
  opacity: 0.8;
  margin-bottom: 0px;
}

.hero-text-box span{
  border-bottom: 2px solid #e67e22;
  display: inline-block;
}

.hero-text-box h2:after{
  background-color: transparent;
}

/* Buttons */

.btn:link,
.btn:visited,
input[type=submit]{
  display: inline-block;
  padding: 10px 30px;
  font-weight: 300;
  text-decoration: none;
  color: #fff;
  border-radius: 50px;
  border: 1px solid #d4b677;
  transition: background-color 0.3s, border 0.3s;
}

.btn-full:link,
.btn-full:visited,
input[type=submit]{
  background-color: #d4b677;
  border: 1px solid #d4b677;
  margin-right: 15px;
}

.btn:hover,
.btn:active,
input[type=submit]:hover,
input[type=submit]:active{
  background-color: #a17a33;
  border: 1px solid #a17a33;
}

.top-btn{
  position: fixed;
  left: 90%;
  bottom: 10%;
  font-size: 4.3em;
}

.top-btn a:hover{
  color: #555;
}

/* QUERIES */
/* Big tablet to 1200px : from 1024px to 1200px */
@media only screen and (max-width: 1200px) {
    .hero-text-box{
        margin: 0 0 0 5%;
        font-size: 0.8em;
    }
}

/* Small tablet to big tablet: from 768px to 1023px */
@media only screen and (max-width: 1023px){

  .hero-text-box{
    font-size: 0.8em;
  }

}

/* Phones to small tablets: from 481px to 767px */
@media only screen and (max-width: 767px){

    header{
        height: 85vh;
        
    }

    .hero-text-box{
        margin: 15% 0 0 5%;
    }

}

/* Small phones: from 0 to 480px */
@media only screen and (max-width: 480px){

  .hero-text-box{
    font-size: 0.8em;
    position: absolute;
    left: 2%;
    top: 45%;
  }

}

@media only screen and (max-height: 565px){
  .hero-text-box{
    margin-top: 0;
    margin-left: 25px;
  }
}

@media only screen and (max-height: 440px){
  .hero-text-box{
    position: absolute;
    top: 30%;
  }
}


</style>