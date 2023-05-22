<template>
  <div>
    <NavigationBar/>
    <br>
    <div class="container">
        <div class="row">
            <h3 class="">게시글 수정</h3>
            <div class="col-1">제목 :</div>
            <input class="col-10" type="text" v-model="updatedTitle" placeholder="내용을 입력해주세요">
            <div class=""></div>    
            <br>
            <div class="col-1">영화 제목 :</div>
            <input class="col-10" type="text" v-model="movieTitle" placeholder="내용을 입력해주세요">
            <div class=""></div>    
            <br>
            <div class="col-1">장르 :</div>
            <input class="col-10" type="text" v-model="genreName" placeholder="내용을 입력해주세요">
            <div class=""></div>    
            <br>
            <div class="col-1">내용 :</div>
            <input class="col-10" style="height:500px;"  type="text" v-model="updatedContent" placeholder="내용을 입력해주세요">
            <div class=""></div>     
            <br>
            <div class="col-1">평점 :</div>
            <input class="col-1" type="number" min="1" max="10" v-model="rating" placeholder="">            
            <div class=""></div>    
            <br>                                           

            <button @click="updateReview" class="btn btn-primary col-2 mt-4" value="Add">수정하기</button>
        </div>
    </div>
  </div>
</template>

<script>
import NavigationBar from "@/components/NavigationBar.vue"
import axios from 'axios'
const UpdateURL = "http://127.0.0.1:8000/api/c1/freeboards/"
const getUsernameURL = "http://127.0.0.1:8000/accounts/user/"
const getWriternameURL = "http://127.0.0.1:8000/api/c1/freeboards/"
export default {
  data(){
    return {
      ArticleId: this.$route.params.id,
      updatedTitle: "",
      updatedContent: "",
      ReviewWriter: "",
      movieTitle:"",
      genreName:"",
      rating: 5,      
      User: "",
      WriterIsUser: false,    
      token: this.$store.state.token  
    }
  },
  components: {
    NavigationBar
  },
  created(){
        // 현재 로그인된 작성자 가져오기
    axios({ 
      method: 'get',
      url: getUsernameURL,
      headers:  {
      Authorization : `Token ${this.token}`
        },
    })
    .then((response) => {
      this.User = response.data.username
      // 현재 수정하려는 리뷰 디테일 및 작성자 가져오기
      axios({ 
        method: 'get',
        url: getWriternameURL + this.ArticleId,
        headers:  {
          Authorization : `Token ${this.token}`
        },
      })
      .then((response) => {
        this.ReviewWriter = response.data.user_name       
        if(this.ReviewWriter === this.User){
          this.WriterIsUser = true
          this.updatedTitle = response.data.title
          this.updatedContent = response.data.content
          this.movieTitle = response.data.Movie_title
          this.genreName = response.data.genre_name
          this.rating = response.data.rating
        }
      })      
    })
  },
  methods:{
    updateReview(){  // 게시물 수정 요청
      const token = this.token
      const title = this.updatedTitle
      const content = this.updatedContent
      const Movie_title = this.movieTitle
      const user_name = this.User
      const genre_name = this.genreName
      const rating = this.rating    
      if (!this.WriterIsUser){
        alert('작성자가 아닙니다!')
        this.router.push({name: "review"})
      }
      else{
        if (!title || !content || !Movie_title || !genre_name || !rating) {
          if (!title) {
          alert("제목을 입력해주세요")
          }
          else if (!content) {
          alert("내용을 입력해주세요")
          }
          else if (!Movie_title) {
          alert("영화제목을 입력해주세요")
          }
          else if (!genre_name) {
          alert("장르를 입력해주세요")
          }
          else if (!rating) {
          alert("평점을 입력해주세요")
          }                        
        }
        else {        

          axios({  
              method: 'put',
              url: UpdateURL + this.ArticleId + '/',
              data: { title, content, user_name, Movie_title, genre_name, rating },
              headers: {
              Authorization : `Token ${token}`
              },
          })
          .then((response) => {
            console.log(response)
            this.$router.push({name: "review"})
          })
        }
      }
    }
  }
}
</script>

<style>

</style>