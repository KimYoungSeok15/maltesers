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
    }
  },
  props: {
    movie: Object
  }
}

</script>

<style>

</style>