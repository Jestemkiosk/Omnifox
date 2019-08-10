<template>
    <section class="section-foxes">
        <ul class="foxes-showcase clearfix">
            <li>
                <figure class="fox-photo">
                    <img src="../assets/1.jpg" alt="Barny">
                </figure>
            </li>
            <li>
                <figure class="fox-photo">
                    <img src="../assets/2.jpg" alt="Alexandra">
                </figure>
            </li>
            <li>
                <figure class="fox-photo">
                    <img src="../assets/3.jpg" alt="Alexandra">
                </figure>
            </li>
            <li>
                <figure class="fox-photo">
                    <img src="../assets/4.jpg" alt="Alexandra">
                </figure>
            </li>
        </ul>
        <ul class="foxes-showcase second-showcase clearfix">
            <li>
                <figure class="fox-photo">
                    <img src="../assets/5.jpg" alt="Lisa">
                </figure>
            </li>
            <li>
                <figure class="fox-photo">
                    <img src="../assets/6.jpg" alt="Tom">
                </figure>
            </li>
            <li>
                <figure class="fox-photo">
                    <img src="../assets/7.jpg" alt="Tom">
                </figure>
            </li>
            <li>
                <figure class="fox-photo">
                    <img src="../assets/8.jpg" alt="Apoc">
                </figure>
            </li>
        </ul>
        <div class="row">
            <h4 class="all-foxes col span-1-of-1">Check out all of our foxes <a href="/foxes">here.</a></h4>
        </div>
    </section>
</template>

<script>
export default {
    name: "Collage"
}
</script>

<style scoped>

.section-foxes{
    padding: 0;
    background-color: #fff;
}

a{
    font-weight: 500;
    color: #e67e22;
    text-decoration: underline;
}

h4{
    text-align: center;
    margin-top: 20px;
}

h4:after{
  display: block;
  height: 2px;
  background-color: #e67e22;
  content: "";
  width:125px;
  margin: 0 auto;
  margin-top: 10px;
}

.foxes-showcase {
    list-style: none;
    width: 100%;
    margin-bottom: 0;
}

.foxes-showcase li {
    display: block;
    float: left;
    width: 25%;
}

.fox-photo {
    width: 100%;
    margin: 0;
    overflow: hidden;
    background-color: #000;
}

.fox-photo img {

    opacity: 0.7;
    width: 100%;
    height: auto;
    -webkit-transform: scale(1.15);
    -ms-transform: scale(1.15);
    transform: scale(1.15);
    -webkit-transition: -webkit-transform 0.5s, opacity 0.5s;
    transition: transform 0.5s, opacity 0.5s;
}

.fox-photo img:hover {
    opacity: 1;
    -webkit-transform: scale(1.03);
    -ms-transform: scale(1.03);
    transform: scale(1.03);
}


/* Big tablet to 1200px : from 1024px to 1200px */
@media only screen and (max-width: 1200px) {
    .foxes-showcase li{
        width:50%;
    }
    .second-showcase{
        display: none;
    }
    h4{
        font-size: 1em;
    }
}

</style>