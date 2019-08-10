<template>
    <section class="section-steps js--section-steps">
      <div class="row">
        <h2 class="col span-1-of-1 box">How it works &mdash; Simple as 1, 2, 3</h2>
      </div>
      <div class="row">
        <div class="col span-1-of-2 steps-box">
          <img src="../assets/app-iPhone.png" alt="" class="app-screen">
        </div>
        <div class="col span-1-of-2 steps-box">
          <div class="works-step">
            <div class="">1</div>
            <p>Choose the subscription plan that best fits your needs and sign up today.</p>
          </div>
          <div class="works-step">
            <div class="">2</div>
            <p>Order your favourite fox using our mobile app or website. Or you can even call us!</p>
          </div>
          <div class="works-step">
            <div class="">3</div>
            <p>Enjoy your fox in about 20 minutes. Play with him and let him bring you joy!</p>
          </div>

          <a href="https://www.apple.com/pl/itunes/charts/free-apps/" class="btn-app" target="_blank"><img src="../assets/download-app.svg" alt=""></a>
          <a href="https://play.google.com/store?hl=pl" class="btn-app" target="_blank"><img src="../assets/download-app-android.png" alt=""></a>
        </div>
      </div>
    </section>
</template>

<script>
export default {
    name: "Steps"
}
</script>

<style scoped>

.row h2{
    text-align: center;
}

.section-steps {
  background-color: #f4f4f4;
}

.steps-box:first-child{
  text-align: right;
  padding-right: 3%;
  margin-top: 30px;
}

.steps-box:last-child{
  padding-left: 3%;
  margin-top: 75px;
}

.app-screen {
  width: 50%;
}

.works-step{
  margin-bottom: 50px;
}

.works-step:last-of-type{
  margin-bottom: 60px;
}

.works-step div{
  color: #e67e22;
  border: 2px solid #e67e22;
  display: inline-block;
  border-radius: 50%;
  height: 55px;
  width: 55px;
  text-align: center;
  font-size: 1.6em;
  padding: 5px;
  float: left;
  margin-right: 10px;
}

.btn-app img{
  height: 50px;
  width: auto;
  margin-right: 10px;
}

@media only screen and (max-widht: 767px){
    .section-steps{
        margin-bottom: 0px;
    }
}

@media only screen and (max-width: 480px){
    .section-steps img{
        text-align: left;
        margin-right: 80px;
    }

    .works-step div{
        font-size: 1.3em;
        height: 40px;
        width: 40px;
    }

    .btn-app img{
        height: 38px;
        margin-right: 0px;
        margin-left: 0px;
    }

    .section-steps h2{
        font-size: 1.9em;
    }

    .btn-app img:first-child{
        margin-left: 50px;
    }

}
</style>