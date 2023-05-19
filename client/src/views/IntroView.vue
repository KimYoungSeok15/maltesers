<template>
  <div class="">
    <div id="bk_grnd_img" class="">
      <router-link class="btn btn-outline-light px-3 m-4" style="position:absolute; right:0%;" to="../login">로그인</router-link> 
      <div class="" style="position:absolute; top:400px; left:600px"> 
      <h1 style="color:white; ">좋아하는 영화를 마음껏 검색해보세요!</h1>
      <br>
      <router-link class="btn btn-outline-light px-3" to="../signup">회원가입</router-link> 
      </div>
    </div>      
  </div>
</template>

<script>
export default {
}
</script>

<style>
  #bk_grnd_img {
    background:url("@/assets/lalaland21.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center center;
    width: 100%;
    height: 1000px;
    position: relative;
}
</style>