<template>
  <div>
    <NavigationBar/>
    <br>
    <h2>좋아하시는 장르에 따른 추천 영화</h2>
      <p>{{user_like_genre}}</p>
    | <span v-for="genre in user_like_genre" :key="genre.id">
      <span>{{genre.genre_name}}</span>
      <span> | </span>
    </span>
    <p>{{all_genres}}</p>
    <p>{{user_like_genre_id_name}}</p>
    <p>{{recommend_movie_list}}</p>
    <p>{{recommend_movie_list[0]}}</p>
    <p>{{recommend_movie_list[1]}}</p>

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
        recommend_movie_list : [],
        recommend_movie : '',
        user_like_genre: '',
        all_genres: '',
        user_like_genre_id_name: ''
      }
    },
    methods : {
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
                      console.log('포함')
                      this.recommend_movie_list.push(l) // 유저가 선호하는 장르의 영화 리스트에 저장
                    }
                  }
                }
              const randomNumber = Math.floor(Math.random() * this.recommend_movie_list.length); // 난수 생성
              this.recommend_movie_list[randomNumber] = this.recommend_movie // 유저가 선호하는 장르의 영화 리스트에서 임의의 난수로 추출하여 영화 추천
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
                let lst2 = [] // 유저가 좋아하는 장르 아이디와 이름 담은 배열
                for (let k of lst) {
                  for (let i of this.all_genres) {
                    if (i.name == k) {
                      lst2.push(i.id)
                    } 
                }
                console.log(lst2)
                this.user_like_genre_id_name = lst2
                this.get_genre_movie_list(this.user_like_genre_id_name)
                }
                
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
            this.get_all_genre()

            
            
          })
          .catch(() => {
            console.log("좋아하는 장르 데이터베이스 빈 값")
            this.like_genre_list = ''
          })
      },
    },
    created() {
      this.call_like_genre()
    }
}
</script>

<style>

</style>