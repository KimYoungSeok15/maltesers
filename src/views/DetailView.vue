<template>
  <div>
    <NavigationBar/>
    <h1 >영화 '' {{movieDetail.title}} '' 상세 내용</h1>
    <img :src="`https://image.tmdb.org/t/p/w200${movieDetail.poster_path}`" alt="">
    <p> {{movieDetail.title}} </p>
    <br>
    <p>"{{movieDetail.tagline}}"</p>
    <h2 class="mt-5">추천영화</h2>
    <div v-for="mv in recommendDetails" :key="mv.id">
      <div @click="move(mv.id)">
        <img class="mx-4" :src="`https://image.tmdb.org/t/p/w200${mv.poster_path}`" alt="">
      </div>
      <p>{{mv.title}}</p>
    </div>
    <p>
    <!-- {{movieDetail}} -->
    </p>
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

      // this.$router.go()
    }
  },
  beforeRouteUpdate(to,from,next){
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
        if (movieidx === '5'){
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