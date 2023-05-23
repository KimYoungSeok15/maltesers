<template>
  <div style="">
    <NavigationBar/>    
    <br>
    <h1 class="fw-bold">리뷰 게시판</h1>
    
    <div class="container border">
      <br>
      <div class="row">
        <div class="col-1"></div>
        <router-link to="/reviewcreate" class="btn btn-primary col-2 m-2"> 리뷰 작성</router-link>
      </div>
      <br>
      <div class="row">
        <div class="col-1"></div>
          <div v-if="articleAll" class="col-10">
            <div class="m-0 rounded" v-for="article in articleAll" :key="article.id" style="border: solid 1px;">
              <div>
                <span @click="GoToFreeDetail(article.id)" class="underline-on-hover col-5 mx-5">영화제목 : {{ article.Movie_title }} </span>
              </div>
              <div>
                <span @click="GoToFreeDetail(article.id)" class="underline-on-hover col-5 mx-5">제목 : {{ article.title }} </span>
              </div>                
              <div>
                <span @click="GoToFreeDetail(article.id)" class="underline-on-hover col-5 mx-5">장르 : {{ article.genre_name }} </span>
              </div>
              <div>
                <span @click="GoToFreeDetail(article.id)" class="underline-on-hover col-5 mx-5">평점 : {{ article.rating }} </span>
              </div>
              <div>
                <span class="text-end underline-on-hover" @click="GoToProfile(article.user_name)" >작성자 : {{ article.user_name }}</span>
                <p class="text-end m-0 px-3">생성시간 : {{ article.created_at.slice(0, 10) }} {{ article.created_at.slice(11, 19) }}</p> 
              </div>
            </div>
          </div>
        </div>
      <br>
    </div>
    <br><br><br><br><br><br><br><br><br><br>
  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import axios from 'axios'

export default {
  name: 'ReviewView',
  components: {
    NavigationBar,
  },
  data() {
    return {
			articleAll: '',
		}
	},
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  // 전체 게시글을 Django DB에서 받아와서 Store에 저장
  created() {
    
    const djangoCommunity = 'http://127.0.0.1:8000/api/c1/freeboards'
      this.isLogin
      if (this.isLogin) {
        this.$store.dispatch('getfreeArticles')
        axios({
            methods: 'get',
            url: djangoCommunity,
            headers:  {
              Authorization : `Token ${this.$store.state.token}`
            },
        })
        .then((response) => {
          this.articleAll = response.data
        })   
        .catch(() => {
          this.articleAll = ''
        })     
      } else {
        alert('로그인이 필요한 서비스 입니다')
        this.$router.push({ name: 'login'})
      }
  },
  methods: {
    GoToFreeDetail(data){
      this.$router.push({name:'ReviewDetail', params: {id: data}})
      
      // this.$router.go()
    },
    GoToProfile(data){
      this.$router.push({name:'profile', params: {username: data}})
    
    },
  }
}
</script>

<style>
  .underline-on-hover {
    text-decoration: none;
    font-weight: normal;
    font-size: 19px; /* 초기 글자 크기 */
  }

  .underline-on-hover:hover {
    text-decoration: underline;
    font-weight: bold;
    font-size: 19px; /* 마우스를 올렸을 때 큰 글자 크기 */
  }
</style>