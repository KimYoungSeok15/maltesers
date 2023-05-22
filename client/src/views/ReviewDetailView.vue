<template>
  <div>
    <NavigationBar/>
    <br>
    <div class="container">
      <div class="row">
        <div class="col-1"></div>
        <div class="col-10 border">
          <br>
          <span style="font-size:30px;" class="col-4">제목 : {{ReviewTitle}}</span><p class="col-4"></p><span class="col-4" v-if="ReviewCreatedAt"> 작성자 : {{ReviewWriter}}</span>
          <hr>
          <div class="border">
            <p> 영화 제목 : {{MovieTitle}}</p>
          </div>
          <div class="border">
            <p> 장르 : {{Genre}}</p>
          </div>                    
          <div class="border">
            <p> 내용 : {{ReviewContent}}</p>
          </div>                    
          <div class="border">
            <p> 평점 : {{Rating}}</p>
          </div>                    
          <p style="font-size:15px;" v-if="ReviewUpdatedAt"> 작성일자 : {{ReviewUpdatedAt}}</p>
          <p style="font-size:15px;" v-if="ReviewCreatedAt"> 수정일자 : {{ReviewCreatedAt}}</p>
          <hr>

          <div class="row border">
            <div class="col-3"></div>
            <div class="col-2"><router-link class="btn btn-primary" to="/review">뒤로가기</router-link></div>
            <div class="col-2"><router-link class="btn btn-primary" v-if="WriterIsUser" :to="`/review/${ReviewId}/update`">수정하기</router-link></div>
            <div class="col-2"><div @click="DeleteReview" class="btn btn-primary" v-if="WriterIsUser">삭제하기</div></div>
          </div>
        </div>
      </div>
    </div>
    <div class="container mt-5">
      <h2> 댓글 리스트 </h2>
      <div class="row">
        <div class="col-1"></div>      
        <div style="font-size:1px" class="col-10">
          <div v-for="comment in Comments" :key=comment.id class="">
            <span v-if="!(comment.id in UpdatingCommentId)" style="font-size:5px" class="col-4 mx-3">내용 : {{comment.content}}</span> 
            <span v-if="!(comment.id in UpdatingCommentId)" class="col-4 mx-3" style="font-size:5px"> 작성자 : {{comment.user_name}} </span>
            <span @click="StartUpdateComment(comment.id)" class="mx-2" style="color:green">수정</span> <span style="color:red">삭제</span>
            <hr class="m-1">
          </div>  
        </div> 
      </div>
    </div> 
    <div class="container mt-5">
      <h1> 댓글 작성 </h1>
      <input type="text" v-model="CommentCreateContext">
      <button @click="CreateComment" class="btn btn-primary ml-2" value="Add">Add</button>
    </div>    
  </div>
</template>
      

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import axios from 'axios'
const ReviewURL = `http://127.0.0.1:8000/api/c1/freeboards/`
const getUsernameURL = "http://127.0.0.1:8000/accounts/user/"
const commentURL = "http://127.0.0.1:8000/api/c1/freeboards/article/comment/"
export default {
  components: {
    NavigationBar,
  },
  data(){
    return{
      ReviewId: this.$route.params.id,
      ReviewTitle: '',
      ReviewContent: '', 
      MovieTitle: '',
      Genre: '',
      Rating: '',
      ReviewCreatedAt: '', 
      ReviewUpdatedAt: '',
      ReviewWriter: '',
      User: '',
      WriterIsUser: false,
      Comments: '',
      CommentCreateContext: '',
      CommentUpdateContext: '',
      UpdatingCommentId: [],
    }
  },
  methods: {
    // 현재 리뷰 삭제
    DeleteReview() {
        axios({  
          method: 'delete',
          url: ReviewURL + this.ReviewId,
          headers:  {
            Authorization : `Token ${this.$store.state.token}`
          }
        })
        .then(() => {
            this.$router.push({ name : "review"})
        })
    },
    // 댓글 작성
    CreateComment(){
      const token = this.$store.state.token
      const freeboard_id = this.ReviewId
      const user_name = this.User
      const content = this.CommentCreateContext
      axios({  
        method: 'post',
        url: commentURL + freeboard_id + '/',
        data: {
          freeboard_id,
          user_name,
          content 
          },
        headers:  {
        Authorization : `Token ${token}`
          },
        })
      .then((response) => {
        console.log(response)
        })
      this.$router.go()
      
    },
    StartUpdateComment(comment_id){
      this.UpdatingCommentId.push(comment_id)
    },
    UpdateComment(content){
      const token = this.$store.state.token
      const freeboard_id = this.ReviewId
      const user_name = this.User
      axios({  
        method: 'post',
        url: commentURL + freeboard_id + '/',
        data: {
          freeboard_id,
          user_name,
          content 
          },
        headers:  {
        Authorization : `Token ${token}`
          },
        })
      .then((response) => {
        console.log(response)
        })
      this.$router.go()
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
    // 리뷰 내용 및 작성자 가져오기
    if (this.$store.state.token){
      axios({  
				method: 'get',
				url: ReviewURL + this.ReviewId,
        headers:  {
          Authorization : `Token ${token}`
        },
      })
      .then((response) => {
        this.ReviewTitle = response.data.title
        this.ReviewContent = response.data.content
        this.MovieTitle = response.data.Movie_title
        this.Genre = response.data.genre_name
        this.Rating = response.data.rating
        this.ReviewCreatedAt = response.data.created_at
        this.ReviewUpdatedAt = response.data.updated_at
        this.ReviewWriter = response.data.user_name
        if(this.User == this.ReviewWriter){
          this.WriterIsUser = true
        }      
      })
    }
    else {
      alert('로그인이 필요한 페이지입니다.')
      this.$router.push({ name: 'login'})
    }
    // 댓글 가져오기
    axios({  
        method: 'get',
        url: commentURL + this.ReviewId + '/',
        headers:  {
        Authorization : `Token ${token}`
      },
    })
    .then((response) => {
      this.Comments = response.data
      for (let i=0; i<this.Comments.length; i++) {
        this.UpdatingCommentId.push(response.data[i].id)   // 각 comment의 id를 배열에 담는다.
      }
    })
    .catch((err)=>{
      console.log(err)
    })

  }
}

</script>

<style>

</style>
