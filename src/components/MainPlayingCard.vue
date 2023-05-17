<template>
  <div>
    <a href="http://localhost:8080/detail"><img :src=PlayingURL alt=""></a>
    <!-- <p>{{ movie.title }}</p> -->
    <!-- <p>{{ movie.overview }}</p> -->
  </div>
</template>

<script>

export default {
  name: 'MainPlayingCard',
  data() {
    return {
      PlayingURL: `https://image.tmdb.org/t/p/w200${this.playing.poster_path}`,
    }
  },
  props: {
    playing: Object
  }
}

</script>

<style>

</style>