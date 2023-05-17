<template>
	<div>
	<NavigationBar/>

		<h1>메인페이지입니다</h1>

		<h2>평점 높은 영화</h2>
		<div class=" d-flex row row-col-2">
			<div  class="card col-2" v-for="(movie, index) in mainTopMovies" :key="index"> 
				<main-Top-card :top="movie"/>
			</div>
		</div>

		<h2>상영중인 영화</h2>
		<div class=" d-flex row row-col-2">
			<div  class="card col-2" v-for="(movie, index) in playingMovies" :key="index"> 
				<main-playing-card :playing="movie"/>
			</div>
		</div>

		<h2>개봉 예정 영화</h2>
		<div class=" d-flex row row-col-2">
			<div  class="card col-2" v-for="(movie, index) in upComingMovies" :key="index"> 
				<main-up-coming-card :upcoming="movie"/>
			</div>
		</div> 
	</div>	
</template>

<script>
import MainTopCard from '../components/MainTopCard.vue'
import MainPlayingCard from '../components/MainPlayingCard.vue'
import MainUpComingCard from '../components/MainUpComingCard.vue'
import NavigationBar from '@/components/NavigationBar.vue'
import { mapState } from 'vuex'
import axios from 'axios'
export default {
	components: {
		NavigationBar,
		MainTopCard,
		MainPlayingCard,
		MainUpComingCard
	},
	data() {
		return {
		topRated: '',
		playing: '',
		upComing: '',
		}
	},
	computed: {
    ...mapState(['mainTopMovies', 'playingMovies', 'upComingMovies'])
	},
	created() {
		const TOPURL = 'https://api.themoviedb.org/3/movie/top_rated?'
		const PLAYINGURL = 'https://api.themoviedb.org/3/movie/now_playing'
		const UPCOMINGURL = 'https://api.themoviedb.org/3/movie/upcoming'
		const params = {
		api_key: process.env.VUE_APP_Movie_API,
		language: 'ko-KR',
		page: '1',
		}
		// 1. 평점 높은 영화 불러오기
		axios({  
				methods: 'get',
				url: TOPURL,
				params: params,
		})
		.then((response) => {
		this.topRated = response.data.results
		this.$store.dispatch('mainTopMovies', this.topRated)
		})

		// 2. 상영중인 영화 불러오기
		axios({
				methods: 'get',
				url: PLAYINGURL,
				params: params,
		})
		.then((response) => {
		this.playing = response.data.results
		this.$store.dispatch('mainPlaying', this.playing)
		})

		// 3. 개봉 예정영화 불러오기
		axios({
				methods: 'get',
				url: UPCOMINGURL,
				params: params,
		})
		.then((response) => {
		this.upComing = response.data.results
		this.$store.dispatch('upComing', this.upComing)
		// tM() {
		//   return this.$store.state.topRatedMovies
		// },
		
		// ...mapState({
		//   msg: state => state.topRatedMovies
		// }),
		})
	}
}
</script>

<style>

</style>
