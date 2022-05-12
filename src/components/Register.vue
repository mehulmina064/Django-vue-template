<template>
  <div class="Register">
    <h1>{{ msg }}</h1>
    <h2>Register Page  </h2>
    <ul>
      <li><h3><a href="https://prodo.in/" target="_blank">Visit</a></h3></li>
      <br>
    </ul>
    <h2>Prodo API</h2>
    <ul>

    </ul>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data () {
    return {
      msg: 'PRODO'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-weight: normal;
}
h2 {
  font-weight: normal;
  color: rgb(196, 2, 127);
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #5bafbe;
}
</style>
