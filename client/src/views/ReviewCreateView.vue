<template>
  <div>
    <NavigationBar/>
    <br>
    <h2 class="">게시글 등록</h2>
    <br>
    <br>
    <div class="container border">
      <br>
        <div class="row">
            <div class="col-1">제목 :</div>
            <input class="col-4 border-white text-white" style="background-color: transparent;" type="text" v-model="reviewTitle" placeholder="제목을 입력해주세요">
            <div class=""></div>
            <br>
            <div class="col-1">영화 제목 :</div>
            <input class="col-4 border-white text-white" style="background-color: transparent;" type="text" v-model="catch_movie_title" placeholder="내용을 입력해주세요" >
            <div class=""></div>
            <br>
            <div class="col-1">장르 :</div>
            <input class="col-4 border-white text-white" style="background-color: transparent;" type="text" v-model="genreName" placeholder="내용을 입력해주세요">
            <div class=""></div>
            <br>
            <div class="col-1">평점 :</div>
            <input class="col-1 border-white text-white" style="background-color: transparent;" type="number" min="1" max="10" v-model="rating" placeholder="">
            <div class=""></div>
            <br>
            <div class="col-1">내용 :</div>
            <input class="col-10 border-white text-white" style="height:500px; background-color: transparent;"  type="text" v-model="reviewContent" placeholder="내용을 입력해주세요">
            <div class=""></div>
            <br>
            <div><button @click="postReview" class="btn btn-outline-light col-2 mt-4" value="Add">Add</button></div>
        </div>
    </div>
  </div>
</template>

<script>
import NavigationBar from "@/components/NavigationBar.vue"
import axios from 'axios'
const getUsernameURL = "http://127.0.0.1:8000/accounts/user/"
const URL = "http://127.0.0.1:8000/api/c1/freeboards/"
export default {
  data(){
    return {
      reviewTitle:"",
      reviewContent:"",
      genreName:"",
      rating: 5,
      catch_movie_title : this.$route.params.movie_title,
      now_user: '',
    }
  },
  components: {
    NavigationBar
  },
  methods:{
    // 글 쓸 때마다 1000 포인트씩 획득
    getUserName_and_point_plus() {
      axios({  
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/user/`,
          headers:  {
          Authorization : `Token ${this.$store.state.token}`
          },
      })
      .then((res)=> {
        console.log(res)
        this.now_user = res.data.username
        this.getUserProfile_and_plus_point()
      })
    },
    getUserProfile_and_plus_point() {
      axios({  
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/profile/userprofile/${this.now_user}/`,
          headers:  {
          Authorization : `Token ${this.$store.state.token}`
          },
      }).then((res)=> {
        console.log(res.data.point)
        this.plus_point(res.data.point)
      })
    }, 
    plus_point(point) {
      point = point + 1000
      axios({  
          method: 'put',
          url: `http://127.0.0.1:8000/accounts/profile/userprofile/put/${this.now_user}/`,
          headers:  {
          Authorization : `Token ${this.$store.state.token}`
          },
          data: {
            point
          }
      }).then((res)=> {
        console.log(res.data)
      })
    },  
    postReview(){
      
      const title = this.reviewTitle
      const content = this.reviewContent     
      const token = this.$store.state.token
      const Movie_title = this.catch_movie_title
      const genre_name = this.genreName
      const rating = this.rating
      let user_name = ''
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
      this.getUserName_and_point_plus()
      axios({  
          method: 'get',
          url: getUsernameURL,
          headers:  {
          Authorization : `Token ${token}`
          },
      })
      .then((response) => {
        user_name = response.data.username
        console.log(user_name)
        axios({  
            method: 'post',
            url: URL,
            data: { title, content, user_name, Movie_title, genre_name, rating },
            headers:  {
            Authorization : `Token ${token}`
            },
        })
        .then(() => {
          this.$router.push({name: "review"})
        })        
      })
      }

    }
  },
  created() {
  }
}
</script>

<style>

</style>