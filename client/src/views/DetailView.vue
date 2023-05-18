<template>
  <div>
    <NavigationBar/>
    <br>
    <div class="container">
      <br>
      <div class="row">
          <img class="col-4" :src="`https://image.tmdb.org/t/p/w400${movieDetail.poster_path}`" alt="">
          <div class="col-1"></div>
          <div class="col-4"> 
            <h1>{{movieDetail.title}} </h1>
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
    move(data){
      // console.log(data);
      this.$router.push({name:'detail', params: {id: data}})

      this.$router.go()
    }
  },
  beforeRouteUpdate(to,from,next){
    console.log(to);
    console.log(from);
    this.testid = to.params.id
    next()
  },
  data(){
    return{
      movieId: Number(this.$route.params.id),
      movieDetail: {},
      recommendDetails: [],
      testid: this.$route.params.id
    }
  },
  computed: {
    ...mapState(['mainTopMovies', 'playingMovies', 'upComingMovies']),
	},
  created() {
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
  }
  
}
</script>

<style>

</style>