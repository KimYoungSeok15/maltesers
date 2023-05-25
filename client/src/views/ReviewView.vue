<template>
  <div>
    <NavigationBar/>    
    <br>
    <h1 class="fw-bold">리뷰 게시판</h1>
    
    <div class="container border border-light">
      <br>
      <div class="row">
        <div class="col-1"></div>
        <router-link :to="{ name: 'reviewcreate', params: { movie_title: ' ' }}" class="btn btn-light m-3 col-2 m-2"> 리뷰 작성</router-link>
        <div class="col-1"></div>
        
      </div>
      <div class="">
          <input type="text" placeholder="영화 리뷰 키워드 입력" v-model="review_key" @keypress.enter="getReview(review_key)">
          <button @click="getReview(review_key)" class="btn btn-light m-2">검색</button>
        </div>
      <br>
      <div class="row">
        <div class="col-1"></div>
        <div v-if="articleAll" class="col-10">
          <div class="row">
            <div class="col-4 mb-3" v-for="article in articleAll" :key="article.id">
              <div class="card" style="padding: 10px; background-color:rgb(172, 177, 214);"> 
                <div class="card-body m-1" style="padding:0px; background-color:white">
                  <h5 class="card-title">{{ article.Movie_title }}</h5>
                  <p class="card-text underline-on-hover" style="cursor: pointer" @click="GoToFreeDetail(article.id)">제목: {{ article.title }}</p>
                  <p class="card-text">장르: {{ article.genre_name }}</p>
                  <p class="card-text">평점: {{ article.rating }}</p>
                  <div class="card-footer text-end border-white ">
                    <p class="card-text" style="display: flex; justify-content: center;">
                      <button @click="GoToFreeDetail(article.id)" class="btn mx-auto btn-light">리뷰 보기</button>
                    </p>
                    <p style="display: flex; justify-content: center;">
                      <span @click="GoToProfile(article.user_name)" style="cursor:pointer" class="underline-on-hover">작성자: {{ article.user_name }}</span>
                    </p>
                    <p class="card-text m-0 px-3">
                      생성시간: {{ article.created_at.slice(0, 10) }} {{ article.created_at.slice(11, 19) }}
                    </p>
                  </div>
                </div>
              </div>
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
      review_key: '',
      reviewSearchURL: ''
		}
	},
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  watch: {
    review_key(newVal) {
      if (newVal === '') {
        this.getAllreview(); // 변경 감지 시 호출할 메소드
      }
    },
  },
  // 전체 게시글을 Django DB에서 받아와서 Store에 저장
  
  methods: {
    getAllreview() {
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
    GoToFreeDetail(data){
      this.$router.push({name:'ReviewDetail', params: {id: data}})
      
      // this.$router.go()
    },
    GoToProfile(data){
      this.$router.push({name:'profile', params: {username: data}})
    
    },

    getReview(review_key) {
      if (review_key=='') { 
        this.reviewSearchURL = `http://127.0.0.1:8000/api/c1/freeboards`
      } else {
        this.reviewSearchURL = `http://127.0.0.1:8000/api/c1/freeboards/${review_key}/`
      }
      axios({
            methods: 'get',
            url: this.reviewSearchURL,
            headers:  {
              Authorization : `Token ${this.$store.state.token}`
            },
          })
          .then((res) => {
            console.log(res)
            this.articleAll = res.data
          })
    }
  },
  created() {
    this.getAllreview()
  },
}
</script>

<style scoped>
div {
  color: black;
}
  .underline-on-hover {
    text-decoration: none;
    font-weight: normal;
    font-size: 19px; /* 초기 글자 크기 */

  }

  .underline-on-hover:hover {
    text-decoration: underline;
    font-weight: bold;
    font-size: 19px; /* 마우스를 올렸을 때 큰 글자 크기 */
    transform: scale(1.1);
  }
  input {
  border-radius: 10px;
  } 
</style>