<template>
  <div class="back" >
    <NavigationBar/>
    <div class="backdropcontainer" :style="{ backgroundImage: `linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url(https://image.tmdb.org/t/p/original${movieDetail.backdrop_path})`}">
      <br>
      <div class="row box1">
        <div class="col-1"></div>
          <img class="col-4 donggle_poster" :src="`https://image.tmdb.org/t/p/w400${movieDetail.poster_path}`" style="'opacity': '1';" alt="">
          <div class="col-1"></div>
          <div class="col-4"> 
            <h1>{{movieDetail.title}} </h1>
            <button @click="likes_plus(movieDetail)" >좋아요</button>
            <br>
            <p>평점 :{{movieDetail.vote_average}}</p>
            <p>개봉일 :{{movieDetail.release_date}}</p>
            <span v-for="genre in movieDetail.genres" :key="genre.id">{{genre.name}}  </span>
            <br>
            <br>
            <p>{{movieDetail.overview}}</p>
            <br>
            <div class="border">
              <div>
                <button class="btn btn-outline-light m-3"><router-link class="aa" :to="{ name: 'reviewcreate', params: { movie_title: `${movieDetail.title}` }}">리뷰 작성</router-link></button>
                <p>이 영화의 최근 리뷰</p>
                <div>
                  <div class="m-1">
                    <a class="aa" v-if="related_reviews[0]" :href="`http://localhost:8080/review/${related_reviews[0].id}`">
                      [{{related_reviews[0].title}}]
                    </a>
                    <p v-else >이 영화의 리뷰가 아직 없습니다!</p>
                    
                  </div>
                  <br>
                </div>
              </div>
            </div>
          </div>
          <br>
      </div>
      <h2>비슷한 영화</h2>
      <div class="row">
      <span class="col-3" v-for="mv in recommendDetails" :key="mv.id">
        <span @click="move(mv.id)">
          <p>{{mv.title}}</p>
            <img style="width:300px; height:400px; object-fit: cover;" class="mx-4 donggle_poster" :src="`https://image.tmdb.org/t/p/w300${mv.poster_path}`" alt="">
        </span>
      </span> 
    </div>
    </div>
  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import { mapState } from 'vuex'
import axios from 'axios'

const URL = `https://api.themoviedb.org/3/movie/`
const params = {
api_key: process.env.VUE_APP_Movie_API,
language: 'ko-KR'
}
export default {
  components: {
    NavigationBar,
  },
  data(){
    return{
      movieId: Number(this.$route.params.id),
      movieDetail: {},
      recommendDetails: [],
      related_reviews_keyword: '',
      related_reviews: [],
    }
  },
  beforeRouteUpdate(to,from,next){
    this.movieId = to.params.id
    this.getMovie()
    next()
  },
  methods:{
    call_review() {
      console.log(this.related_reviews_keyword)
      const key = this.related_reviews_keyword
      console.log(key)
      axios({  
          method: 'get',
          url: `http://127.0.0.1:8000/api/c1/freeboards/${key}/`,
      })
      .then((res) => {
        console.log(res, 'ㅁㅁㅁㅁㅁㅁㅁㅁㅁ')
        this.related_reviews = res.data
        this.related_reviews.reverse()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 좋아요 리스트에 추가
    likes_plus(movieDetail) {
      alert('좋아요 추가')
      const user_name = this.$store.state.nowUserName
      const movie_id = movieDetail.id
      const movie_name = movieDetail.title
      const poster_path = movieDetail.poster_path
      const token = this.$store.state.token
      axios({  
          method: 'post',
          url: `http://127.0.0.1:8000/accounts/profile/Likes/${user_name}/`,
          data: {
            user_name, movie_name, movie_id, poster_path
          },
          headers:  {
            Authorization : `Token ${token}`
          },
      })
      .then((res) => {
        console.log(res)
      })
    },  
    getMovie() {
      axios({  
          methods: 'get',
          url: URL+this.movieId,
          params: params,
      })
      .then((response) => {
        console.log(response);
        this.movieDetail = response.data
        console.log(this.movieDetail, 'ㅁㄴㅇㅁㄴㅇㅁㄴㅇㄴ')
        this.related_reviews_keyword= this.movieDetail.title.slice(0,2)  
        this.call_review()
      })
      axios({  
          methods: 'get',
          url: URL+this.movieId+'/recommendations',
          params: params,
      })
      .then((response) => {
        console.log(response.data.results);
        for (const movieidx in response.data.results) {
          if (movieidx === '4'){
            break
          }
          this.recommendDetails.push(response.data.results[movieidx])
        }
      });
    },
    move(data){
      // console.log(data);
      this.$router.push({name:'detail', params: {id: data}})

      this.$router.go()
    }
  },
  computed: {
    ...mapState(['mainTopMovies', 'playingMovies', 'upComingMovies']),
	},
  created() {
    this.getMovie()

  },

  
}
</script>

<style scoped>
  .donggle_poster {
    border-radius: 5%;
  }
  .backdropcontainer {
    min-height: 1200px
  }
  .box1 { 
    min-height: 605px
  }
    /* a 태그에 밑줄 제거 */
  .aa {
    text-decoration: none;
    color: white; /* 원하는 색깔로 변경하세요 */
  }
  
  .review_create_a {
    text-decoration: none;
    color: black; /* 원하는 색깔로 변경하세요 */
  }

  .aa:hover {
    color: white; /* 마우스 호버 시 변경할 색깔을 설정하세요 */
    font-weight: bold; /* 호버 시 글꼴 굵기 설정 */
  }

</style>