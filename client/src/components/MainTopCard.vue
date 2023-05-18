<template>
  <div>
    <router-link :to="`detail/${top.movie_id}`"><img :src=TopURL alt=""></router-link>
    <!-- <a href="http://localhost:8080/detail"><img :src=PlayingURL alt=""></a>
    <a href="http://localhost:8080/detail"><img :src=upcomingURL alt=""></a> -->
    <!-- <p>{{ movie.title }}</p> -->
    <!-- <p>{{ movie.overview }}</p> -->
    <!-- {{top}} -->
  </div>
</template>

<script>

export default {
  name: 'MainTopCard',
  data() {
    return {
      TopURL: `https://image.tmdb.org/t/p/w200${this.top.poster_path}`
    }
  },
  props: {
    top: Object
  }
}

</script>

<style>

</style>