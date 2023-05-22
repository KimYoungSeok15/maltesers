<template>
	<div>
	<NavigationBar/>
    <br>
		<h1>전체 영화 페이지입니다</h1>
    <br>
		<!-- <div>{{RateSortedMovies}}</div> -->
		<div class=" d-flex row row-col-2">
			<div class="card col-2" v-for="(movie, index) in this.RateSortedMovies" :key="index"> 
				<main-Top-card :top="movie"/>  
				<!-- main-Top-card : 컴포넌트, top: prop, movie: for문 변수 -->
				<!-- <span>{{movie.title}}</span> -->
				<!-- <span>{{movie.vote_average}}</span>
				<span>{{movie.genre_ids}}</span> -->
			</div>
		</div>
	</div>	
</template>

<script>
import MainTopCard from '../components/MainTopCard.vue'
import NavigationBar from '@/components/NavigationBar.vue'
import axios from 'axios'
export default {
	components: {
		NavigationBar,
		MainTopCard
	},
  data() {
    return {
			movieAll: '',
		RateSortedMovies: ''
		}
	},
	computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  // 전체 영화를 Django DB에서 받아와서 Store에 저장
  created() {
    const djangoMovie = 'http://127.0.0.1:8000/api/m1/movies/'
	this.isLogin
      if (this.isLogin) {
		axios({
			methods: 'get',
			url: djangoMovie,
		})
		.then((response) => {
		// console.log(response.data[0].title) - '대부'
		this.movieAll = response.data
				let temp = response.data
				this.RateSortedMovies = temp.sort((a,b)=>b.vote_average-a.vote_average)
		this.$store.dispatch('getAllMovies', this.movieAll)  
		console.log(this.$store.state.allMovies)
		})
	} else {
		alert('로그인이 필요한 서비스 입니다')
		this.$router.push({ name: 'login'})
	}
	}


	// computed: {
    // ...mapState(['mainTopMovies', 'playingMovies'])
	// },

		// const TOPURL = 'https://api.themoviedb.org/3/movie/top_rated?'
		// const params = {
		// api_key: process.env.VUE_APP_Movie_API,
		// language: 'ko-KR',
		// page: '1',
		// }
		
		// 1. 평점 높은 영화 불러오기


		// 2. 최신 영화 불러오기


		// 3. 개봉 예정영화 불러오기
		// axios({
		// 		methods: 'get',
		// 		url: UPCOMINGURL,
		// 		params: params,
		// })
		// .then((response) => {
		// this.upComing = response.data.results
		// this.$store.dispatch('upComing', this.upComing)
		// tM() {
		//   return this.$store.state.topRatedMovies
		// },
		
		// ...mapState({
		//   msg: state => state.topRatedMovies
		// }),
		// })
}

</script>

<style>

</style>
