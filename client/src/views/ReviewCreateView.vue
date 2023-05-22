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
            <input class="col-10" type="text" v-model="reviewTitle" placeholder="제목을 입력해주세요">
            <div class=""></div>
            <br>
            <div class="col-1">내용 :</div>
            <input class="col-10" style="height:500px;"  type="text" v-model="reviewContent" placeholder="내용을 입력해주세요">
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
            <div class="col-1">평점 :</div>
            <input class="col-1" type="number" min="1" max="10" v-model="rating" placeholder="">
            <div class=""></div>
            <div><button @click="postReview" class="btn btn-primary col-2 mt-4" value="Add">Add</button></div>
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
      movieTitle:"",
      genreName:"",
      rating: 5
    }
  },
  components: {
    NavigationBar
  },
  methods:{
    postReview(){
      const title = this.reviewTitle
      const content = this.reviewContent     
      const token = this.$store.state.token
      const Movie_title = this.movieTitle
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