<template>
  <div class="backdropcontainer" style="min-height:1250px;">
	<NavigationBar/>
		<br>
		<h1>Movie</h1>
		<hr>
		<input class="my-5" v-model="SearchText" @keyup.enter="Search" type="text"> <button @click="Search" class="btn btn-primary">검색</button>
		<div v-if="!SearchedMovies" class="d-flex row row-col-2">
			<div class="col-2 mb-4 p-10" v-for="(movie, index) in this.visibleMovies" :key="index"> 
				<main-Top-card :top="movie"/>  
			</div>
		</div>
		<div v-if="SearchedMovies" class="d-flex row row-col-2">
			<div class="col-2 mb-4 p-10" v-for="(movie, index) in this.visibleMovies" :key="index"> 
				<main-Top-card :top="movie"/>  
			</div>
		</div>
<ul class="pagination d-flex justify-content-center">
    <!-- 이전 버튼 -->
    <li class="page-item" :class="{ 'disabled': currentPage === 1 }">
      <a class="page-link" href="javascript:void(0)" @click="goToPage(currentPage - 1)">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
    <!-- 페이지 번호 버튼 -->
    <li class="page-item" v-for="page in totalPages" :key="page" @click="goToPage(page)" :class="{ active: currentPage === page }">
      <a class="page-link" href="javascript:void(0)" :style="{ backgroundColor: currentPage === page ? '#fff' : '#0f0f0f', color: currentPage === page ? '#0f0f0f' : '#fff' }">{{ page }}</a>
    </li>
    <!-- 다음 버튼 -->
    <li class="page-item" :class="{ 'disabled': currentPage === totalPages }">
      <a class="page-link" href="javascript:void(0)" @click="goToPage(currentPage + 1)">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  </ul>
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
			RateSortedMovies: '',
			SearchedMovies: '',
			SearchText: '',
      currentPage: 1, // 현재 페이지 번호
      moviesPerPage: 12, // 페이지당 영화 개수			
		}
	},
	watch: {
		SearchText(text){
			if (!text){
			this.SearchedMovies = ''
		}}
	},
	computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    totalPages() {
      if (this.SearchedMovies) {
        // 검색된 영화의 전체 페이지 수 계산
        return Math.ceil(this.SearchedMovies.length / this.moviesPerPage)
      } else {
        // 전체 영화의 전체 페이지 수 계산
        return Math.ceil(this.RateSortedMovies.length / this.moviesPerPage)
      }
    },		
    visibleMovies() {
      let startIndex = (this.currentPage - 1) * this.moviesPerPage
      let endIndex = startIndex + this.moviesPerPage
      if (this.SearchedMovies) {
        // 검색된 영화에서 현재 페이지에 해당하는 영화들 반환
        return this.SearchedMovies.slice(startIndex, endIndex)
      } else {
        // 전체 영화에서 현재 페이지에 해당하는 영화들 반환
        return this.RateSortedMovies.slice(startIndex, endIndex)
      }
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
			this.movieAll = response.data
			let temp = response.data
			this.RateSortedMovies = temp.sort((a,b)=>b.vote_average-a.vote_average)
			this.$store.dispatch('getAllMovies', this.movieAll)  
		})
	} else {
		alert('로그인이 필요한 서비스 입니다')
		this.$router.push({ name: 'login'})
	}
	},
	methods:{
		Search(){
			const SearchURL = `https://api.themoviedb.org/3/search/movie?query=${this.SearchText}`
			const params = {
				api_key: process.env.VUE_APP_Movie_API,
				language: 'ko-KR',
				page: '1'
			}			
			axios({
				methods: 'get',
				url: SearchURL,
				params: params,
			})
			.then((res)=>{
				this.SearchedMovies = res.data.results
			})
			this.goToPage(1)
		},
    goToPage(page) {
      this.currentPage = page // 페이지 이동
    }		
	}
}
</script>

<style scoped>
.backdropcontainer {
  background:url("@/assets/eternal12.jpg");
  opacity: 0.9;
}
.pagination .page-link {
	margin-top: 20px;
  background-color: #0f0f0f;
  color: #fff;
	border-color: rgb(77, 77, 77);
	outline: none; /* 클릭시 파란색 테두리 제거 */
	box-shadow: none;
}

.pagination button {
  margin-right: 5px;
  background-color: #eaeaea;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
}

.pagination button.active {
  background-color: #ccc;
}

input {
  border-radius: 10px;
  } 
</style>
