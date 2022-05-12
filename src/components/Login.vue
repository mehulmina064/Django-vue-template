<template>
  <div class="Login">

    <form :model="formsData">
    <label for="email"><b>Email</b></label>
    <input v-model="formsData.email" type="email" placeholder="Enter Email" name="email" required>
    <br>

    <label for="psw"><b>Password</b></label>
    <input v-model="formsData.password" type="password" placeholder="Enter Password" name="psw" required>
    <br>

    <button type="submit" @click="submitForm(formsData)">Login</button>
    <br>

    </form>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>

  <div class="container" style="background-color:#f1f1f1">
    <br>
    <button type="button" class="cancelbtn">Cancel</button>
    <br>
    <span class="psw">Forgot <a href="#">password?</a></span>
  </div>

  

  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      msg: 'Welcome to PRODO',
      formsData: {
      email: '',
      password: ''
    }
    }
  },
  methods: {
    //   submitForm() {
    //     console.log(this.formsData);
    //   }
    async submitForm() {
            const response = await this.$http.post('http://127.0.0.1:8000/api/user/', this.formsData);
            console.log(response);
            console.log("response");
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
label{
      font-weight: normal;
  color: rgb(196, 2, 127);
}
</style>
