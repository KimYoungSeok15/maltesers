<template>
  <div class="back" >
    <NavigationBar/>
    <br>
    <div class="container" :style="{ 'background': `url(https://image.tmdb.org/t/p/original${movieDetail.backdrop_path})`, 'opacity': '0.7' }">
      <br>
      <div class="row">
          <img class="col-4" :src="`https://image.tmdb.org/t/p/w400${movieDetail.poster_path}`" alt="">
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
          </div>
          <br>
      </div>
    </div>
    <h2>비슷한 영화</h2>
    <div class="row">
      <span class="col-3" v-for="mv in recommendDetails" :key="mv.id">
        <span @click="move(mv.id)">
          <p>{{mv.title}}</p>
            <img style="width:300px; height:400px; object-fit: cover;" class="mx-4" :src="`https://image.tmdb.org/t/p/w300${mv.poster_path}`" alt="">
        </span>
      </span> 
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
  methods:{
    // 좋아요 리스트에 추가
    likes_plus(movieDetail) {
      alert('좋아요 추가')
      const user_name = this.$store.state.nowUserName
      const movie_id = movieDetail.id
      const movie_name = movieDetail.title
      const token = this.$store.state.token
      axios({  
          method: 'post',
          url: `http://127.0.0.1:8000/accounts/profile/Likes/${user_name}/`,
          data: {
            user_name, movie_name, movie_id
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
  data(){
    return{
      movieId: Number(this.$route.params.id),
      movieDetail: {},
      recommendDetails: [],
      // id: this.$route.params.id
    }
  },
  beforeRouteUpdate(to,from,next){
    this.movieId = to.params.id
    this.getMovie()
    next()
  },

  computed: {
    ...mapState(['mainTopMovies', 'playingMovies', 'upComingMovies']),
	},
  created() {
    this.getMovie()
  }
  
}
</script>

<style>
</style>