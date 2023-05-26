<template>
  <div style="height:1000px;" class="backdropcontainer">
    <div style="height: 100px;"></div>     
    <img @click="GoMain" src="@/assets/hooni3.png" style="cursor: pointer;" id="image" alt="">
    <div id="logincan" class="border col-4 offset-4">
      <div style="height: 30px;"></div>    
        <h1 style="height: 70px;">LogIn Page</h1>
        <form @submit.prevent="LogIn">
          <label for="username">username : </label>
          <input type="text" id="username" v-model="username"><br>
          <br>
          <label for="password1"> password : </label>
          <input type="password" id="password1" v-model="password"><br>
          <br>
          <button class="mb-3 btn btn-outline-dark m-3" type="submit">LogIn</button>
        </form>
        <span class="mx-1">아직 회원이 아니신가요?</span>
        <router-link class="mx-1" to="../signup">가입하기</router-link>
        <br>
        <br>
      </div>
      <br>
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
    },
    GoMain() {
      this.$router.push({name:'intro'})
    }
  }
}
</script>

<style>
#image {
  z-index: 2; /* 다른 요소들보다 앞에 위치하여 hover 효과를 유지 */
  height: 200px; 
  position: relative;
}
#image:hover{
  transition: transform 0.3s ease; /* 변환 효과의 지속 시간과 가속도 설정 */
  transform: scale(1.2); /* 마우스를 올렸을 때 이미지 크기 확대 */
}
.backdropcontainer {
  background:url("@/assets/eternal12.jpg");
  opacity: 0.9;
}
#logincan {
  background-color: rgb(208, 222, 222);
  opacity: 0.8;
  border-radius: 30px;
}
</style>