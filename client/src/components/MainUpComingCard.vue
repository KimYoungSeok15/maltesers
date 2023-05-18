<template>
  <div>
    <a href="http://localhost:8080/detail"><img :src=UpComingURL alt=""></a>
    <!-- <p>{{ movie.title }}</p> -->
    <!-- <p>{{ movie.overview }}</p> -->
  </div>
</template>

<script>

export default {
  name: 'MainUpComingCard',
  data() {
    return {
      UpComingURL: `https://image.tmdb.org/3/movie/upcoming/t/p/w200${this.upcoming.poster_path}`
    }
  },
  props: {
    upcoming: Object
  }
}

</script>

<style>

</style>