<template>
  <div>
    <a href="http://localhost:8080/detail"><img :src=PosterURL alt=""></a>
    <!-- <p>{{ movie.title }}</p> -->
    <!-- <p>{{ movie.overview }}</p> -->
  </div>
</template>

<script>

export default {
  name: 'MovieCard',
  data() {
    return {
      PosterURL: `https://image.tmdb.org/t/p/w300${this.movie.poster_path}`
    }
  },
  props: {
    movie: Object
  }
}

</script>

<style>

</style>