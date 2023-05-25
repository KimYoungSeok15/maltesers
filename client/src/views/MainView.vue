<template>
  <div style="color:rgb(50,50,50)">
    <NavigationBar/>
    <div class="backdropcontainer-wrapper" style="height: 800px">
      <h2 class="fw-semibold" style="color:black; z-index:3; position:absolute; top:230px;">오늘의 영화</h2>
      <div v-show="MostPopMovie" class="backdropcontainer" :style="{
        backgroundImage: `linear-gradient(to bottom, transparent, rgba(219, 223, 234, 0.7)), url(https://image.tmdb.org/t/p/original${MostPopMovie.backdrop_path})`,
        backgroundPosition: 'center'}">
        <div class="row box1" style="width: 1000px; display: flex; justify-content: center;">
          <div class="col-3" style="height: 400px; width: 300px;">
            <img class="donggle_poster" style="cursor: pointer; width: 100%; height: 100%; object-fit: contain;" @click="GoDetail(MostPopMovie.id)" :src="`https://image.tmdb.org/t/p/original${MostPopMovie.poster_path}`" alt="">
          </div>
        </div>			
      </div>
    </div>
    <br>
    <h2 class="fw-semibold py-0 px-4" style="position:relative; text-align: left; z-index:4;">평점 높은 영화</h2>
    <hr>
    <carousel-container id="carousel" :movies="RateSortedMovies"></carousel-container>

    <br>
    <h2 class="fw-semibold py-0 px-4" style="text-align: left;">최신 영화</h2>
    <hr>
    <carousel-container :movies="LatestSortedMovies"></carousel-container>

    <br>
    <h2 class="fw-semibold py-0 px-4" style="text-align: left;">인기 영화</h2>
    <hr>
    <carousel-container :movies="PopularitySortedMovies"></carousel-container>
    <br>

	</div>	
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import CarouselContainer from '@/components/CarouselContainer.vue'
import axios from 'axios'
export default {
  components: {
    NavigationBar,
		CarouselContainer
  },
  data() {
    return {
      movieAll: [],
      RateSortedMovies: [],
      LatestSortedMovies: [],
      PopularitySortedMovies: [],
      PopMovies: [],
      MostPopMovie: null
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    calculateScore(movie) {
      let score = 0

      // adult 점수 계산
      if (movie.adult === false) {
        score += 10
      }

      // original_language 점수 계산
      if (movie.original_language === "ko") {
        score += 30
      } else if (movie.original_language === "en") {
        score += 10
      }

      // popularity 점수 계산
      score += Math.floor(movie.popularity / 100);

      // vote_average 점수 계산
      score += Math.round(movie.vote_average * 10)

      // vote_count 점수 계산
      score += Math.floor(movie.vote_count / 100)

      return score
    },
		GoDetail(movieId){
			this.$router.push(`detail/${movieId}`)
		}
  },
  created() {
		const TMDB_URL = `https://api.themoviedb.org/3/movie/popular?`		
    const djangoMovie = 'http://127.0.0.1:8000/api/m1/movies/'
		this.isLogin
    if (this.isLogin) {
			const params = {
				api_key: process.env.VUE_APP_Movie_API,
				language: 'ko-KR',
				region: 'KR',				
				page: '1'
			}			
			// TMDB에서 인기있는 영화들을 가져온다.
			axios({
				methods: 'get',
				url: TMDB_URL,
				params: params,
			})
			.then((res)=>{
				this.PopMovies = res.data.results
				let tempObj = [...res.data.results]
				tempObj.sort((a,b)=>new Date(a.release_date)- new Date(b.release_date))			
				let maxScore = 0
				for (const movie in this.PopMovies) {
					let score = this.calculateScore(this.PopMovies[movie])
					console.log(score, movie)
					for (const [index, mov] of tempObj.entries()){
						if (mov.release_date === this.PopMovies[movie].release_date){
							score += index
						}
					}
					if (score > maxScore) {
						maxScore = score
						this.MostPopMovie = this.PopMovies[movie]
					}
				}				
			})
		// 전체 영화를 Django DB에서 받아와서 Store에 저장
			axios({
			methods: 'get',
			url: djangoMovie,
		})
		.then((response) => {
		this.movieAll = response.data
		let temp1 = response.data
		let temp2 = response.data
		let temp3 = response.data
		temp1.sort((a,b)=>b.vote_average-a.vote_average)
		this.RateSortedMovies = temp1.slice(0,24)
		temp2.sort((a,b)=>new Date(b.release_date)- new Date(a.release_date))
		this.LatestSortedMovies = temp2.slice(0,24)
		temp3.sort((a,b)=>b.popularity-a.popularity)
		this.PopularitySortedMovies = temp3.slice(0,24)
		this.$store.dispatch('getAllMovies', this.movieAll)  
		})
		} 
		else {
        alert('로그인이 필요한 서비스 입니다')
        this.$router.push({ name: 'login'})
		}
	},

}

</script>

<style scoped>
.backdropcontainer-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 471px;
}

.backdropcontainer {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  height: 1000px;
  box-sizing: border-box;
  padding: 0px;
  z-index: 0;
}
</style>
