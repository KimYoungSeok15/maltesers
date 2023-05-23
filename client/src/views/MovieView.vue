<template>
	<div>
	<NavigationBar/>
    <br>
		<h1>전체 영화 페이지입니다</h1>
    <br>
		<div class=" d-flex row row-col-2">
			<div class="col-2" v-for="(movie, index) in this.RateSortedMovies" :key="index"> 
				<main-Top-card :top="movie"/>  
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


}

</script>

<style>

</style>
