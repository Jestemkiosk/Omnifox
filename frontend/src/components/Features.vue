<template>
    <section class="section-features">
        <div class="row">
            <h2 class="col span-1-of-1 box">“A fox is a wolf who sends flowers. ”</h2>
        </div>
        <div class="row">
            <p class="col span-1-of-1 box long-copy">Hello, we are Omnifox, your new premium fox delivery service. We know you're always busy. We'll bring you a fox every day to take the stress off of you! You'll love them just like we do!</p>
        </div>
        <div class="row info">
            <div class="col span-1-of-4 box">
                <h3>100% fox friendly</h3>
                <p>We only bring you already domesticated foxes, we don't take freedom away from the wild ones. 10% of your revenue goes to a fundation trying to prevent violent fox domestication. Let's fight fire with fire!</p>
            </div>
            <div class="col span-1-of-4 box">
                <h3>Ready in 20 minutes</h3>
                <p>You're only twenty minutes away from your cute and lovely fox delivered to your home. We work with the best tamers in each town to ensure that you and the fox are 100% happy.</p>
            </div>
            <div class="col span-1-of-4 box">
                <h3>365 days/year</h3>
                <p>Throw your worries away forever! Our subscription plans include up to 365 days/year coverage. You can also order more flexibly if that's your style. Our goal is to make sure you can always pet a furry friend.</p>
            </div>
            <div class="col span-1-of-4 box">
                <h3>Adopt a fox!</h3>
                <p>After you've shown us you can care for a fox, you can sign up for an adoption program and get a fox just for yourself! You can then use our service to order food and general supplies. Isn't that awesome?!</p>
            </div>
        </div>
    </section>
</template>

<script>

export default {
    name: "Features"
}
</script>

<style scoped>
.long-copy {
  margin-bottom: 40px;
  letter-spacing: 1.15px;
  font-size: 1.05em;
  text-align: center;
  
}

@media only screen and (max-width: 767px){
    .info{
        display: none;
    }
}


</style>