<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'normalize.css'
import 'vue-ionicons/ionicons.css'

export default {
  name:"App",
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Lato:100,300,300i,400&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-weight: 300;
  font-family: 'Lato', 'Arial', sans-serif;
}

html, body{
  min-width: 1140;
}

html {
  background-color: #fff;
  color: #555 !important;
  font-size: 20px !important;
  text-rendering: optimizeLegibility;

}

.clearfix {zoom: 1}
.clearfix:after {
  content: '.';
  clear: both;
  display: block;
  height: 0;
  visibility: hidden;
}

.row {
  max-width: 1140px;
  margin: 0 auto;
}

section{
  padding: 80px 0;
}

.box{
  padding: 1%;
}


/* --------- HEADINGS --------- */

h1,
h2,
h3{
  font-weight: 300;
  text-transform: uppercase;
}

h1{
  margin-top: 0;
  margin-bottom: 10px;
  color: #fff;
  font-size: 2.4em;
  word-spacing: 4px;
  letter-spacing: 1px;
}

h2{
  font-size: 1.8em;
  word-spacing: 2px;
  text-align: center;
  margin-bottom: 30px;
  letter-spacing: 1px;
}

h3{
  font-size: 1.1em;
  margin-bottom: 15px;
  font-weight: 400;
}

h2:after{
  display: block;
  height: 2px;
  background-color: #e67e22;
  content: "";
  width:250px;
  margin: 0 auto;
  margin-top: 30px;
}

/* --------- PARAGRAPHS --------- */
.long-copy{
  line-height: 1.45em;
  width: 80%;
  margin-left: 10%;
}

.box p{
  font-size: 0.9em;
  line-height: 145%;
  margin-bottom: 0;
}

/* --------- BUTTONS --------- */

.btn:link,
.btn:visited,
input[type=submit]{
  display: inline-block;
  padding: 10px 30px;
  font-weight: 300;
  text-decoration: none;
  color: #fff;
  border-radius: 50px;
  border: 1px solid #e67e22;
  transition: background-color 0.3s, border 0.3s;
}

.btn-full:link,
.btn-full:visited,
input[type=submit]{
  background-color: #e67e22;
  border: 1px solid #e67e22;
  margin-right: 15px;
}

.btn:hover,
.btn:active,
input[type=submit]:hover,
input[type=submit]:active{
  background-color: #cf6d17;
  border: 1px solid #cf6d17;
}


/* Small tablet to big tablet: from 768px to 1023px */
@media only screen and (max-width: 1023px){
  h2{
    font-size: 1.5em;
  }
  
  .btn:link,
  .btm:visited{
    padding: 6px;
  }

  section{
      padding: 30px 0;
  }
}

/* Phones to small tablets: from 481px to 767px */
@media only screen and (max-width: 767px){
    body{
    font-size: 18px;
  }
}

/* Small phones: from 0 to 480px */
@media only screen and (max-width: 480px){

  .btn:link,
  .btm:visited{
    font-size: 0.9em;
  }

  h3{
    display: inline-block;
  }

}

@media only screen and (max-height: 565px){
  h1{
    font-size: 2em;
  }
  h2{
    font-size: 1.2em;
  }
}

@media only screen and (max-height: 440px){
  h1{
    font-size: 1.7em;
  }
}
</style>
