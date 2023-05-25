<template>
  <div>
    <NavigationBar/>
    <div class="backdropcontainer" :style="{ backgroundImage: `linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url(https://image.tmdb.org/t/p/original${randomMovies.backdrop_path})`}" >
      <button @click="refresh" class="btn btn-outline-light m-3 m-3">Random!</button>
      <br>
      <div class="container">
        <div class="row">
          <router-link class="col-12 my-5" :to="`../detail/${randomMovies.movie_id}`" >
            <img style="border-radius: 5%;" :src="`https://image.tmdb.org/t/p/w300${randomMovies.poster_path}`">
          </router-link> 
          <div class="col-4" ></div>
          <div class="col-4">
            <h3 class="fw-bold mt-3">{{ randomMovies.title }}</h3>
            <!-- <p class="fw-bold mt-3">{{ randomMovies_genre_name }}</p> -->
            <p class="fw-bold mt-3">{{ randomMovies.overview}}</p>
          </div>
        </div>
      </div>
    </div>
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
      randomMovies :null,
      randomMovies_genre_name :null,
    }
  },
  methods: {
    refresh(){
      this.render()
    },
    render(){
      const HooniMovie = 'http://127.0.0.1:8000/api/m1/movies/'
      
      axios({
        methods: 'get',
        url: HooniMovie,
      })
      .then((response) => {
        console.log(response.data.length-1)
        let previousNumbers = [];

        function generateUniqueRandomNumber() {
          const randomIndex = Math.floor(Math.random() * response.data.length);
          
          if (previousNumbers.includes(randomIndex)) {
            // 이미 나온 수라면 재귀적으로 다시 호출하여 새로운 수를 생성합니다.
            return generateUniqueRandomNumber();
          }
          previousNumbers.push(randomIndex);
          // 중복을 방지한 유일한 수를 반환합니다.
          return randomIndex;
        }

        // 사용 예시
        console.log(generateUniqueRandomNumber(), 'asdsadasds');

        this.randomMovies = response.data[generateUniqueRandomNumber()]
        console.log(this.randomMovies)
        const genre_id_list = this.randomMovies.genre_ids
        axios({
            method: 'post',
            url: "http://127.0.0.1:8000/api/m1/movies/genrename/",
            data: {
              genre_id_list
            }
        })
        .then((res) => {
          console.log(res.data.genre_name_list)
          this.randomMovies_genre_name = res.data.genre_name_list

        })
      })
    }
  },
  computed: {
    ...mapState(['topRatedMovies']),

  },
  created() {
    this.render()
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
  .backdropcontainer {
    min-height: 1000px
  }
</style>