<template>
  <div style="height:1000px;" class="backdropcontainer">
    <div style="height: 100px;"></div>    
    <img @click="GoMain" src="@/assets/hooni3.png" style="cursor: pointer;" id="image" class="" alt="">   
    <div id="logincan" class="border col-4 offset-4">     
    <div style="height: 50px;"></div>
    <h1 style="height: 100px;">회원 가입</h1>
    <form @submit.prevent="signUp">
      <label for="username" class="me-4">사용자이름 :</label>
      <input type="text" id="username" v-model="username"><br>
      <br>
      <label for="password1" class="me-4 ms-3"> 비밀번호 : </label>
      <input type="password" id="password1" v-model="password1"><br>
      <br>
      <label for="password2" class="me-2"> 비밀번호 확인 : </label>
      <input type="password" id="password2" v-model="password2"><br>
      <br>
      <button class="btn btn-outline-dark" type="submit">제출</button>
    </form>
    <button @click="GoBack" class="btn mt-3 btn-outline-dark m-3">돌아가기</button>
    </div>
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
      if (password1 !== password2){
        alert('비밀번호가 서로 다릅니다!')
      } else {
      this.$store.dispatch('signUp', payload)
      }
    },
    GoBack() {
      this.$router.push({ name: 'login' })
    },
    GoMain() {
      this.$router.push({name:'intro'})
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
#logincan {
  background-color: rgb(208, 222, 222);
  opacity: 0.8;
  border-radius: 30px;
}
</style>