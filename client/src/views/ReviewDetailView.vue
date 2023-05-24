<template>
  <div class="h-100%">
    <NavigationBar/>
    <br>
    <div class="container">
      <div class="row">
        <div class="col-1"></div>
        <div class="col-10 border">
          <br>
          <span style="font-size:30px;" class="col-4">제목 : {{ReviewTitle}}</span><p class="col-4"></p><span class="col-4" v-if="ReviewCreatedAt"> 작성자 : {{ReviewWriter}}</span>
          <hr>
          <p class="d-flex justify-content-end mx-3 px-3" style="font-size:15px;" v-if="ReviewUpdatedAt"> 작성일자 : {{ReviewUpdatedAt}}</p>
          <p class="d-flex justify-content-end mx-3 px-3" style="font-size:15px;" v-if="ReviewCreatedAt"> 수정일자 : {{ReviewCreatedAt}}</p>
          <div class="d-flex justify-content-end border-top mx-3 px-3">
            <p class="m-0">영화 제목: {{ MovieTitle }}</p>
          </div>
          <div class="d-flex justify-content-end mx-3 px-3">
            <p> 장르 : {{Genre}}</p>
          </div>     
          <div class="d-flex justify-content-end mx-3 px-3">
            <p> 평점 : {{Rating}}</p>
          </div>                
          <div class="" style="height:200px">
            <br>
            <p>{{ReviewContent}}</p>
          </div>                   
          <hr>

          <div class="row">
            <div class="col-3"></div>
            <div class="col-2"><router-link class="btn btn-outline-light" to="/review">뒤로가기</router-link></div>
            <div class="col-2"><router-link class="btn btn-outline-light" v-if="WriterIsUser" :to="`/review/${ReviewId}/update`">수정하기</router-link></div>
            <div class="col-2"><div @click="DeleteReview" class="btn btn-outline-light" v-if="WriterIsUser">삭제하기</div></div>
          </div>
          <br>
        </div>
      </div>
    </div>
    <div class="container mt-5">
      <p> 댓글 리스트 </p>
      <div class="row">
        <div class="col-1"></div>      
        <div v-if="Comments" style="font-size:1px" class="col-10">
          <div v-for="comment in Comments" :key=comment.id class="">
            <span v-if="!(UpdatingCommentId.includes(comment.id))" style="font-size:15px" class="col-4 mx-3">내용 : {{comment.content}}</span> 
            <input v-if="UpdatingCommentId.includes(comment.id)" @keyup.enter="UpdateComment(comment.id, comment.content)" v-model="comment.content" style="font-size:5px" class="col-4 mx-3">
            <span v-if="!(UpdatingCommentId.includes(comment.id))" class="col-4 mx-3" style="font-size:15px"> 작성자 : {{comment.user_name}} </span>
            <span v-if="comment.user_name === User" @click="StartUpdateComment(comment.id, comment.content)" class="mx-2" style="color:green">수정</span> 
            <span v-if="comment.user_name === User" @click="DeleteComment(comment.id)" style="color:red">삭제</span>
            <hr class="m-1">
          </div>  
        </div> 
      </div>
    </div> 
    <div class="container mt-3">
      <input @keyup.enter="CreateComment" type="text" v-model="CommentCreateContext" placeholder="댓글 입력">
      <button @click="CreateComment" class="btn btn-outline-light m-2" value="Add">Add</button>
    </div>    
  </div>
</template>
      

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import axios from 'axios'
const ReviewURL = `http://127.0.0.1:8000/api/c1/freeboards/`
const getUsernameURL = "http://127.0.0.1:8000/accounts/user/"
const commentURL = "http://127.0.0.1:8000/api/c1/freeboards/article/comment/"
const commentUpdateURL = "http://127.0.0.1:8000/api/c1/freeboards/comment/"
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
    // 댓글 가져오기
    GetComments(){
      const token = this.$store.state.token
      axios({  
          method: 'get',
          url: commentURL + this.ReviewId + '/',
          headers:  {
          Authorization : `Token ${token}`
        },
      })
      .then((response) => {
        this.Comments = response.data
      })
      .catch((err)=>{
        this.Comments=[]
        console.log(err)
      })
    },
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
      .then(() => {
        this.GetComments()
        this.CommentCreateContext = ''
        })
      
    },
    StartUpdateComment(comment_id, content){  // 토글기능. 리스트에 없으면 넣고 있으면 뺀다
      console.log(comment_id)
      if (this.UpdatingCommentId.includes(comment_id)) {
          // 이미 수정 중인 경우
          this.UpdateComment(comment_id, content);
        } 
      else {
        this.UpdatingCommentId.push(comment_id);
      }
      console.log(this.UpdatingCommentId)
    },
    UpdateComment(comment_id, content){
      const token = this.$store.state.token
      axios({  
        method: 'put',
        url: commentUpdateURL + comment_id + '/',
        data: {
          content 
          },
        headers:  {
        Authorization : `Token ${token}`
          },
        })
      .then((res) => {
        this.UpdatingCommentId = this.UpdatingCommentId.filter(function(element) {
          return element !== res.data.id
        });
      })
    },
    DeleteComment(id){
      const token = this.$store.state.token
      axios({
        method: 'delete',
        data: {
          id
        },
        url: commentUpdateURL + id + '/',
        headers: {
          Authorization : `Token ${token}`
        }
        })
        .then(()=>{
          // 댓글 가져오기
          this.GetComments()
        }
        )
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
    })
    .catch((err)=>{
      console.log(err)
    })

  }
}

</script>

<style>

</style>
