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
            <!-- <input class="col-4 border-white text-white" style="background-color: transparent;" type="text" v-model="genreName" placeholder="내용을 입력해주세요"> -->
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
            <input class="col-1 border-white text-white" style="background-color: transparent;" type="number" min="1" max="10" v-model="rating" placeholder="">
            <div class=""></div>
            <br>
            <div class="col-1">내용 :</div>
            <input class="col-10 border-white text-white" style="padding-bottom: 300px; background-color: transparent;"  type="text" v-model="reviewContent" placeholder="내용을 입력해주세요">
            <div class=""></div>
            <br>
            <div><button @click="postReview" class="btn btn-outline-light col-2 mt-4" value="Add">Add</button> <br></div>
        </div>
        <br>
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
      point = point + 50000// 글 쓸때 1000씩 경험치 부여
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
      console.log(typeof this.reviewTitle)
      console.log(typeof this.catch_movie_title)
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