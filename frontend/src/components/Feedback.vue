<template>
    <section class="section-feedback">
    <div class="row">
        <h2 class="col span-1-of-1">OUR CUSTOMERS CAN'T LIVE WITHOUT US</h2>
    </div>
    <div class="row">
        <div class="col span-1-of-3">
            <blockquote>
            Omnifox is just awesome! I just launched a startup which makes me really stressed a lot of the time, so Omnifox is a life-saver. Now that I got used to it, I couldn't live without my daily foxes!
            <cite><img src="../assets/customer-1.jpg" alt="">Tom Holmes</cite>
            </blockquote>
        </div>
        <div class="col span-1-of-3">
            <blockquote>
            I was looking for a quick and easy way to get the stress off my chest in Florence . I tried a lot of them and ended up with Omnifox. It's the best pet-rental in the world! Keep up the great work!

            <cite><img src="../assets/customer-2.jpg" alt="">Robert Harvey</cite>
            </blockquote>
        </div>
        <div class="col span-1-of-3">
            <blockquote>
            Inexpensive, beautiful and really lovely foxes, delivered right to my home. That's like a dream come true. We have a lot of pet-rental services in New York but no one comes even close to Omnifox!
            <cite><img src="../assets/customer-3.jpg" alt>Veronica Smith</cite>
            </blockquote>
        </div>
    </div>
    </section>
</template>

<script>
export default {
    name: "Feedback"
}
</script>

<style scoped>
.section-feedback{
  background-image: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.9)), url(../assets/2.jpg);
  background-size: cover;
  background-attachment: fixed;
  color: #fff;
}

blockquote{
  padding: 2%;
  font-style: italic;
  line-height: 145%;
  position: relative;
  margin-top: 40px;
  margin-left: 5px;
}

.section-feedback blockquote::before {
    content: "\201C";
    font-size: 500%;
    display: block;
    position: absolute;
    top: -5px;
    left: -5px;
}

cite img{
  height: 45px;
  border-radius: 50%;
  margin-right: 10px;
  vertical-align: middle;
}

cite{
  margin-top: 25px;
  display: block;
}

@media only screen and (max-width: 767px){
  .section-feedback{
    display:none;
  }
}
</style>