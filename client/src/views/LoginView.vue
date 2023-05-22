<template>
  <div>
    <div style="height: 100px;"></div>     
    <img src="@/assets/hooni2.png" style="height: 200px; position:relative;" class="" alt="">
    <div style="height: 50px;"></div>    
    <h1 style="height: 70px;">LogIn Page</h1>
    <form @submit.prevent="LogIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      <br>
      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password"><br>
      <br>
      <input class="mb-3" type="submit" value="LogIn">
    </form>
    <span class="mx-1">아직 회원이 아니신가요?</span>
    <router-link class="mx-1" to="../signup">가입하기</router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username : '',
      password : '',
    }
  },
  methods: {
    LogIn() {
      const username = this.username
      const password = this.password
      const payload = {
        username, password
      }
      this.$store.dispatch('LogIn', payload)
    }
  }
}
</script>

<style>

</style>