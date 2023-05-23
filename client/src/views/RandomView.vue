<template>
  <div>
    <NavigationBar/>
    <br>
    <h1>랜덤 영화 조회</h1>
    <button @click="refresh" class="btn btn-primary m-3">Random!</button>
    <br>
    <img :src="`https://image.tmdb.org/t/p/w300${randomMovies.poster_path}`">
    <h3 class="fw-bold mt-3">{{ randomMovies.title }}</h3>
    <p class="fw-bold mt-3">{{ randomMovies_genre_name }}</p>
    <p class="fw-bold mt-3">{{ randomMovies.overview}}</p>

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
      this.$router.go()
    }
  },
  computed: {
    ...mapState(['topRatedMovies']),

  },
  created() {
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
      console.log(generateUniqueRandomNumber());

      this.randomMovies = response.data[generateUniqueRandomNumber()]
      console.log(this.randomMovies.genre_ids)
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