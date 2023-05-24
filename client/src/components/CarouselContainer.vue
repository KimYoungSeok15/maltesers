<template>
  <div class="total-carousel-container">
    <carousel :per-page="6" :paginationEnabled="false">
      <slide v-for="(movie, index) in movies" :key="index">
        <MainSlideCard class="mx-5 w-75" :slide="movie"/> 					
      </slide>
    </carousel>		
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel'
import MainSlideCard from '../components/MainSlideCard.vue'

export default {
  components: {
    Carousel,
    Slide,
    MainSlideCard,
  },
  props: {
    movies: Array,
  },
};
</script>