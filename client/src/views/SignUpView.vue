<template>
  <div>
    <div style="height: 100px;"></div>    
    <img src="@/assets/hooni2.png" id="image" class="" alt="">    
    <div style="height: 50px;"></div>
    <h1 style="height: 100px;">Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      <br>
      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>
      <br>
      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2"><br>
      <br>
      <button class="btn btn-outline-light" type="submit">제출</button>
    </form>
    <button @click="GoBack" class="btn mt-3 btn-outline-light m-3">돌아가기</button>
  </div>
</template>

<script>

export default {
  data() {
    return {
      username : '',
      password1 : '',
      password2 : ''
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signUp', payload)
      
    },
    GoBack() {
      this.$router.push({ name: 'login' })
    }
    
  },
  
}
</script>


<style>
#image {
  height: 200px; 
  position:relative;
  z-index: 2; /* 다른 요소들보다 앞에 위치하여 hover 효과를 유지 */
  height: 200px; 
  position: relative;
}
#image:hover{
  transition: transform 0.3s ease; /* 변환 효과의 지속 시간과 가속도 설정 */
  transform: scale(1.2); /* 마우스를 올렸을 때 이미지 크기 확대 */
}
</style>