<template>
  <div>
    <NavigationBar/>
    <br>
    <div class="container">
      <div class="row">
        <div class="col-1"></div>
        <div class="col-10 border">
          <br>
          <span class="col-4">제목 : {{ArticleTitle}}</span><p class="col-4"></p><span class="col-4" v-if="ArticleCreatedAt"> 작성자 : {{ArticleWriter}}</span>
          <hr>
          <p v-if="ArticleUpdatedAt"> 작성일자 : {{ArticleUpdatedAt}}</p>
          <p v-if="ArticleCreatedAt"> 수정일자 : {{ArticleCreatedAt}}</p>
          <hr>
          <p>내용 : {{ArticleContent}}</p>
          <hr>
          <hr>
           <hr>
          <router-link to="/community">뒤로가기</router-link> <br>
          <router-link v-if="WriterIsUser" :to="`/community/${ArticleId}/update`">수정하기</router-link><br>
          <router-link v-if="WriterIsUser" to="/community">삭제하기</router-link>
        </div>
      </div>
    </div>
  </div>
</template>
      

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import axios from 'axios'
const URL = `http://127.0.0.1:8000/api/c1/freeboards/`
const getUsernameURL = "http://127.0.0.1:8000/accounts/user/"
export default {
  components: {
    NavigationBar,
  },
  data(){
    return{
      ArticleId: this.$route.params.id,
      ArticleTitle: '',
      ArticleContent: '', 
      ArticleCreatedAt: '', 
      ArticleUpdatedAt: '',
      ArticleWriter: '',
      User: '',
      WriterIsUser: false,
    }
  },
  created() {
    const token = this.$store.state.token
    // 현재 유저 이름 가져오기
    axios({  
        method: 'get',
        url: getUsernameURL,
        headers:  {
        Authorization : `Token ${token}`
        },
    })
    .then((response) => {
      this.User = response.data.username
    })
    // 게시물 작성자 이름 가져오기
    if (this.$store.state.token){
      axios({  
				methods: 'get',
				url: URL + this.ArticleId,
        headers:  {
          Authorization : `Token ${token}`
        },
      })
      .then((response) => {
        this.ArticleTitle = response.data.title
        this.ArticleContent = response.data.content
        this.ArticleCreatedAt = response.data.created_at
        this.ArticleUpdatedAt = response.data.updated_at
        this.ArticleWriter = response.data.user_name
        if(this.User == this.ArticleWriter){
          this.WriterIsUser = true
        }      
      })
    }
    else {
      alert('로그인이 필요한 페이지입니다.')
      this.$router.push({ name: 'login'})
    }

  }
}
</script>

<style>

</style>
