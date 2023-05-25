<template>
  <div>
    <NavigationBar/>
    <br>
    <div class="container">
        <div class="row">
            <h3 class="">게시글 수정</h3>
            <div class="col-1">제목 :</div>
            <input class="col-4 text-white" type="text" v-model="updatedTitle" placeholder="내용을 입력해주세요" style="background-color: transparent;">
            <div class=""></div>    
            <br>
            <div class="col-1 text-white">영화 제목 :</div>
            <input class="col-4 text-white" type="text" v-model="movieTitle" placeholder="내용을 입력해주세요" style="background-color: transparent;">   
            <div class="col-7">
              <div class="input-group col-3" style="width: 30%;  opacity: 0.5;">
              <label class="input-group-text" for="inputGroupSelect01" >장르</label>
                <select class="form-select" id="inputGroupSelect01" v-model="genreName" >
                <!-- <option selected >Choose...</option> -->
                <option value="모험">모험</option>
                <option value="판타지">판타지</option>
                <option value="애니메이션">애니메이션</option>
                <option value="드라마">드라마</option>
                <option value="공포">공포</option>
                <option value="액션">액션</option>
                <option value="코미디">코미디</option>
                <option value="역사">역사</option>
                <option value="서부">서부</option>
                <option value="스릴러">스릴러</option>
                <option value="범죄">범죄</option>
                <option value="다큐멘터리">다큐멘터리</option>
                <option value="SF">SF</option>
                <option value="미스터리">미스터리</option>
                <option value="음악">음악</option>
                <option value="로맨스">로맨스</option>
                <option value="가족">가족</option>
                <option value="전쟁">전쟁</option>
                <option value="TV 영화">TV 영화</option>
                </select>
              </div>
            </div>
            <div class=""></div>
            <br>
            <div class="col-1">평점 :</div>
            <input class="col-1 text-white" type="number" min="1" max="10" v-model="rating" placeholder="" style="background-color: transparent;">            
            <div class=""></div>    
            <br>

            <div class="col-1">내용 :</div>
            <input class="col-10 text-white" style="padding-bottom: 300px; background-color: transparent;"  type="text" v-model="updatedContent" placeholder="내용을 입력해주세요">
            <div class=""></div>     
                                                   

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