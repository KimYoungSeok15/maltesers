<template>
  <div>
    <NavigationBar/>
    <br>
    <h1>랜덤 영화 조회</h1>
    <button @click="refresh" class="btn btn-primary m-3">pick</button>
    <br>
    <img :src="randomMoviesPoster">
    <h3 class="fw-bold mt-3">{{ randomMoviesTitle }}</h3>

  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'RandomView',
  components: {
    NavigationBar,
  },
  data() {
    return {
      inDex: 0,
      randomMoviesPoster :null,
      randomMoviesTitle :null,
    }
  },
  methods: {
    refresh(){
      this.$router.go()
    }
  },
  computed: {
    ...mapState(['topRatedMovies']),

  },
  created() {
    const TMDBURL = 'https://api.themoviedb.org/3/movie/top_rated?'
    const params = {
      api_key: process.env.VUE_APP_Movie_API,
      language: 'ko-KR',
      page: '1',
    }
    axios({
        methods: 'get',
        url: TMDBURL,
        params: params,
    })
    .then((response) => {
      console.log(response)
      this.movieAllData = response.data.results
      this.$store.dispatch('topRatedMovies', this.movieAllData)
      const pickIndex = Math.floor(Math.random() * (this.$store.state.topRatedMovies.length-1))
      console.log(pickIndex)
      this.inDex = pickIndex
      this.randomMoviesTitle = this.$store.state.topRatedMovies[this.inDex].title
      this.randomMoviesPoster = `https://image.tmdb.org/t/p/w300${this.$store.state.topRatedMovies[this.inDex].poster_path}`

    })
  }
}

</script>

<style>
  .underline-on-hover {
    text-decoration: none;
    font-weight: normal;
    font-size: 19px; /* 초기 글자 크기 */
  }

  .underline-on-hover:hover {
    text-decoration: underline;
    font-weight: bold;
    font-size: 19px; /* 마우스를 올렸을 때 큰 글자 크기 */
  }
</style>