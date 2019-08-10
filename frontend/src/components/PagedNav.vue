<template>
    <nav class="sticky clearfix">
          <div class="logo">
            <a href="/"><img src="../assets/lisek.png" alt="" class="logo">
              <h4>OMNIFOX</h4></a>
          </div>
          <ul class="main-nav">
            <li><a href="/">Home</a></li>
            <li><a href="/foxes">Our Foxes</a></li>
            <li><a href="/cities">Our cities</a></li>
          </ul>
    </nav>
</template>

<script>
export default {
    name: "PagedNav"
}
</script>

<style scoped>
nav .row{
  margin: 0;
  max-width: 1920px;
}

.logo{
  width: auto;
  float: left;
  opacity: 0.65;
  position: absolute;
}

.logo h4{
  margin-left: 40.5px;
  color: #fff;
  position: absolute;
  margin-top: 125px;
  font-size: 1.5em;
  padding-right: 100px;
  text-align: right;
  display: inline-block;
}

.logo img{
  height: 175px;
  transition: opacity 0.3s;
}

.logo:hover,
.logo:active{
  opacity: 0.8;
}

/* Main nav */
.main-nav{
  float: right;
  list-style: none;
  margin: 25px 15px 0px 0px;
  opacity: 0.7;
  padding: 10px 0 10px 0;
  transition: opacity 1s;
}

.main-nav a{
  padding: 10px;
}

.main-nav li{
  padding-bottom: 5px;
}

.main-nav:hover,
.main-nav:active{
  opacity: 1;
}

.main-nav li{
  display: inline-block;
  margin-left: 40px;
}

.main-nav li a:link,
.main-nav li a:visited{
  padding: 8px;
  color: #fff;
  text-decoration: none;
  text-transform: uppercase;
  font-size: 0.9em;
  border-bottom: 2px solid transparent;
  transition: border-bottom 0.3s;
  margin-left: 0;

}

.main-nav li a:hover,
.main-nav li a:active{
  border-bottom: 2px solid #db8829;
}

/* Sticky NAV */
.sticky{
  position: sticky;
  top: 0;
  left: 0;
  width: 100%;
  background-color: rgba(255,255,255,0.93);
  box-shadow: 0 1px 1px;
}

.sticky .main-nav li a:link,
.sticky .main-nav li a:visited{
  padding: 8px 0;
  color: #222;
}

.sticky .logo img{
  height: 75px;
  opacity: 0.9;
  width: 75px;
}

.sticky .logo h4{
  margin-top: 17.5px;
  margin-left: 70px;
  color: #222;
}

/* BUTTONS */
.top-btn{
  position: fixed;
  left: 90%;
  bottom: 5%;
  font-size: 5em;
}

.top-btn a:hover{
  color: #555;
}

@media only screen and (max-width: 1200px) {
    .main-nav li{
      display: block;
      margin-top: 20px;
    }

    .foxes-showcase li{
      width:50%;
    }

    .main-nav a:link,
    .main-nav a:visited{
      padding-right: 20px;
      margin-right: 0;
    }

    .sticky .main-nav{
      padding-right: 0;
      padding-left: 5px;
      padding: 0 25px 15px 0;
    }

    .sticky{
      box-shadow: 0 0 0;
      background-color: transparent;
      position: static;
    }

    .sticky .main-nav li a:link,
    .sticky .main-nav li a:visited{
      color: #fff;
      opacity:1;
    }

    .sticky .logo h4{
      color: #fff;
      opacity:1;
    }
}

/* Small tablet to big tablet: from 768px to 1023px */
@media only screen and (max-width: 1023px){

  .sticky{
    position: static;
  }

  .main-nav a:link,
  .main-nav a:visited{
    padding-right: 20px;
    margin-right: 0;
  }

  .main-nav{
    padding-right: 0;
    padding-left: 5px;
    font-size: 0.8em;
  }

  .top-btn a:hover{
    color: #e67e22;
  }

}


/* Phones to small tablets: from 481px to 767px */
@media only screen and (max-width: 767px){

  .main-nav a:link,
  .main-nav a:visited{
    padding-right: 20px;
    margin-right: 0;
  }

  .main-nav{
    padding-right: 0;
    padding-left: 5px;
  }

  .logo img{
    height: 125px;
  }

  .logo h4{
    margin-top: 95px;
    margin-left: 30px;
    font-size: 0.8em;
  }

  .top-btn{
    font-size: 4em;
  }

  .sticky{
    position: static;
  }
}

/* Small phones: from 0 to 480px */
@media only screen and (max-width: 480px){

  .top-btn{
    font-size: 2.5em;
  }

  .main-nav a:link,
  .main-nav a:visited{
    padding-right: 20px;
    margin-right: 0;
  }

  .main-nav{
    padding-right: 0;
    padding-left: 5px;
  }

  .logo img{
    height:100px;
  }

  .logo h4{
    margin-left: 20px;
    margin-top: 75px;
    font-size: 0.66em;
  }

}

</style>