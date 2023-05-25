<template>
  <div class="total-carousel-container">
    <carousel :per-page="6" :paginationEnabled="false">
      <slide v-for="(movie, index) in movies" :key="index">
        <MainSlideCard class="" :slide="movie"/> 					
      </slide>
    </carousel>		
  </div>
</template>

<script scoped>
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

<style scoped>
.box1 {
  border-radius: 10px;
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.9);
}
</style>