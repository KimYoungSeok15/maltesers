<template>
  <div>
    <NavigationBar/>
    <div class="backdropcontainer" :style="{ backgroundImage: `linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url(https://image.tmdb.org/t/p/original${recommend_movie.backdrop_path})`}">
      <div v-if="check_input_genre" style="position: relative; display: inline-block;">
        <img src="@/assets/lalaland33.jpg" style="opacity: 0.5; width:100vW; height:1100px">
        <div  style="position: absolute; top: 40%; left: 50%; transform: translate(-50%, -50%); z-index: 1;">
          <h1 class="fw-semibold">{{ now_user }}님!</h1>
          <br>
          <h2 class="fw-semibold">{{ message }}</h2>
        </div>
      </div>
      <br>
      <div class="row box1">
        <div class="col-1"></div>
          <img class="col-3" :src="`https://image.tmdb.org/t/p/w300${recommend_movie.poster_path}`" style="'opacity': '1'; border-radius: 5%" alt="">
          <div class="col-1"></div>
          <div class="col-5">
          <h2 v-if="!check_input_genre">{{now_user}}님이 좋아하는 장르에 따른 추천 영화</h2>
          <br>
          <br>
          <!-- | <span v-for="genre in user_like_genre" :key="genre.id">
              <span>{{genre.genre_name}}</span>
              <span> | </span>
              <p>{{user_like_genre_id_name}}</p>
            </span> -->
            <div class="d-flex flex-wrap">
              <span class="col-2 mx-0 px-0" v-for="genre_list in all_genres" :key="genre_list.name">
                <span :class="{ 'white-border': pick_genre.includes(genre_list.name) }" class="p-1">{{ genre_list.name }}</span>
              </span>
            </div>
          <!-- <p>{{recommend_movie}}</p> -->
          <p>{{recommend_movie.title}}</p>
          <p>{{recommend_movie.vote_average}}</p>
          <p>{{recommend_movie.release_date}}</p>
          <p>{{recommend_movie.overview}}</p>
        </div>
        <img style="width:200px; height:60px" src="@/assets/copy.png" alt="">
      </div>
    </div>
  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import axios from 'axios'

export default {
    name: 'RecommendView',
    components: {
        NavigationBar,
    },
    data() {
      return {
        now_user: this.$store.state.nowUserName,
        recommend_movie_list : [],
        recommend_movie : [],
        user_like_genre: [],
        all_genres: [],
        user_like_genre_id_name: '',
        pick_genre: [],
        message: '',
        check_input_genre: true
      }
    },
    methods : {
      commonElements() {
        const commonElements = this.all_genres
        .filter(genre => {
          const matchingGenre = this.user_like_genre.find(userGenre => userGenre.genre_name === genre.name);
          return matchingGenre !== undefined;
        })
        .map(genre => genre.name); // name 속성만 추출하여 배열로 변환

      console.log(commonElements);
      this.pick_genre = commonElements;

      },    
      get_genre_movie_list(a) {
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/api/m1/movies`,
            })
            .then((res) => {
              console.log(a)
              for (let ll of a) {
                for (let l of res.data) {
                  if (l.genre_ids.includes(ll)) {
                    const duplicateMovieIndex = this.recommend_movie_list.findIndex(movie => movie.id === l.id);
                    if (duplicateMovieIndex !== -1) {
                      // 이미 중복된 키 값이 존재하는 경우 요소를 대체
                      this.recommend_movie_list.splice(duplicateMovieIndex, 1, l);
                    } else {
                      this.recommend_movie_list.push(l);
                    }
                  }
                }
              }
            const length = this.recommend_movie_list.length;
            const randomNumber = Math.floor(Math.random() * length);
            console.log(typeof randomNumber)
            console.log(this.recommend_movie_list[randomNumber])
            this.recommend_movie = this.recommend_movie_list[randomNumber]
            })
        },
        get_all_genre() {
          axios({
              method: 'get',
              url: `http://127.0.0.1:8000/api/m1/movies/genres/`,
              })
              .then((res) => {
                console.log(res)
                let lst = []
                for (let j of this.user_like_genre) {
                  lst.push(j.genre_name) // 유저가 좋아하는 장르 이름 담은 배열
                }
                console.log(lst)
                this.all_genres = res.data
                let lst2 = this.all_genres.filter(i => lst.includes(i.name)).map(i => i.id);
                // let lst2 = [] // 유저가 좋아하는 장르 아이디와 이름 담은 배열
                // for (let k of lst) {
                //   for (let i of this.all_genres) {
                //     if (i.name == k) {
                //       lst2.push(i.id)
                //     } 
                // }
                console.log(lst2)
                this.user_like_genre_id_name = lst2
                this.get_genre_movie_list(this.user_like_genre_id_name)
                this.commonElements()

              
                
              })
        },
        call_like_genre() {
          const user_name = this.$store.state.nowUserName
          console.log(user_name)
          axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/profile/userprofile/user_like_genre/${user_name}/`,
          headers:  {
              Authorization : `Token ${this.$store.state.token}`
            }
          })
          .then((res) => {
            console.log(res)
            this.user_like_genre = res.data
            console.log('call_like_genre 실행')
            this.get_all_genre()
            
            
            
          })
          .catch(() => {
            console.log("좋아하는 장르 데이터베이스 빈 값")
            this.like_genre_list = ''
            this.message = '프로필에서 좋아하는 장르 입력하고 영화 추천을 받아보세요!'
            this.check_input_genre = 'false'
          })
      },
    },
    created() {
      this.call_like_genre()

      
    }
}
</script>

<style>
.white-border {
  border: 1px solid white;
}
</style>