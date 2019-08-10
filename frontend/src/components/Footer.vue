<template>
    <footer>
        <div class="row">
          <div class="col span-1-of-2">
            <ul class="footer-nav">
              <li><a href="/">Home</a></li>
              <li><a href="/foxes">Our Foxes</a></li>
              <li><a href="/cities">Our Cities</a></li>
              <li><a href="/resume.pdf">My Resume</a></li>
              <li><a href="#">API endpoint</a></li>
            </ul>
          </div>
          <div class="col span-1-of-2">
            <ul class="social-nav">
              <li><a href="/resume.pdf"><MdBriefcaseIcon class="ion-resume" title="My Resume"/></a></li>
              <li><a href="#"><LogoGithubIcon class="ion-social-github" title="This project's Github Repository"/></a></li>
              <li><a href="https://www.fiverr.com/jestemkioskiem"><MdFolderOpenIcon class="ion-social-fiverr" title="My Fiverr Freelancer Profile"/></a></li>
            </ul>
          </div>
        </div>

        <div class="row">
            <div class="footer-copyright col span-1-of-1">
                <p>Copyright &copy; 2019 by <span>Wiktor Metryka</span>. All rights reserved.
                <br>Front End: <span>VueJS, <span class="smaller">Bootstrap CSS, Normalize CSS</span></span>
                <br>Back End:<span>Python Flask <span class="smaller">REST API</span></span></p>
            </div>
        </div>
    </footer>
</template>

<script>

import LogoGithubIcon from 'vue-ionicons/dist/logo-github.vue'
import MdBriefcaseIcon from 'vue-ionicons/dist/md-briefcase.vue'
import MdFolderOpenIcon from 'vue-ionicons/dist/md-folder-open.vue'

export default {
    name: "Footer",
    components:{
        MdBriefcaseIcon,
        LogoGithubIcon,
        MdFolderOpenIcon
    }
}
</script>

<style scoped>

footer{
  background-color: #202020;
  padding-bottom: 30px;
  padding-top: 10px;
  font-size: 0.8em;
}

a{
    color: #e67e22;
}

.smaller{
    font-size: 0.75em;
}

.footer-copyright p{
    margin: 0;
}

.footer-nav{
  list-style: none;
  float: left;
}

.social-nav{
  list-style: none;
  float: right;
}

.footer-nav li,
.social-nav li{
  display: inline-block;
  margin-right: 20px;
}

.footer-nav li:last-child,
.social-nav li:last-child{
  margin-right: 0;
}

.footer-nav a:link,
.footer-nav a:visited{
  border: 0;
  text-decoration: none;
}

.footer-nav a:hover,
.footer-nav a:active{
  color: #fff;
  text-decoration: none;
  transition: color 0.2s, text-decoration 0.2s;
}

footer p{
  color: #888;
  margin-top: 10px;
  text-align: center;
  font-size: 0.8em;
}

.social-nav li a:link,
.social-nav li a:visited{
  font-size: 1.3em;
  color: #d2d2d2;
}

.ion-social-github,
.ion-resume,
.ion-social-fiverr{
  transition: color 0.2s;
}

.ion-resume:hover,
.ion-resume:active{
  color: #55acee;
}

.ion-social-fiverr:hover,
.ion-social-fiverr:active{
  color: #00b22d;
}

.ion-social-github:hover,
.ion-social-github:active{
  color: #9cdaf1;
}

footer span{
  color: #fff;
}

.footer-nav li:first-child{
  margin-left: 10px;
}

.social-nav li:last-child{
  margin-right: 15px;
}

/* Small phones: from 0 to 480px */
@media only screen and (max-width: 480px){
    footer{
      font-size: 0.7em;
      text-align: center;
    }

    footer li{
      margin:0;
    }

    footer p{
      font-size: 0.6em;
    }
}

</style>